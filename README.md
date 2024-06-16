Hr'rtech Документация
Установка
Убедитесь, что установлены зависимости:

bash
Копировать код
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
Сервер разработки
Запустите сервер разработки на http://localhost:3000:

bash
Копировать код
# npm
npm run dev

# pnpm
pnpm run dev

# yarn
yarn dev

# bun
bun run dev
Продакшн
Соберите приложение для продакшн:

bash
Копировать код
# npm
npm run build

# pnpm
pnpm run build

# yarn
yarn build

# bun
bun run build
Локально просмотрите сборку продакшн:

bash
Копировать код
# npm
npm run preview

# pnpm
pnpm run preview

# yarn
yarn preview

# bun
bun run preview
Ознакомьтесь с документацией по деплою для получения дополнительной информации.

# Инструкция по установке и запуску Flask приложения с Gunicorn

## Установка необходимых пакетов

Создайте файл `requirements.txt` со следующими зависимостями:

```plaintext
Flask
pymongo
flask-cors
icecream
Flask-Bcrypt
pyjwt
flask-socketio
eventlet
pymorphy2
requests
schedule
gunicorn
```

Установите все необходимые пакеты с помощью `pip`:

```bash
pip install -r requirements.txt
```




## Запуск сервера с Gunicorn

Используйте следующую команду для запуска сервера с Gunicorn:

```bash
gunicorn -k eventlet -w 1 -b 0.0.0.0:2665 app:app
```

## Настройка Gunicorn конфигурации

Создайте файл конфигурации Gunicorn, например `gunicorn_config.py`, с содержимым:

```python
bind = '0.0.0.0:2665'
workers = 1
worker_class = 'eventlet'
```

Теперь вы можете запускать Gunicorn с использованием конфигурационного файла:

```bash
gunicorn -c gunicorn_config.py app:app
```



