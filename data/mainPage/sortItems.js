export default [
    {
        key: 'salary',
        items: [
            {
                name: 'По соответствию',
                value: 'relevance',
                // active будет добавляться при получении данных от сервера
                active: true
            },
            {
                name: 'По дате',
                value: 'publication_time',
                active: false
            },
            {
                name: 'По убыванию зарплат',
                value: 'salary_desc',
                active: false
            },
            {
                name: 'По возрастанию зарплат',
                value: 'salary_ask',
                active: false
            },
        ]
    },
    {
        key: 'period',
        items: [
            {
                name: 'За все время',
                value: 0,
                // active будет добавляться при получении данных от сервера
                active: true
            },
            {
                name: 'За месяц',
                value: 30,
                active: false
            },
            {
                name: 'За неделю',
                value: 7,
                active: false
            },
            {
                name: 'За последние 3 дня',
                value: 3,
                active: false
            },
            {
                name: 'За сутки',
                value: 1,
                active: false
            }
        ]
    }
]