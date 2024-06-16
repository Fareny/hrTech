<template>
    <header class="header">
        <AppSection class="section_center">
            <section class="header__content">
                <div class="header__content-navigation navigation">
                    <NuxtLink to="/" class="navigation__logo">
                        <img src="" class="navigation__logo-image" alt="logo">
                        <h1 class="navigation__logo-title">Global Solutions</h1>
                    </NuxtLink>

                    <div
                        v-if="props.isAuth"
                        class="navigation__links navigation-links"
                    >   
                        <NuxtLink v-if="userStore.recruiter" to="/my-vacancies" class="navigation-links__item">Мои вакансии</NuxtLink>
                        <NuxtLink v-if="userStore.recruiter" to="/profile/tests" class="navigation-links__item">Тесты</NuxtLink>
                        <NuxtLink v-if="!userStore.recruiter" to="/resume" class="navigation-links__item">Мое резюме</NuxtLink>
                        <NuxtLink v-if="!userStore.recruiter" to="/negotiations" class="navigation-links__item">Отклики</NuxtLink>
                        <NuxtLink v-if="!userStore.recruiter" to="/" class="navigation-links__item">Помощь</NuxtLink>
                    </div>
                </div>

                <div class="header__content-actions content-actions">
                    <div
                        v-if="props.isAuth"
                        class="content-actions__wrapper"
                    >
                        <NuxtLink to="/chats" class="content-actions__item">
                            <MessageIcon />
                        </NuxtLink>
                        <NuxtLink to="/favourites" class="content-actions__item">
                            <HeartIcon />
                        </NuxtLink>
                        <div class="content-action__notifications">
                            <AppDetails>
                                <template #summary>
                                    <div class="content-actions__item">
                                        <NotificationIcon @click="openNotifications = !openNotifications" />
                                        <div v-if="notificationStore.notifications.length > 0" class="content-actions__dot"></div>
                                    </div>
                                </template>

                                <template #content> 
                                    <template v-if="notificationStore.notifications.length > 0">
                                        <DetailsItem
                                            v-for="notification in notificationStore.notifications"
                                            :key="notification.id"
                                            :notification="notification"
                                        >
                                            <span>
                                                <p class="notification-item__title">{{ notification.title }}</p>
                                                <NuxtLink
                                                    v-if="notification.message"
                                                    :to="notification.link"
                                                    class="notification-item__message"
                                                >
                                                    {{ notification.message }}
                                                </NuxtLink>
                                            </span>    
                                            
                                        </DetailsItem>
                                    </template>

                                    <template v-else>
                                        <DetailsItem
                                            :noClickable="true"
                                        >
                                            У вас нет уведомлений
                                        </DetailsItem>
                                    </template>
                                </template>
                            </AppDetails>
                        </div>
                        <NuxtLink to="/profile" class="content-actions__item">
                            <UserIcon />
                        </NuxtLink>
                    </div>
                    <div
                        v-if="!props.isAuth"
                        class="content-actions__wrapper content-actions__wrapper_no-auth"
                    >
                        <AppButton class="button_clear">
                            <NuxtLink to="/registration" class="content-actions__item">Регистрация</NuxtLink>
                        </AppButton>
                        <AppButton>
                            <NuxtLink to="/authorization" class="content-actions__item">Войти</NuxtLink>
                        </AppButton>
                    </div>
                </div>
            </section>

            <HeaderHome v-if="!props.isAuth"/>
        </AppSection>
    </header>
</template>

<script setup>
    import './HeaderComponents.scss'

    import MessageIcon from '~/components/AppIcons/Message.vue';
    import HeartIcon from '~/components/AppIcons/Heart.vue';
    import NotificationIcon from '~/components/AppIcons/Notification.vue';
    import UserIcon from '~/components/AppIcons/User.vue';

    import AppSection from "~/components/AppSection/AppSection.vue";
    import HeaderHome from "~/components/HeaderComponents/HeaderHome/HeaderHome.vue";
    import AppDetails from '~/components/AppDetails/AppDetails.vue';
    import DetailsItem from '~/components/AppDetails/DetailsItem/DetailsItem.vue';
    import { useNotificationStore } from '~/stores/notificationStore';
    import { ref } from 'vue';

    const openNotifications = ref(false);
    const userStore = useUserStore();
    
    const notificationStore = useNotificationStore();

    const props = defineProps({
        isAuth: {
            default: false,
            type: Boolean
        }
    })
    
</script>
