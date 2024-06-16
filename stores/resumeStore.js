import { defineStore } from 'pinia'
import commonScripts from "~/helpers/commonScripts.js";

export const useResumeStore = defineStore('resumeStore', {
    state: () => ({
        personalInfo: {
            aboutMe: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In purus urna, lacinia quis convallis at, dapibus vel lorem. Vestibulum accumsan turpis et mattis pulvinar. Donec ut nibh eget ex auctor egestas non eget ligula. Praesent eleifend commodo sem, et tempus velit viverra in. Quisque in tincidunt erat, auctor porttitor lectus. Donec consequat ultrices lorem, id eleifend sem laoreet eu. Mauris ut justo lectus. Morbi non condimentum magna, vitae vehicula erat. Nulla ut imperdiet nulla, ut sodales sem. Proin dapibus, libero in imperdiet luctus, neque mi condimentum diam, ut elementum nisl lectus nec ante. Vestibulum feugiat sit amet augue in tempus. In commodo mi ut turpis aliquam, eget dictum elit sagittis. Nullam efficitur ac quam nec lobortis. Nulla dictum tristique sapien. Donec varius dapibus magna, vitae consequat quam sagittis et.\n' +
                '\n' +
                'In tristique elit sit amet viverra ornare. Mauris posuere mollis orci vel feugiat. Vivamus molestie dapibus odio nec lacinia. Integer bibendum orci vitae ligula lacinia volutpat. Proin nunc urna, pharetra in imperdiet a, laoreet eget lacus. Vestibulum sapien est, luctus id dolor vitae, mollis fringilla libero. Proin faucibus consectetur metus quis elementum. Donec vitae ipsum mollis, fermentum nulla nec, ultrices elit.',
            contacts: {
                phone: '+7 (915) 005-33-99',
                tellegram: '@MishaFilimon',
                email: 'filimon.michail255@gmail.com'
            },
            skills: {
                id: 0,
                value: null,
                options: [
                    {
                        label: 'BEM',
                        value: 1
                    },
                    {
                        label: 'CSS3',
                        value: 2
                    },
                    {
                        label: 'Webpack',
                        value: 3
                    },
                    {
                        label: 'SASS',
                        value: 4
                    },
                    {
                        label: 'HTML5',
                        value: 5
                    },
                    {
                        label: 'JavaScript',
                        value: 6
                    },
                    {
                        label: 'React',
                        value: 7
                    },
                    {
                        label: 'Vue',
                        value: 8
                    },
                    {
                        label: 'Angular',
                        value: 9
                    },
                    {
                        label: 'Git',
                        value: 10
                    },
                    {
                        label: 'GitHub',
                        value: 11
                    },
                    {
                        label: 'NPM',
                        value: 12
                    },
                    {
                        label: 'Gulp',
                        value: 13
                    },
                    {
                        label: 'Selenium',
                        value: 14
                    },
                    {
                        label: 'Cypress',
                        value: 15
                    },
                    {
                        label: 'Jest',
                        value: 16
                    },
                    {
                        label: 'Jasmine',
                        value: 17
                    },
                    {
                        label: 'Master of the Gym',
                        value: 18
                    },
                    {
                        label: 'Сumуникация',
                        value: 19
                    },
                    {
                        label: 'Работал сварщиком',
                        value: 20
                    },
                    {
                        label: 'Ебашил биты под 3 дня дождя',
                        value: 21
                    }
                ]
            },
        },
        resumeInfo: {
            name: 'Frontend Разработчик',
            sallary: 52000,
            currencySymbol: '₽',
            categories: {
                id: 10,
                value: ['frontend', 'backend', 'fullstack', 'data-scientist']
            },
            conditions: [
                {
                    id: 1,
                    name: 'Тип занятости',
                    value: ['full-time', 'part-time'],
                    options: [
                        {
                            label: 'Полная занятость',
                            value: 'full-time'
                        },
                        {
                            label: 'Частичная занятость',
                            value: 'part-time'
                        },
                        {
                            label: 'Проектная работа',
                            value: 'project'
                        },
                        {
                            label: 'Волонтерство',
                            value: 'volunteering'
                        },
                        {
                            label: 'Стажировка',
                            value: 'trainee'
                        }
                    ]
                },
                {
                    id: 2,
                    name: 'График работы',
                    value: ['full-day', 'remote'],
                    options: [
                        {
                            label: 'Полный день',
                            value: 'full-day'
                        },
                        {
                            label: 'Гибкий график',
                            value: 'flexible'
                        },
                        {
                            label: 'Удаленная работа',
                            value: 'remote'
                        },
                        {
                            label: 'Сменный график',
                            value: 'shift'
                        },
                        {
                            label: 'Вахтовый метод',
                            value: 'wfh'
                        }
                    ]
                }
            ],
            experience: [
                {
                    id: 0,
                    positionName: 'Программист',
                    companyInfo: {
                        name: "ООО Черти Ярославля",
                        logo: "https://img.hhcdn.ru/employer-logo/3133061.png",
                        location: "Москва",
                        rating: 4.9,
                        subway: {
                            name: "Серпуховская",
                            color: "#D3D3D3"
                        }
                    },
                    timeStart: {
                        month: 2,
                        year: 2023
                    },
                    timeEnd: {
                        month: 1,
                        year: 2024
                    },
                    validateTime: true,
                    responsibility: `Тесто`
                }
            ],
        }
    }),

    actions: {
        countMonth(timeStart, timeEnd) {
            return commonScripts.differenceNumber(timeStart.year, timeEnd.year) * 12 + timeStart.month + timeEnd.month - 1
        },

        getNewWorkPlace() {
            const maxId = Math.max([...this.resumeInfo.experience.map(item => item.id)]) + 1

            return {
                id: maxId,
                positionName: '',
                companyInfo: {
                    name: "",
                    logo: null,
                    location: "",
                    rating: 4.9,
                    subway: null,
                    site: ''
                },
                timeStart: {
                    month: 2,
                    year: 2023
                },
                timeEnd: {
                    month: 1,
                    year: 2024,
                    now: false
                },
                validateTime: true,
                responsibility: ''
            }
        },

        getExperienceById(id) {
            return this.resumeInfo.experience.find(item => item.id === id)
        },

        getExperinceTime(totalMonth) {
            return `
                ${Math.floor(totalMonth / 12)} ${commonScripts.getNounYear(Math.floor(totalMonth / 12))} 
                ${totalMonth % 12} ${commonScripts.getNounMonth(totalMonth % 12)}
            `
        }
    }
})
