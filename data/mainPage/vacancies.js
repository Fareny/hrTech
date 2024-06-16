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
        companyInfo: {
            name: 'ООО Черти Ярославля',
            logo: 'https://img.hhcdn.ru/employer-logo/3133061.png',
            location: 'Москва',
            subway: {
                name: 'Серпуховская',
                color: '#D3D3D3'
            }
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
        companyInfo: {
            name: 'test',
            logo: null,
            location: 'test',
            subway: null
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
        companyInfo: {
            name: 'test',
            logo: null,
            location: 'test',
            subway: null
        }
    }
]