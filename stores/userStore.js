import { defineStore } from 'pinia'

export const useUserStore = defineStore('userStore', {
    state: () => ({
        isAuth: false,
        userName: '',
        email: '',
        recruiter: false
    }),

    persist: {
        storage: persistedState.localStorage,
    },

    actions: {
        setAuthInfo(status, email, userName, recruiter) {
            this.isAuth = status;
            this.userName = userName;
            this.email = email;
            this.recruiter = recruiter;
        }
    }
})
