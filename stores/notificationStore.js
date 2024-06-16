import { defineStore } from 'pinia'

export const useNotificationStore = defineStore('notificationStore', {
    state: () => ({
        notifications: [],
    }),

    actions: {
        setNotifications(notifications) {
            this.notifications = notifications;
        }
    }
})
