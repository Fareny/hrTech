<template>
    <client-only>
        <HeaderComponents
            v-show="!isAuthPage"
            :isAuth="userStore.isAuth"
        />
    </client-only>

    <main class="main wrapper">
        <NuxtPage />
    </main>

    <FooterComponents />
</template>

<script setup>
    import './assets/default.scss';
    import { checkAuth } from '~/http/http.js';
    import { useUserStore } from '~/stores/userStore';
    import { useNotificationStore } from '~/stores/notificationStore';
    import HeaderComponents from "~/components/HeaderComponents/HeaderComponents.vue";
    import FooterComponents from "~/components/FooterComponents/FooterComponents.vue";
    import socketService from '~/helpers/mainSocketConnection';
    import { computed, onUnmounted, onMounted, ref } from 'vue';

    const userStore = useUserStore();
    const notificationStore = useNotificationStore();
    const route = useRoute();
    const isConnected = ref(false);

    const isAuthPage = computed(() => {
        return route.path === '/authorization' || route.path === '/registration';
    });

    const registerSocketEvents = () => {
        if (isConnected.value) {
            socketService.onEvent('notifications', (info) => {
                notificationStore.setNotifications(info.notifications);
            });
        }
    };

    const checkToken = async () => {
        try {
            const check = await checkAuth();
            
            if(check.isAuth) {
                userStore.setAuthInfo(
                    check.isAuth,
                    check.user.email,
                    check.user.username,
                    check.user.recruiter
                );
            }

            if (check.isAuth) {
                await socketService.connect('wss://julia.endless-summer.ru');
                isConnected.value = true;
                registerSocketEvents();
                socketService.sendEvent('get-notifications', {});
            } else {
                navigateTo('/authorization');
            }

        } catch (error) {
            console.log(error);
        }
    };

    onMounted(() => {
        checkToken();
    });

    onUnmounted(() => {
        socketService.disconnect();
        isConnected.value = false;
    });
</script>
