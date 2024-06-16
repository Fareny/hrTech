import { defineStore } from 'pinia'
import api from "~/http/api.js";

export const useVacancyStore = defineStore('vacancyStore', {
    state: () => ({
        vacancies: [],
        pagination: {},
        filters: [],
        searchValue: '',
        sortItems: []
    }),

    actions: {
        // Действия с Вакансиями

        getVacancies(params = {}) {
            api.get('catalog', params).then((data) => {
                this.vacancies = data.jobs
                this.pagination = data.pagination
            })
            // return getVacancies(this.filters, this.searchValue, this)
        },

        loadVacancies() {
            this.pagination.page += 1
            api.get('catalog', { page: this.pagination.page }).then((data) => {
                this.vacancies.push(...data.jobs)
            })
        },

        getVacanciesBySearch(searchValue) {
            // getVacancies(filters, this.searchValue, this)
        },

        getVacanciesByFilters(filters) {
            // getVacancies(filters, this.searchValue, this)
        },

        changeVacancyPage(page) {
            this.getVacancies(this.pagination)
        },

        async getVacancyById(id) {
            return api.get('item', { id }).then((data) => {
                return data
            })
        },

        getVacancySalary(vacancy) {
            return vacancy.salaryType === 'between' ?
                `${vacancy.salaryStart} - ${vacancy.salaryEnd} ${vacancy.currencySymbol}` :
                `${vacancy.salary} ${vacancy.currencySymbol}`
        },

        // Действия с фильтрами

        getFilters() {
            api.get('filters').then((data) => {
                this.filters = data
            })
        }
    }
})
