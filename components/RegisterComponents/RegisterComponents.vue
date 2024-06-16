<template>
        <section class="reg__section">
            <div class="reg__container">

                <div class="reg__image">
                        <div class="reg__image-container">
                            <img src="~/assets/svg/arrowBack.svg" alt="arrowBack">
                        </div>
                        <div>
                            <h3 class="reg__image-title">С возвращением!</h3>
                            <p class="reg__image-text">Для того чтобы продолжить пользоваться сайтом, войдите в свою учетную запись</p>
                        </div>

                    <NuxtLink class="reg__image-button" to="/authorization">
                        <img src="~/assets/svg/arrow.svg" alt="arrow">
                        <span class="reg__image-button-text">Войти</span>
                    </NuxtLink>
                </div>
                
                <form class="reg__form" @submit.prevent="handleSubmit">
                <h2 class="reg__title">Регистрация</h2>
                <fieldset class="reg__inputs">
                        <AppInput
                            class="reg__input"
                            id="username"
                            type="text"
                            placeholder="Введите ваше ФИО"
                            :value="credentials.username"
                            @changeValue="(val) => credentials.username = val.value"
                        />

                        <ErrorCircleIcon v-if="!credentials.password && touched" class="reg__input-icon" />
                </fieldset>

                <fieldset class="reg__inputs">
                        <AppInput
                            class="reg__input"
                            id="email"
                            type="text"
                            placeholder="Введите ваш email"
                            :value="credentials.email"
                            @changeValue="(val) => credentials.email = val.value"
                        />

                        <ErrorCircleIcon v-if="!credentials.password && touched" class="reg__input-icon" />
                </fieldset>
                
                    <fieldset class="reg__inputs" >
                        <AppInput
                            class="reg__input"
                            id="password"
                            type="password"
                            placeholder="Введите ваш пароль"
                            :value="credentials.password"
                            @changeValue="(val) => credentials.password = val.value"
                        />

                        <ErrorCircleIcon v-if="!credentials.password && touched" class="reg__input-icon" />
                    </fieldset>

                    <fieldset class="reg__inputs_checkbox">
                        <AppCheckbox
                            type="radio"
                            id="job_seeker"
                            name="userType"
                            value="job_seeker"
                            @changeValue="(val) => credentials.userType = val.id"
                        >
                            <span>Я ищу работу</span>
                        </AppCheckbox>
                        <AppCheckbox
                            type="radio"
                            id="employer"
                            name="userType"
                            value="employer"
                            @changeValue="(val) => credentials.userType = val.id"
                        >
                            <span>Я ищу сотрудников</span>
                        </AppCheckbox>
                    </fieldset>

                    <fieldset class="reg__checkbox reg-checkbox reg-remeber">
                        <AppCheckbox
                            class="reg-checkbox__item"
                            type="checkbox"
                            @changeValue="(val) => rememberMe = val.value"
                        >
                            <span class="reg__checkbox_text">Запомнить меня</span>
                        </AppCheckbox>
                    </fieldset>

                    <AppButton
                        class="reg__form-button"
                        :disabled="loading"
                    >
                        <template v-if="loading">
                            <Loader class="reg__form__loading-icon" />
                        </template>
                        <template v-else>
                            Зарегистрироваться
                        </template>
                    </AppButton>

                    <NuxtLink class="reg__form-link" to="/authorization">Уже есть аккаунт? Войти</NuxtLink>
                </form>
            </div>  
        </section>
</template>

<script setup>
    import './RegisterComponents.scss'

    import { registration } from '~/http/http.js'

    import AppInput from '~/components/AppInputs/Input/Input.vue';
    import AppCheckbox from "~/components/AppInputs/Checkbox/Checkbox.vue";

    import ErrorCircleIcon from "~/components/AppIcons/ErrorCircle.vue";
    import Loader from "~/components/AppIcons/Loader.vue";
    import { toast } from 'vue3-toastify';

    const touched = ref(false);
    const loading = ref(false);
    const userStore = useUserStore();

    const rememberMe = ref(false);
    const credentials = ref({
        email: '',
        username: '',
        password: '',
        userType: ''
    });

    const handleSubmit = async () => { 
        touched.value = true;

        try {
            if(credentials.value.username !== '' && 
                credentials.value.email !== '' && 
                credentials.value.password !== '' && 
                credentials.value.userType !== '') {

                loading.value = true;
                rememberMe.value ? localStorage.setItem('rememberMe', credentials.value.email) : localStorage.removeItem('rememberMe');

                const data = await registration(credentials.value);
                userStore.setAuthInfo(data.isAuth, data.user.email, data.user.username);

                navigateTo('/');
            } else {
               toast.error('Заполните все поля!');
            }
        } catch (error) {
            console.error('Ошибка регистрации:', error);
            toast.error('Произошла ошибка при регистрации!');
        } finally {
            loading.value = false;
        }
    };
</script>
