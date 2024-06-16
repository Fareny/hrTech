
from flask import Flask, request, jsonify, send_from_directory,abort
from pymongo import MongoClient, DESCENDING, ASCENDING
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId
from icecream import ic
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from werkzeug.utils import secure_filename
import eventlet
import os
import pymorphy2
import requests
import schedule
import threading
import uuid
import json
import locale
morph = pymorphy2.MorphAnalyzer()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
bcrypt = Bcrypt(app)
SECRET_KEY = 'superpupersecretkey'
eventlet.monkey_patch()


app.config['SECRET_KEY'] = 'superpupersecretkey2'
socketio = SocketIO(app, async_mode='eventlet',cors_allowed_origins="*")

bot_token = "6972046408:AAGvwvFThZSZDq1Escyt7M5ZdAO3Bt9sS04"
client = MongoClient("mongodb://localhost:27017/")
db = client["hakaton"]
users_collection = db["users"]
jobs_collection = db["jobs"]
chats_collection = db['chats']
filters_collection=db['filters']
schedule_collection=db['schedule']
notification_collection=db['notification']
tests_colletion=db['tests']
test_result_collection=db['test_result']

app.config['UPLOAD_FOLDER'] = 'media'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

def generate_token(email):
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

@socketio.on('disconnect')
def disconnect():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"status": "error", "message": "Токен отсутствует"}), 401
    try:

        token_bytes = token.encode('utf-8')
        decoded_token = jwt.decode(token_bytes, SECRET_KEY, algorithms=['HS256'])
        email = decoded_token.get('email')
        if not email:
            return jsonify({"status": "error", "message": "Email отсутствует в токене"}), 401
        users_collection.update_one({'email': email}, {'$set': {'online': False}})
    except:
        return jsonify({"status": "error", "message": "Токен невалидный"}), 401



@socketio.on('connect')
def connect(auth):

    cookies = request.cookies


    token = cookies.get('auth_token')
    if not token:
        return jsonify({"status": "error", "message": "Токен отсутствует"}), 401

    try:

        token_bytes = token.encode('utf-8')
        decoded_token = jwt.decode(token_bytes, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Токен устарел"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Токен невалидный"}), 401

    email = decoded_token.get('email')
    if not email:
        return jsonify({"status": "error", "message": "Email отсутствует в токене"}), 401

    try:
        time=datetime.now()
        time=time.strftime("%Y-%m-%d %H:%M:%S")
        users_collection.update_one({'email': email}, {'$set': {'socket_id': request.sid,'last_seen':time,'online':True}})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Ошибка базы данных: {str(e)}"}), 500





@socketio.on('get-notifications')
def connect(auth):

    cookies = request.cookies


    token = cookies.get('auth_token')
    if not token:
        return jsonify({"status": "error", "message": "Токен отсутствует"}), 401

    try:

        token_bytes = token.encode('utf-8')
        decoded_token = jwt.decode(token_bytes, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Токен устарел"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Токен невалидный"}), 401

    email = decoded_token.get('email')
    if not email:
        return jsonify({"status": "error", "message": "Email отсутствует в токене"}), 401


    emit('notifications',{'notifications': potencial_notifications(email)},broadcast=True)


def potencial_notifications(email):
    user = users_collection.find_one({'email': email})

    notifications = []

    if user:
        if user.get('job_search') == 'Не указан':
            notifications.append({
                'title': 'Не указан район поиска работы',
                'message': 'Перейдите в профиль и укажите ваш район поиска работы',
                'type': 'profile',
                'link':'/profile',
                'id':'1'
            })

        if user.get('phone_number') == 'Не указан':
            notifications.append({
                'title': 'Не указан номер телефона',
                'message': 'Перейдите в профиль и укажите ваш номер телефона',
                'type': 'profile',
                'link':'/profile',
                'id':'2'
            })






        offline_messages = notification_collection.find({'user_name': email})
        for message in offline_messages:
            notifications.append({
                'text': 'У вас новое сообщение',
                'type': 'message',
                'chatId': message['chatId']
            })

    return notifications





@socketio.on('disconnect')
def disconnect():
    token=request.cookies.get('auth_token')
    if not token:
        return jsonify({"status": "error", "message": "Токен отсутствует"}), 401
    try:

        token_bytes = token.encode('utf-8')
        decoded_token = jwt.decode(token_bytes, SECRET_KEY, algorithms=['HS256'])
        email=decoded_token.get('email')
        if not email:
            return jsonify({"status": "error", "message": "Email отсутствует в токене"}), 401
        users_collection.update_one({'email': email}, {'$set': {'online':False}})



    except:
        return jsonify({"status": "error", "message": "Токен невалидный"}), 401


@socketio.on('join_chat')
def on_join(data):
    username = data['username']
    room=data['room']
    join_room(room)
    send(f"{username} has entered the room.", to=room)




