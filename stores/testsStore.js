import {defineStore} from "pinia";
import commonScripts from "~/helpers/commonScripts.js";
import api from "~/http/api.js";
import {toast} from "vue3-toastify";

export const useTestsStore = defineStore('testsStore', {
    state: () => ({
        tests: [],
    }),

    persist: {
        storage: persistedState.localStorage,
    },

    actions: {
        getTests() {
            api.get('get-tests').then((data) => {
                this.tests = data
            })
        },

        createTest(test) {
            test.answers = []
            test.fields.forEach(field => {
                test.answers.push({
                    id: field.id,
                    noAnswer: field.isNoAnswer,
                    value: field.value
                })
            })

            api.post('create-test', {
                test
            }).then((data) => {
                test.id = data.new_id
                this.tests.push(test)
            })
        },

        getTest(id) {
            return this.tests.find(test => test.id === id)
        },

        updateTest(test) {
            let currentTest = this.getTest(test.id)

            api.post('update-test', {
                test
            }).then(() => {
                currentTest.name = test.name
                currentTest.fields = test.fields
                currentTest.questions = test.fields.length
            })
        },

        deleteTest(id) {
            api.get(`delete-test/${id}`).then(() => {
                this.tests = this.tests.filter(test => test.id !== id)
            })
        },

        checkAnswers(test) {
            const checkedAnswers = {}

            test.fields.forEach(field => {
                if (!field.isNoAnswer) {
                    const currentAnswer = test.answers.find(answer => answer.id === field.id)

                    if (field.type === 'checkbox' || field.type === 'radio') {
                        checkedAnswers[field.id] = commonScripts.compareArrays(currentAnswer.value, field.value)
                    } else {
                        checkedAnswers[field.id] = field === currentAnswer
                    }
                } else {
                    checkedAnswers[field.id] = true
                }
            })

            return checkedAnswers
        },

        async saveAnswers(test, answers, userLogin) {
            const cloneTest = JSON.parse(JSON.stringify(test))

            cloneTest.passingPercentage = Math.round((Object.values(answers).filter(el => el).length / cloneTest.fields.length) * 100)
            cloneTest.userLogin = userLogin
            cloneTest.dateOfPassage = commonScripts.formatDate(new Date())

            return await api.post('get-result-test', {
                test: cloneTest
            });
        }
    }
})