export default [
    // Зарплата Между
    {
        id: 0,
        title: 'Frontend-разработчик',
        date: 'test',
        salary: null,
        salaryStart: 100000,
        salaryEnd: 200000,
        salaryType: 'between',
        currencySymbol: '₽',
        experience: '1-3 года',
        employmentType: {
            name: 'Полная занятость',
            value: 'full-time'
        },
        schedule: {
            name: 'Гибкий график',
            value: 'flexible'
        },
        companyInfo: {
            name: 'ООО Черти Ярославля',
            logo: 'https://img.hhcdn.ru/employer-logo/3133061.png',
            location: 'Москва',
            rating: 4.9,
            subway: {
                name: 'Серпуховская',
                color: '#D3D3D3'
            }
        },
        description: `<p><strong><span>Тендертех </span></strong><span>- аккредитованная IT финтех компания, предоставляющая банковские гарантии, кредиты и страхование финансовых услуг участникам госзакупок. Участник Сколково.</span></p> <p><span>Мы делаем процесс получения банковских продуктов для малого и среднего бизнеса простым, понятным и быстрым.</span></p> <p><strong><span>Тендертех в цифрах:</span></strong></p> <ul> <li><span>11 крупных банков-партнеров</span></li> <li><span>2 000+ партнеров</span></li> <li><span>50+ тысяч клиентов</span></li> <li><span>200+ миллиардов рублей выданных финансовых продуктов</span></li> </ul> <p><strong><span>Стек разработки: </span></strong><span>Vue.js + Nuxt + Typescript</span></p> <p><em><span>Хочешь работать, а </span><strong><span>в будущем возглавлять</span></strong><span> крутую команду фронтенда, где уделяют должное внимание передаче знаний младшим, code-review, рефакторингу и бест-практисам в целом? Это к нам!</span></em></p> <p><strong><span>Чем предстоит заниматься:</span></strong></p> <ul> <li> <p><span>(неожиданно) Писать код;</span></p> </li> <li> <p><span>Кроссбраузерная верстка пользовательских интерфейсов по макетам (макеты в Figma);</span></p> </li> <li><span>Участвовать в code review;</span></li> <li><span>Участвовать в планировании спринтов и в формировании способов достижения бизнес-целей команды - каждое мнение важно!</span></li> <li><span>Конструктивное тыканье пальцами в коллег вместе с объективной критикой :)</span></li> </ul> <p><strong><span>О тебе:</span></strong></p> <ul> <li><span>Пишешь вменяемый код, не заставляющий остальных разработчиков разбивать себе лоб рукой;</span></li> <li><span>Уверенное знание Javascript, Vue.js, Typescript;</span></li> <li><span>Умение работать с Docker/Docker-compose;</span></li> <li><span>Понимание KISS, DRY, SOLID;</span></li> <li><span>Опыт работы с Nuxt;</span></li> <li><span>Умеешь разбираться в чужом коде и тебе не страшно этим заниматься;</span></li> <li><span>Имеешь опыт менторства;</span></li> <li><span>Пробовал себя в качестве тимлида и не испугался</span></li> </ul> <p><strong><span>Работая в Тендертех ты получаешь:</span></strong></p> <ul> <li><span>Реализацию опыта и возможность влиять и создавать новые продукты в области финтех</span></li> <li><span>Стабильный и прозрачный доход, обсудим на интервью</span></li> </ul> <p><strong><span>Условия:</span></strong></p> <ul> <li><span>Оформление по ТК РФ с первого дня</span></li> <li><span>График работы пн-пт с 9 до 18 или с 10 до 19, с учетом обеденного перерыва</span></li> <li><span>Возможность гибридного графика работы (офис, удаленно после испытательного срока)</span></li> <li><span>Работа в комфортном офисе рядом с м. Добрынинская.</span></li> <li><span>Своя кухня со всем необходимым: чай, кофе, печенье, фрукты, микроволновая печь, холодильник. Рядом много кафе, ресторанов и столовых, Вкусвилл и Азбука вкуса в 5 минутах от двери до двери</span></li> <li><span>Каждую пятницу в офисе обеды за счет компании</span></li> <li><span>Лояльное и адекватное руководство</span></li> <li><span>Ежегодный оплачиваемый отпуск 28 календарных дней</span></li> <li><span>Сокращенные на 1 час пятницы в летний период</span></li> <li><span>Зарплатный проект АО "АЛЬФА-БАНК"</span></li> </ul>`,
        education: {
            name: 'Не требуется или не указано',
            value: null
        }
    },
    // Зарплата ОТ
    {
        id: 1,
        title: 'Frontend-разработчик',
        date: 'test',
        salary: 100000,
        salaryType: 'of',
        currencySymbol: '₽',
        experience: null,
        employmentType: {
            name: 'Полная занятость',
            value: 'full-time'
        },
        schedule: {
            name: 'Гибкий график',
            value: 'flexible'
        },
        companyInfo: {
            name: 'test',
            logo: null,
            location: 'test',
            rating: 4.9,
            subway: null
        },
        description: `Hello world, <br><b>motherfucker!</b>`,
        education: {
            name: 'Не требуется или не указано',
            value: null
        }
    },
    // Зарплата ДО
    {
        id: 2,
        title: 'Frontend-разработчик',
        date: 'test',
        salary: 100000,
        salaryType: 'to',
        currencySymbol: '₽',
        experience: '3-6 лет',
        employmentType: {
            name: 'Полная занятость',
            value: 'full-time'
        },
        schedule: {
            name: 'Гибкий график',
            value: 'flexible'
        },
        companyInfo: {
            name: 'test',
            logo: null,
            location: 'test',
            rating: 4.9,
            subway: null
        },
        description: `Hello world, <br><b>motherfucker</b>`,
        education: {
            name: 'Не требуется или не указано',
            value: null
        }
    }
]