@app.route('/api/logout', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def logout():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"status": "error", "message": "Токен отсутствует"}), 401

    try:

        token_bytes = token.encode('utf-8')
        decoded_token = jwt.decode(token_bytes, SECRET_KEY, algorithms=['HS256'])
        email = decoded_token.get('email')
        if not email:
            return jsonify({"status": "error", "message": "Email отсутствует в токене"}), 401
        users_collection.update_one({'email': email}, {'$set': {'online': False}})
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Токен невалидный"}), 401

    response = jsonify({"status": "ok", "message": "Вы вышли из системы"})
    response.delete_cookie('auth_token', path='/', domain=None, samesite='None', secure=True)
    return response


@app.route('/api/get-messages', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def get_messages23():
    token = request.cookies.get('auth_token')

    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    id_chat = request.args.get('chatId')
    if not id_chat:
        return jsonify({"error": "id_chat parameter is required"}), 400

    chat = chats_collection.find_one({"id_chat": id_chat})
    if not chat:
        return jsonify({"error": "No messages found for this chat ID"}), 404

    user = users_collection.find_one({'email': email})
    if not user:
        return jsonify({"error": "User not found"}), 404


    second_user = users_collection.find_one({
        'chats': id_chat,
        '_id': {'$ne': user['_id']}
    })

    if not second_user:
        second_user = {
            'username': 'Специальное',
            'email': 'special_email@special.ru',
            'avatar': 'special.png',
            'last_seen': 'never',
            'online': True
        }

    for i in chat['messages']:
        i['chatId'] = id_chat
        file_type = None
        if 'image' in i:
            file_type = 'image'
        elif 'video' in i:
            file_type = 'video'
        elif 'file' in i:
            file_type = 'file'
        if file_type:
            i[file_type] = i.get(file_type, None)

    response_data = {
        "messages": chat['messages'],
        "secondUser": {
            "name": second_user['username'],
            "avatar": f"https://julia.endless-summer.ru/api/get_image?filename={second_user['avatar']}",
            'last_seen': time_since_last_seen(second_user['last_seen'], second_user['online']),
            'email': second_user['email'],
        }
    }

    return jsonify(response_data), 200



@app.route('/api/filters', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def get_filters():
    filters = filters_collection.find()
    filters_list = []

    for filter in filters:
        filter['_id'] = str(filter['_id'])
        filters_list.append(filter)

    return jsonify(filters_list)

def get_plural_form(number, word):
    p = morph.parse(word)[0]
    return p.make_agree_with_number(number).word

def time_since_last_seen(last_seen,online):
    if online==True:
        return "В сети"
    now = datetime.now()
    try:
        last_seen_time = datetime.strptime(last_seen, "%Y-%m-%d %H:%M:%S")
    except:
        return "Был в сети (никогда)"
    diff = now - last_seen_time

    if diff < timedelta(minutes=1):
        return "Был в сети (только что)"
    elif diff < timedelta(hours=1):
        minutes = int(diff.total_seconds() / 60)
        minute_word = get_plural_form(minutes, 'минута')
        return f"Был в сети ({minutes} {minute_word} назад)"
    elif diff < timedelta(days=1):
        hours = int(diff.total_seconds() / 3600)
        hour_word = get_plural_form(hours, 'час')
        return f"Был в сети ({hours} {hour_word} назад)"
    elif diff < timedelta(days=7):
        days = diff.days
        day_word = get_plural_form(days, 'день')
        return f"Был в сети ({days} {day_word} назад)"
    else:
        weeks = int(diff.days / 7)
        week_word = get_plural_form(weeks, 'неделя')
        return f"Был в сети ({weeks} {week_word} назад)"

def get_current_datetime():

    now = datetime.now()

    formatted_datetime = now.strftime("%H:%M %d.%m.%Y")
    return formatted_datetime

ALLOWED_EXTENSIONS = {'*'}




@socketio.on('sendMessage')
def handle_send_message_event(data):

    username = data['user_name']
    timestamp = get_current_datetime()
    chat_id = data['chatId']
    query_params = request.args
    room = query_params.get('room')
    saved_files = []

    message = data.get('message', '')




    if 'image' in data:
        saved_files = data['image']
        file_type = 'image'
    elif 'video' in data:
        saved_files = data['video']
        file_type = 'video'
    elif 'file' in data:
        saved_files = data['file']
        file_type = 'file'
    else:
        saved_files = None
        file_type = None

    message_data = {
        "time": timestamp,
        "message": data.get('message', ''),
        "user_name": username,
    }

    if file_type:
        message_data[file_type] = saved_files


    chats_collection.update_one(
        {"id_chat": chat_id},
        {"$push": {"messages": message_data}}
    )

    second_user = users_collection.find_one({"chats": chat_id, "email": {"$ne": username}})
    socket_id = second_user['socket_id']



    emit('newMessage', {
        'message': message,
        'user_name': username,
        'time': timestamp,
        'files': saved_files,
        'chatId': chat_id
    }, room=socket_id)





@app.route("/api/authorization", methods=["POST"])
@cross_origin(origins=["*"], supports_credentials=True)
def authorization():
    data = request.get_json()
    if data['password'] == "" or data['email'] == "":
        return jsonify({"status": "error", "message": "Все поля должны быть заполнены"}), 400

    user = users_collection.find_one({"email": data['email']})

    if user and bcrypt.check_password_hash(user['password'], data['password']):
        user_info = {
            "username": user['username'],
            "email": user['email']
        }
        response = jsonify({"status": "ok", "user": user_info,'isAuth':True})
        token = generate_token(data['email'])
        response.set_cookie('auth_token', token, httponly=True, secure=True, samesite='None', max_age=timedelta(days=30))
        return response
    else:
        return jsonify({"status": "error", "message": "Неверное имя пользователя или пароль"}), 401




@app.route('/api/upload-file', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def upload_file():
    form_data = request.form

    chat_id = form_data.get('chatId')
    user_name = form_data.get('user_name')

    print(f'chatId: {chat_id}, user_name: {user_name}')

    file = request.files.get('file')

    if file is None or file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    link = request.host_url + 'api/get_image?filename=' + filename
    return jsonify({'message': 'File uploaded successfully', 'link': link})




@app.route("/api/registration", methods=["POST"])
@cross_origin(origins=["*"], supports_credentials=True)
def registration():
    data = request.get_json()
    user_search = users_collection.find_one({"email": data['email']})
    if user_search:
        return jsonify({"status": "Ошибка", "message": "Пользователь с таким email уже существует"}), 400
    if len(data['password']) < 8:
        return jsonify({"status": "Ошибка", "message": "Пароль минимум 8 символов"}), 400
    if data['password'] == "" or data['username'] == "" or data['email'] == "":
        return jsonify({"status": "Ошибка", "message": "Все поля должны быть заполнены"}), 400
    usertype = data.get('userType', 'user')
    if usertype=='employer':
        recruiter=True
    else:
        recruiter=False
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    data_for_record = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password,
        "chats":[
            "special"
        ],
        "avatar":"base.jpg",
        "last_seen":"never",
        "last_change_password":"Никогда",
        "job_search":"Не указан",
        "phone_number":"Не указан",
        "favorite_jobs":[],
        "responses":[],
        "recruiter":recruiter,
        "tests_for":[],
    }
    users_collection.insert_one(data_for_record)
    token = generate_token(data['email'])
    user_info = {
            "username": data['username'],
            "email": data['email']
        }
    response = jsonify({"status": "ok",'message': 'Вы успешно зарегистрировались','user': user_info,'isAuth':True})

    response.set_cookie('auth_token', token, httponly=True, secure=True, samesite='None', max_age=timedelta(days=30))
    return response, 200


@app.route("/api/get-favourites", methods=["GET"])
@cross_origin(origins=["*"], supports_credentials=True)
def get_favourites():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401


    user = users_collection.find_one({"email": email}, {'_id': 0, 'favorite_jobs': 1})
    if not user:
        return jsonify({"error": "User not found"}), 404

    favourites = user.get('favorite_jobs', [])

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    paginated_favourites = favourites[offset:offset + limit]

    response = []
    for job_id in paginated_favourites:
        info_job = jobs_collection.find_one({"_id": ObjectId(job_id)})
        if info_job:
            info_job['_id'] = str(info_job['_id'])
            response.append(info_job)
    pagination = {
        'page': page,
        'limit': limit,
        'total': len(favourites),
        'total_pages': (len(favourites) + limit - 1) // limit
    }
    full_response = {
        'status': 'ok',
        'favourites': response,
        'pagination': pagination
    }
    return jsonify(full_response)

@app.route("/api/check-auth", methods=["GET"])
@cross_origin(origins=["*"], supports_credentials=True)
def check_auth():
    token = request.cookies.get('auth_token')

    if not token:
        return jsonify({"status": "error", "message": "Токен отсутствует","isAuth":False}), 401
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])['email']
        token=generate_token(email)

        user = users_collection.find_one({"email": email})
        if not user:
            return jsonify({"status": "error", "message": "Пользователь не найден","isAuth":False}), 401
        user_info = {
            "username": user['username'],
            "email": user['email'],
            "recruiter":user['recruiter']
        }
        response = jsonify({"status": "ok", "message": "Токен валидный",'isAuth':True,'user': user_info})
        response.set_cookie('auth_token', token, httponly=True, secure=True, samesite='None', max_age=timedelta(days=30))
        return response
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Токен устарел","isAuth":False}), 401
    except jwt.InvalidSignatureError:
        return jsonify({"status": "error", "message": "Токен невалидный","isAuth":False}), 401


