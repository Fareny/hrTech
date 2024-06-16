<template>
        <section class="auth">
            <div class="auth__container">
                
                <form class="auth__form" @submit.prevent="handleSubmit">
                    <h2 class="auth__title">Авторизация</h2>

                    <fieldset class="auth__inputs">
                        <AppInput
                            class="auth__input"
                            id="email"
                            :value="credentials.email"
                            type="text"
                            placeholder="Введите ваш email"
                            @changeValue="(val) => credentials.email = val.value"
                        />

                        <ErrorCircleIcon v-if="!credentials.password && touched" class="auth__input-icon" />
                    </fieldset>

                    <fieldset class="auth__inputs" >
                        <AppInput
                            class="auth__input"
                            id="password"
                            :value="credentials.password"
                            type="password"
                            placeholder="Введите ваш пароль"
                            @changeValue="(val) => credentials.password = val.value"
                        />

                        <ErrorCircleIcon v-if="!credentials.password && touched" class="auth__input-icon" />
                    </fieldset>

                    <fieldset class="auth__checkbox auth-checkbox auth-remeber">
                        <AppCheckbox
                            class="auth-checkbox__item"
                            type="checkbox"
                            :checked="rememberMe"
                            @changeValue="(val) => rememberMe = val.value"
                        >
                            <span class="auth__checkbox-text">Запомнить меня</span>
                        </AppCheckbox>

                        <p class="auth__forgot">Забыли пароль?</p>
                    </fieldset>

                    <AppButton
                        class="auth__form-button"
                        :disabled="loading"
                    >
                        <template v-if="loading">
                            <Loader class="reg__form__loading-icon" />
                        </template>
                        <template v-else>
                            Войти
                        </template>
                    </AppButton>

                    <NuxtLink class="auth__form-link" to="/registration">Нет аккаунта? Зарегистрироваться</NuxtLink>
                </form>

                <div class="auth__info auth-info">
                    <div class="auth-info__container">
                        <img src="~/assets/svg/addUser.svg" alt="">
                    </div>
                    <div>
                        <h3 class="auth-info__title">Привет, друг!</h3>
                        <p class="auth-info__text">Введите свои личные данные и отправляйтесь в путешествие вместе с нами</p>
                    </div>

                    <NuxtLink class="auth-info__button" to="/registration">
                        <span class="auth-info__button-text">Регистрация</span>
                        <img class="auth-info__button-arrow" src="~/assets/svg/arrow.svg" alt="">
                    </NuxtLink>
                </div>
            </div>
        </section>
</template>

<script setup>
    import './AuthComponents.scss'
    import { ref } from 'vue'
    import { login } from '~/http/http.js'
    import ErrorCircleIcon from "~/components/AppIcons/ErrorCircle.vue";
    import Loader from "~/components/AppIcons/Loader.vue";
    import AppInput from '~/components/AppInputs/Input/Input.vue'
    import AppCheckbox from "~/components/AppInputs/Checkbox/Checkbox.vue"
    import { toast } from 'vue3-toastify';

    const touched = ref(false);
    const userStore = useUserStore();
    const loading = ref(false);

    const rememberEmail = ref(localStorage.getItem('rememberMe') || '');

    const rememberMe = ref(rememberEmail.value ? true : false);

    const credentials = ref({
        email: rememberEmail.value,
        password: ''
    });

    const handleSubmit = async () => {
        touched.value = true;
        try {
            if (credentials.value.email !== '' && credentials.value.password !== '') {
                loading.value = true;
                rememberMe.value ? localStorage.setItem('rememberMe', credentials.value.email) : localStorage.removeItem('rememberMe');
                const data = await login(credentials.value);
                userStore.setAuthInfo(data.isAuth, data.user.email, data.user.username);
                navigateTo('/');
            } else {
                toast.error('Заполните все поля!');
            }
        } catch (error) {
            console.error('Ошибка авторизации:', error);
            toast.error(error.message);
        } finally {
            loading.value = false;
        }
    };

</script>