@app.route("/api/get-my-vacancies", methods=["GET"])
@cross_origin(origins=["*"], supports_credentials=True)
def get_my_vacancies():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    total_jobs = jobs_collection.count_documents({"email": email})
    jobs = list(jobs_collection.find({"email": email}).skip(offset).limit(limit))

    for i in jobs:
        i['_id'] = str(i['_id'])
    pagination = {
        'page': page,
        'limit': limit,
        'total': total_jobs,
        'total_pages': (total_jobs + limit - 1) // limit
    }
    full_response = {
        'status': 'ok',
        'jobs': jobs,
        'pagination':pagination,
    }

    return jsonify(full_response)


def build_query(data):
    query = {}

    if 'search' in data:
        query['$text'] = {'$search': data['search']}

    if 'salary' in data:
        query['$or'] = [
            {'salaryStart': {'$gte': data['salary']}},
            {'salaryEnd': {'$gte': data['salary']}}
        ]

    if 'experience' in data:
        query['experience'] = data['experience']

    if 'employmentType' in data:
        query['employmentType.value'] = data['employmentType']

    if 'schedule' in data:
        query['schedule.value'] = data['schedule']

    if 'subway' in data:
        query['companyInfo.subway.name'] = data['subway']

    if 'education' in data and data['education'] is not None:
        query['education.value'] = data['education']

    if 'periodSort' in data:
        period_sort = data['periodSort']
        if period_sort == 0:
            query['date'] = {"$gte": datetime.now() - timedelta(days=365*100)}
        else:
            query['date'] = {"$gte": datetime.now() - timedelta(days=period_sort)}

    return query

def build_sort(data):
    sort = []
    if 'salarySort' in data:
        if data['salarySort'] == 'relevance':
            sort.append(('score', {'$meta': 'textScore'}))
        elif data['salarySort'] == 'salary_desc':
            sort.append(('salaryStart', -1))
        elif data['salarySort'] == 'salary_ask':
            sort.append(('salaryStart', 1))

    if 'periodSort' in data:
        sort.append(('date', -1))

    return sort

@app.route('/api/catalog', methods=['GET', 'POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def handle_jobs():
    if request.method == 'POST':
        data = request.json
    else:
        data = request.args.to_dict()

    pagination = {
        'page': int(data.get('page', 1)),
        'limit': int(data.get('limit', 10)),
    }
    pagination['skip'] = (pagination['page'] - 1) * pagination['limit']

    query = build_query(data)
    sort = build_sort(data)

    if sort:
        jobs_cursor = jobs_collection.find(query).sort(sort).skip(pagination['skip']).limit(pagination['limit'])
    else:
        jobs_cursor = jobs_collection.find(query).skip(pagination['skip']).limit(pagination['limit'])

    jobs = list(jobs_cursor)

    for job in jobs:
        job['_id'] = str(job['_id'])

    total_count = jobs_collection.count_documents(query)
    pagination['total_count'] = total_count
    pagination['total_pages'] = (total_count + pagination['limit'] - 1) // pagination['limit']

    response = {
        'jobs': jobs,
        'pagination': pagination
    }

    return jsonify(response)

@app.route('/api/item', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def get_job():
    job_id = request.args.get('id')
    if not job_id:
        return jsonify({'error': 'Job ID is required'}), 400

    try:
        job = jobs_collection.find_one({'_id': ObjectId(job_id)})
        if not job:
            return jsonify({'error': 'Job not found'}), 404

        job['_id'] = str(job['_id'])
        return jsonify(job)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/hello_word", methods=["GET"])
def hello():
    return "Hello World!"







@app.route('/api/get_image', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def get_image():

    filename = request.args.get('filename')

    if not filename:
        abort(400, description="Filename query parameter is required")

    try:
        return send_from_directory('media', filename, as_attachment=False)
    except FileNotFoundError:
        abort(404, description="File not found")




def convert_datetime_format(datetime_str):

    _, date_str = datetime_str.split()

    day, month, _ = date_str.split('.')
    return f"{day}.{month}"


@app.route('/api/get-chats', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def get_chats():
    token = request.cookies.get('auth_token')

    if not token:
        return jsonify({"status": "error", "message": "Token is missing", "isAuth": False}), 401

    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = decoded_token['email']

        user = users_collection.find_one({'email': email})
        if not user:
            abort(404, description="User not found")
        chat_ids = user.get('chats', [])
        if not chat_ids:
            return jsonify([])

        response_data = []
        special_chat_info=chats_collection.find_one({'id_chat': 'special'})
        last_date = convert_datetime_format(special_chat_info['messages'][-1]['time'])
        chat_special={
            'chatId': 'special',
            'name': 'Специальное',
            'lastMessage': special_chat_info['messages'][-1]['message'],
            'lastDate': last_date,
            'avatar': 'https://julia.endless-summer.ru/api/get_image?filename=special.png'
        }
        response_data.append(chat_special)
        for chat_id in chat_ids:

            second_user = users_collection.find_one({
                'chats': chat_id,
                '_id': {'$ne': user['_id']}
            })
            if not second_user:
                continue

            chat = chats_collection.find_one({'id_chat': chat_id})
            if not chat:
                continue

            if not chat.get('messages'):
                chat_info = {
                    'chatId': str(chat_id),
                    'name': second_user['username'],
                    'lastMessage': 'Написать сообщение...',
                    'lastDate': '',
                    'avatar': f"https://julia.endless-summer.ru/api/get_image?filename={second_user['avatar']}"
                }
                response_data.append(chat_info)
                continue

            last_message_entry = chat['messages'][-1]
            try:
                last_message = last_message_entry['message']
                last_date = last_message_entry['time']
            except:
                last_message = 'Написать сообщение...'
                last_date = ''

            last_date = convert_datetime_format(last_date)

            file_type = None
            if 'image' in last_message_entry:
                file_type = 'image'
                last_message='Новое изображение'
            elif 'video' in last_message_entry:
                file_type = 'video'
                last_message='Новый видео файл'
            elif 'file' in last_message_entry:
                file_type = 'file'
                last_message='Новый файл'

            chat_info = {
                'chatId': str(chat_id),
                'name': second_user['username'],
                'lastMessage': last_message,
                'lastDate': last_date,
                'avatar': f"https://julia.endless-summer.ru/api/get_image?filename={second_user['avatar']}",
                'email': second_user['email']
            }

            if file_type:
                chat_info[file_type] = last_message_entry[file_type]
            response_data.append(chat_info)
        return jsonify(response_data)

    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidSignatureError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        abort(500, description=str(e))


@app.route('/api/delete-chat', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def delete_chat():
    token = request.cookies.get('auth_token')

    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    id_chat = request.json.get('chatId')
    if not id_chat:
        return jsonify({"error": "chatId parameter is required"}), 400

    chat = chats_collection.find_one({"id_chat": id_chat})
    if not chat:
        return jsonify({"error": "No chat found for this chat ID"}), 404

    user = users_collection.find_one({'email': email})
    if not user:
        return jsonify({"error": "User not found"}), 404

    second_user = users_collection.find_one({
        'chats': id_chat,
        '_id': {'$ne': user['_id']}
    })

    if not second_user:
        return jsonify({"error": "No second user found with the same chat ID"}), 404

    chats_collection.delete_one({'id_chat': id_chat})
    users_collection.update_one({'email': email}, {'$push': {'blocked': second_user['email']}})
    return jsonify({"status": "ok", "message": "Chat deleted successfully"})


CLIENT_ID = '170f5ed52d50480d9d8d1751089ecddd'
CLIENT_SECRET = 'a1463ab310d0416e8dd2a334351b2e7c'
REDIRECT_URI = 'http://localhost:5000/callback'

TOKEN_URL = 'https://oauth.yandex.ru/token'

USER_INFO_URL = 'https://login.yandex.ru/info'

TELEMOST_API_URL = 'https://cloud-api.yandex.net/v1/telemost-api/conferences'



def schedule_job(time_to_run, chat_id, user_email, nameMeeting, descriptionMeeting, full_datetime=False):
    schedule_collection.insert_one({
        "time_to_run": time_to_run,
        "chat_id": chat_id,
        "user_email": user_email,
        "nameMeeting": nameMeeting,
        "descriptionMeeting": descriptionMeeting
    })

    if full_datetime:
        schedule_specific_time(time_to_run, chat_id, user_email, nameMeeting, descriptionMeeting)
    else:
        schedule.every().day.at(time_to_run).do(send_meeting_link, chat_id, user_email, nameMeeting, descriptionMeeting)

def schedule_specific_time(time_to_run, chat_id, user_email, nameMeeting, descriptionMeeting):
    def job():
        send_meeting_link(chat_id, user_email, nameMeeting, descriptionMeeting)

    run_at = datetime.strptime(time_to_run, "%Y-%m-%d %H:%M:%S")
    delay = (run_at - datetime.now()).total_seconds()

    if delay > 0:
        threading.Timer(delay, job).start()
    else:
        print("Scheduled time is in the past. Cannot schedule the job.")

def send_meeting_link(chat_id, user_email, nameMeeting, descriptionMeeting):
    try:
        join_url = create_meeting(nameMeeting, descriptionMeeting)
        time_str = datetime.now().strftime("%H:%M %d.%m.%Y")
        message = {
            "time": time_str,
            "message": join_url,
            "user_name": user_email,
            "type": "conference"
        }


        users = users_collection.find({"chats": chat_id})

        for user in users:
            if user.get("online", False):
                socket_id = user.get("socket_id")
                username = user.get("username")
                if socket_id:
                    emit_new_message(socket_id, chat_id, message, user_email)

        chats_collection.update_one(
            {"id_chat": chat_id},
            {"$push": {"messages": message}}
        )
    except Exception as e:
        print(f"Ошибка отправки ссылки на встречу: {e}")

def emit_new_message(socket_id, chat_id, message, username):
    saved_files = []
    timestamp = datetime.now().strftime("%H:%M %d.%m.%Y")
    socketio.emit('newMessage', {
        'message': message['message'],
        'user_name': username,
        'time': timestamp,
        'files': saved_files,
        'chatId': chat_id,
        'type':'conference'
    }, room=socket_id)

def create_meeting(nameMeeting, descriptionMeeting):

    access_token = "y0_AgAEA7qklCQHAAvduwAAAAEGFYwcAAAxarZn1w9B6Jz-XgiN4Wb1OLUYoQ"
    headers = {
        'Authorization': f'OAuth {access_token}'
    }
    conference_data = {
        "access_level": "PUBLIC",
    }
    conference_response = requests.post(TELEMOST_API_URL, headers=headers, json=conference_data)
    conference_info = conference_response.json()
    if conference_response.status_code == 201:
        join_url = conference_info['join_url']
        return join_url
    else:
        raise Exception(f"Ошибка при создании конференции: {conference_info.get('message', 'Неизвестная ошибка')}")

@app.route('/api/create-meeting', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def schedule_meeting():
    data = request.json


    required_fields = ['title', 'description', 'startDate', 'startTime', 'chatId']
    missing_fields = [field for field in required_fields if field not in data['meetingData']]
    if missing_fields:
        return jsonify({"status": "Missing fields", "fields": missing_fields}), 400

    data = data['meetingData']
    nameMeeting = data['title']
    descriptionMeeting = data['description']
    startDate = data['startDate']
    startTime = data['startTime']
    chat_id = data['chatId']

    try:
        datetime.strptime(startTime, '%H:%M')
        time_to_run = startTime
    except ValueError:
        return jsonify({"status": "Invalid time format"}), 400

    full_datetime_str = f"{startDate} {startTime}:00"

    try:
        meeting_datetime = datetime.strptime(full_datetime_str, "%Y-%m-%d %H:%M:%S")
        if meeting_datetime < datetime.now():
            return jsonify({"status": "Meeting time is in the past"}), 400
    except ValueError:
        return jsonify({"status": "Invalid date format"}), 400

    token = request.cookies.get('auth_token')
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    user_email = decoded_token['email']

    schedule_job(full_datetime_str, chat_id, user_email, nameMeeting, descriptionMeeting, full_datetime=True)

    return jsonify({"status": "ok"}), 200


def run_schedule():
    while True:
        schedule.run_pending()
        eventlet.sleep(1)


threading.Thread(target=run_schedule).start()

def get_plural_form(number, word):
    if word == 'минута':
        if number % 10 == 1 and number % 100 != 11:
            return 'минута'
        elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
            return 'минуты'
        else:
            return 'минут'
    elif word == 'час':
        if number % 10 == 1 and number % 100 != 11:
            return 'час'
        elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
            return 'часа'
        else:
            return 'часов'
    elif word == 'день':
        if number % 10 == 1 and number % 100 != 11:
            return 'день'
        elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
            return 'дня'
        else:
            return 'дней'
    elif word == 'неделя':
        if number % 10 == 1 and number % 100 != 11:
            return 'неделя'
        elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
            return 'недели'
        else:
            return 'недель'
def time_since_last_password_change(last_change_password):
    now = datetime.now()

    try:
        last_change_time = datetime.strptime(last_change_password, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return "Пароль никогда не был изменен"

    diff = now - last_change_time

    if diff < timedelta(minutes=1):
        return "только что"
    elif diff < timedelta(hours=1):
        minutes = int(diff.total_seconds() / 60)
        minute_word = get_plural_form(minutes, 'минута')
        return f"{minutes} {minute_word} назад"
    elif diff < timedelta(days=1):
        hours = int(diff.total_seconds() / 3600)
        hour_word = get_plural_form(hours, 'час')
        return f"{hours} {hour_word} назад"
    elif diff < timedelta(days=7):
        days = diff.days
        day_word = get_plural_form(days, 'день')
        return f"{days} {day_word} назад"
    else:
        weeks = int(diff.days / 7)
        week_word = get_plural_form(weeks, 'неделя')
        return f"{weeks} {week_word} назад"

@app.route('/api/get-profile', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def get_profile():
    token = request.cookies.get('auth_token')
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    email = decoded_token['email']
    user = users_collection.find_one({'email': email},{'_id':0,'password':0,'chats':0,'online':0,'socket_id':0,'last_seen':0,'blocked':0})
    user['last_change_password'] = time_since_last_password_change(user['last_change_password'])
    user['avatar']=f'https://julia.endless-summer.ru/api/get_image?filename={user["avatar"]}'
    return jsonify(user)


def allowed_file(filename):
    return True

def update_user_info(email, updates):
    allowed_fields = {'username', 'email', 'new_password', 'old_password', 'job_search', 'phone_number'}

    update_data = {}

    if 'new_password' in updates and isinstance(updates['new_password'], dict):
        new_password_data = updates['new_password']
        if 'new_password' in new_password_data and 'old_password' in new_password_data:

            if len(new_password_data['new_password']) < 8:
                return False
            user = users_collection.find_one({'email': email})
            if user and bcrypt.check_password_hash(user['password'], new_password_data['old_password']):
                hashed_password = bcrypt.generate_password_hash(new_password_data['new_password']).decode('utf-8')
                update_data['password'] = hashed_password
                update_data['last_change_password'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            else:
                return False

    for field in updates:
        if field in allowed_fields and field not in {'new_password', 'old_password'}:
            update_data[field] = updates[field]

    if update_data:
        result = users_collection.update_one({'email': email}, {'$set': update_data})
        return result.matched_count > 0
    else:
        return False



def update_profile_avatar(email, file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        result = users_collection.update_one({'email': email}, {'$set': {'avatar': filename}})
        return filename
    return False

@app.route('/api/profile-update', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def profile_update():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    updates = request.json

    if not updates:
        return jsonify({'error': 'Invalid input'}), 400

    success = update_user_info(email, updates)

    if success:
        return jsonify({'status': 'ok'}), 200
    else:
        return jsonify({'status': 'error'}), 404



@app.route('/api/update-profile-avatar', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def profile_update_avatar():
    token = request.cookies.get('auth_token')
    if not token:
            return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401
    if 'avatar' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['avatar']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    success = update_profile_avatar(email, file)

    if success:
        url=f'https://julia.endless-summer.ru/api/get_image?filename={success}'
        return jsonify({'link':url,'status': 'ok'}), 200
    else:
        return jsonify({'status': 'error'}), 404


def get_filter_option_by_value(filter_id, value):

    filter_item = filters_collection.find_one({"id": filter_id})
    if filter_item:
        for option in filter_item['options']:
            if option['value'] == value:
                return option
    return None

@app.route('/api/create-vacancy', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def create_vacancie():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    data = request.form

    photo = request.files.get('logo')

    if photo:
        print("Photo filename:", photo.filename)
        print("Photo content type:", photo.content_type)

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        photo_url = "https://julia.endless-summer.ru/api/get_image?filename=" + photo.filename
    else:
        print("No photo file received")
        photo_url = "https://placekitten.com/199/55"

    educations_values = json.loads(data.get('educations', '[]'))
    type_of_employment_values = json.loads(data.get('typeOfEmployment', '[]'))
    work_schedule_values = json.loads(data.get('workSchedule', '[]'))

    education_options = [get_filter_option_by_value(3, value) for value in educations_values]
    education_options = [option for option in education_options if option is not None]
    experience_value = data.get('experience', '')
    experience_value=experience_value.replace('"', '')

    experience_option = get_filter_option_by_value(0, experience_value)
    experience_option=experience_option['name']

    employment_options = [get_filter_option_by_value(1, value) for value in type_of_employment_values]
    employment_options = [option for option in employment_options if option is not None]

    schedule_options = [get_filter_option_by_value(2, value) for value in work_schedule_values]
    schedule_options = [option for option in schedule_options if option is not None]

    id_test=data.get('id_test')

    vacancy = {
        "title": data.get('title'),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "salaryStart": int(data.get('salaryStart')),
        "salaryEnd": int(data.get('salaryEnd')),
        "salaryType": "between",
        "currencySymbol": "₽",
        "experience": experience_option if experience_option else None,
        "employmentType": employment_options[0] if employment_options else {"name": "Полная занятость", "value": "full-time"},
        "schedule": schedule_options,
        "companyInfo": {
            "name": data.get('name'),
            "logo": photo_url,
            "location": data.get('location'),
            "rating": 2.4,
            "subway": {
                "name": data.get('subway'),
                "color": "#D3D3D3"
            }
        },
        "description": data.get('description'),
        "education": education_options[0] if education_options else {"name": "Не требуется или не указано", "value": None},
        "email": email,
        "id_test": id_test
    }

    jobs_collection.insert_one(vacancy)
    return jsonify({'status': 'ok'}), 200


@app.route("/api/remove-favourite", methods=["POST"])
@cross_origin(origins=["*"], supports_credentials=True)
def remove_favourite():
    token = request.cookies.get("auth_token")
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email = payload["email"]
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    data = request.json

    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid input"}), 400
    if "vacancyId" not in data:
        return jsonify({"error": "vacancyId is required"}), 400

    vacancy_id = data["vacancyId"]

    try:
        result = users_collection.update_one({"email": email}, {"$pull": {"favorite_jobs": vacancy_id}})
        if result.modified_count == 0:
            return jsonify({"error": "Vacancy ID not found in user's favorites"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": "ok"}), 200


@app.route("/api/get-responses", methods=["GET"])
@cross_origin(origins=["*"], supports_credentials=True)
def get_responses():
    token = request.cookies.get("auth_token")
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email = payload["email"]
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    try:
        responses_data=users_collection.find_one({"email": email}, {"responses": 1, "_id": 0})
        for i in responses_data['responses']:
            i["name_vacancy"]=jobs_collection.find_one({"_id": i["vacancyId"]}, {"title": 1, "_id": 0})['title']
            i['_id']=str(i['_id'])



        return jsonify(responses_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/create-test', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def add_test():
    token=request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401
    if users_collection.find_one({'email':email},{'recruiter':1})['recruiter'] == False:
        return jsonify({"status": "error", "message": "Пользователь не рекрутер","isAuth":False}), 401
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    for test in data:
        if "dateCreated" in test:
            test["dateCreated"] = datetime.strptime(test["dateCreated"], "%d.%m.%y")
    data=data['test']
    data['creater']=email

    id=tests_colletion.insert_one(data).inserted_id

    return jsonify({"message": "Tests added successfully",'new_id': str(id)}), 201

@app.route('/api/get-tests', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def get_tests():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401
    if users_collection.find_one({'email':email},{'recruiter':1})['recruiter'] == False:
        return jsonify({"status": "error", "message": "Пользователь не рекрутер","isAuth":False}), 401
    tests = list(tests_colletion.find({'creater': email}))
    for i in tests:
        i['id']=str(i['_id'])
        i.pop('_id')
    tests_ids=users_collection.find_one({'email': email}, {'tests_for': 1, '_id': 0})
    if not tests_ids:
        return jsonify(tests)
    for i in tests_ids['tests_for']:
        data=tests_colletion.find_one({'_id': ObjectId(i)})
        data['id']=str(data['_id'])
        data.pop('_id')
        tests.append(data)
    return jsonify(tests)




@app.route('/api/update-test', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def edit_test():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    data = request.json


    if 'test' not in data or 'id' not in data['test']:
        return jsonify({"error": "Invalid data format"}), 400

    test_data = data['test']
    test_id = test_data['id']



    try:
        result = tests_colletion.update_one(
            {'_id': ObjectId(test_id)},
            {'$set': test_data}
        )
        if result.matched_count == 0:
            return jsonify({"error": "Test not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Test updated successfully"}), 200

@app.route('/api/delete-test/<test_id>', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def delete_test(test_id):
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    if not test_id:
        return jsonify({"error": "testId parameter is required"}), 400

    try:

        test = tests_colletion.find_one({'_id': ObjectId(test_id), 'creater': email})
        if test is None:
            return jsonify({"error": "Test not found or you are not authorized to delete this test"}), 404

        result = tests_colletion.delete_one({'_id': ObjectId(test_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Test not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Test deleted successfully"}), 200




@app.route('/api/get-result-test', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def get_result_test():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    data = request.json


    if 'test' not in data:
        return jsonify({"error": "Invalid data format"}), 400

    test_data = data['test']
    test_id = test_data.get('id')
    if not test_id:
        return jsonify({"error": "Test ID is required"}), 400



    total_questions = len(test_data['fields'])
    correct_answers = 0

    for answer in test_data['answers']:
        question = next((field for field in test_data['fields'] if field['id'] == answer['id']), None)
        if question:


            answer['value']=answer['value'].lower()
            if isinstance(answer['value'], list):
                answer_values = [str(val).lower() for val in answer['value']]
                question_values = [str(val).lower() for val in question['value']]
                print(answer_values, question_values)
                if set(answer_values) == set(question_values):
                    correct_answers += 1
            else:
                print(answer['value'], question['value'])
                if str(answer['value']).lower() == str(question['value']).lower():

                    correct_answers += 1

    passing_percentage = (correct_answers / total_questions) * 100
    passing_percentage_chat=passing_percentage

    test_result_data = {
        'testId': test_id,
        'userLogin': email,
        'passingPercentage': passing_percentage,
        'dateOfPassage': test_data['dateOfPassage'],
        'answers': test_data['answers']
    }
    test_result_collection.insert_one(test_result_data)

    all_results = test_result_collection.find({'testId': test_id})
    total_pass_percentage = passing_percentage
    count = 1

    for result in all_results:
        total_pass_percentage += result['passingPercentage']
        count += 1

    average_passing_percentage = total_pass_percentage / count
    average_passing_percentage = round(average_passing_percentage, 2)

    tests_colletion.update_one(
        {'_id': ObjectId(test_id)},
        {'$set': {'passingPercentage': average_passing_percentage}}
    )

    users_collection.update_one(
        {'email': email},{"$pull":{
            "tests_for":test_id
        }
        }
    )


    chat_id=chats_collection.insert_one({
        "id_chat":'',
        "messages":[
            {"user_name":email, "message": f"Тест пройден. Средний процент прохождения: {passing_percentage_chat.__round__(2)}%",'time':datetime.now().strftime('%H:%M %d.%m.%Y')},
        ]
    }).inserted_id

    chats_collection.update_one(
        {'_id': chat_id},
        {'$set': {'id_chat': str(chat_id)}}
    )

    users_collection.update_one(
        {'email': email},
        {'$push': {'chats': str(chat_id)}}
    )
    creater_email=tests_colletion.find_one({'_id':ObjectId(test_id)},{'creater':1})['creater']
    users_collection.update_one(
        {'email': creater_email},
        {'$push': {'chats': str(chat_id)}}
    )

    return jsonify({"message": "Test result saved successfully","chat_id":str(chat_id)}), 200


@app.route('/api/negotiations', methods=['GET'])
@cross_origin(origins=["*"], supports_credentials=True)
def negotiations():
    token=request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    data=users_collection.find_one({'email':email},{'_id':0,"responses":1})
    return jsonify(data)

@app.route('/api/respond', methods=['POST'])
@cross_origin(origins=["*"], supports_credentials=True)
def respond():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "auth_token is missing"}), 401

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"status": "error", "message": "Token has expired", "isAuth": False}), 401
    except jwt.InvalidTokenError:
        return jsonify({"status": "error", "message": "Invalid token", "isAuth": False}), 401

    data = request.json
    catalog_info=jobs_collection.find_one({'_id':ObjectId(data['id'])})
    date_today = datetime.now()
    date_today_to_str = date_today.strftime("%d %B %Y")
    data_for_ansers={
        'id':data['id'],
        'name':catalog_info['title'],
        'status':"Резюме не просмотрено",
        'date':date_today_to_str,
    }
    users_collection.update_one({'email': email}, {'$push': {'responses': data_for_ansers}})

    users_collection.update_one(
    {'email': email, 'tests_for': {'$exists': False}},
    {'$set': {'tests_for': []}}
)
    users_collection.update_one(
        {'email': email},
        {'$push': {'tests_for': catalog_info['id_test']}}
    )


    return jsonify({"status": "ok", "message": "Ответ сохранен","id_test":catalog_info['id_test']})




if __name__ == "__main__":
    eventlet.monkey_patch()
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()
    app.run(debug=True, port=2665)