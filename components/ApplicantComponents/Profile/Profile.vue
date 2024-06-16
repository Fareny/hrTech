<template>
    <section class="profile__section">
        <div class="profile__container">
            <div class="profile__image_overlay">
                <div class="profile__icon_wrapper" @click="triggerFileInput">
                    <ImagePlusIcon class="profile__icon" />
                    <input 
                        type="file" 
                        ref="fileInput" 
                        @change="handleImageUpload" 
                        class="profile__image_input"
                        accept="image/*"
                    />
                </div>
                <img class="profile__image" :src="`${profile.avatar}`" alt="avatar">
            </div>
            <div class="profile__content">
                <p class="profile__name">{{ profile.username }}</p>
                <p class="profile__email">{{ profile.email }}</p>
            </div>
        </div>

        <div class="profile__settings">
            <h2 class="profile__title">Настройки</h2>
            <div class="profile__fields">
                <div v-for="(field, key) in profileFields" :key="key" class="profile__field">

                    <span class="profile__label">{{ field.label }}</span>
                    <AppInput
                        v-if="key !== 'password'"
                        :value="profile[key]"
                        :mask="profile[key]"
                        :type="field.inputType"
                        :status="editMode[key]"
                        class="profile__input"
                        :class="{'profile__input_active': editMode[key]}"
                        :placeholder="field.label"
                        @changeValue="(val) => profile[key] = val.value"
                    />

                    <span
                        v-if="field.type === 'text' && key === 'password' && !editMode[key]"
                        class="profile__value"
                    >
                        {{ field.value }}
                    </span>

                    <div
                        v-if="key === 'password' && editMode[key]"
                        class="password__fields"
                    >
                        <AppInput
                            :value="passwordFields.oldPassword"
                            label="Старый пароль"
                            type="password"
                            placeholder="Старый пароль"
                            class="profile__input_active"
                            @changeValue="(val) => passwordFields.oldPassword = val.value"
                        />
                        <a class="profile__link" href="#">Забыли пароль?</a>
                        <AppInput
                            :value="passwordFields.newPassword"
                            label="Новый пароль"
                            type="password"
                            placeholder="Новый пароль"
                            class="profile__input_active"
                            @changeValue="(val) => passwordFields.newPassword = val.value"
                        />
                        <AppInput
                            :value="passwordFields.confirmNewPassword"
                            label="Подтвердите новый пароль"
                            type="password"
                            placeholder="Подтвердите новый пароль"
                            class="profile__input_active"
                            @changeValue="(val) => passwordFields.confirmNewPassword = val.value"
                        />
                    </div>

                    <div class="profile__button_wrapper">
                        <AppButton
                            class="profile__button"
                            @click="toggleEdit(key)"
                        >
                            {{ editMode[key] ? 'Сохранить' : 'Изменить' }}
                        </AppButton>
                        <AppButton
                            class="profile__button"
                            v-if="editMode[key]"
                            @click="cancelEdit(key)"
                        >
                            Отмена
                        </AppButton>
                    </div>
                </div>
            </div>
            <AppButton class="profile__exit__button" @click="handleExit" >
                Выйти
            </AppButton>
        </div>
    </section>
</template>

<script setup>
import './Profile.scss';
import { reactive, onMounted, ref } from 'vue';
import AppInput from '../../AppInputs/Input/Input.vue';
import AppButton from '../../AppButton/AppButton.vue';
import { getMyProfile, profileUpdate, updateProfileAvatar } from '~/http/http';
import api from "~/http/api.js";
import ImagePlusIcon from '~/components/AppIcons/ImagePlus.vue';
import { toast } from 'vue3-toastify';

const profile = reactive({
    username: '',
    email: '',
    phone_number: '',
    job_search: '',
    avatar: '',
    last_change_password: '',
    new_password: {}
});

const editMode = reactive({
    username: false,
    email: false,
    password: false,
    phone_number: false,
    job_search: false
});

const profileFields = {
    username: { label: 'Имя', type: 'input', inputType: 'text' },
    email: { label: 'Email', type: 'input', inputType: 'email' },
    password: { label: 'Пароль', type: 'text', value: 'Обновлён никогда' },
    phone_number: { label: 'Мобильный телефон', type: 'input', inputType: 'tel' },
    job_search: { label: 'Район поиска работы', type: 'input', inputType: 'text' }
};

const passwordFields = reactive({
    oldPassword: '',
    newPassword: '',
    confirmNewPassword: ''
});

const fileInput = ref(null);

let tempProfile = {};
let tempPasswordFields = {};

const toggleEdit = (field) => {
    if (!editMode[field]) {
        tempProfile = { ...profile };
        tempPasswordFields = { ...passwordFields };
    } else {
        if (field === 'password') {
            savePassword();
        } else {
            saveProfile();
        }
    }
    editMode[field] = !editMode[field];
};

const handleExit = async () => {
    navigateTo('/authorization');
    await api.get('logout');
};

const saveProfile = async () => {
    const data = await profileUpdate(profile);
    if(data.status === 'ok') {
        toast.success('Профиль обновлен!');
    } else {
        toast.error('Не удалось обновить профиль!');
    }
};

const savePassword = async () => {

    if(!passwordFields.oldPassword || !passwordFields.newPassword || !passwordFields.confirmNewPassword) {
        toast.error('Необходимо заполнить все поля!');
        return;
    }

    if (passwordFields.newPassword !== passwordFields.confirmNewPassword) {
        toast.error('Пароли не совпадают!');
        return;
    }
    
    profile.new_password = {
        old_password: passwordFields.oldPassword,
        new_password: passwordFields.newPassword
    };

    const data = await profileUpdate(profile);
    if (data.status === 'ok') {
        profileFields.password.value = `Обновлен: только что`;
        toast.success('Пароль обновлен!');
    } else {
        toast.error('Не удалось обновить пароль!');
    }

    profile.new_password = {};
    passwordFields.oldPassword = '';
    passwordFields.newPassword = '';
    passwordFields.confirmNewPassword = '';
};

const cancelEdit = (field) => {
    if (field === 'password') {
        Object.assign(passwordFields, tempPasswordFields);
    } else {
        profile[field] = tempProfile[field];
    }
    editMode[field] = false;
};

const handleImageUpload = async (event) => {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('avatar', file);
        toast.info('Обновляю аватар...');
        const data = await updateProfileAvatar(formData);
        if (data.status === 'ok') {
            profile.avatar = data.link;
            toast.success('Аватар обновлен!');
        } else {
            console.error('Failed to upload image');
        }
    }
};

const triggerFileInput = () => {
    fileInput.value.click();
};

onMounted(() => {
    const getProfileInfo = async () => {
        const data = await getMyProfile();
        profile.username = data.username;
        profile.email = data.email;
        profile.phone_number = data.phone_number;
        profile.job_search = data.job_search;
        profile.avatar = data.avatar;
        profile.last_change_password = data.last_change_password;
        profileFields.password.value = `Обновлен: ${profile.last_change_password}`;
    };

    getProfileInfo();
});
</script>

<style scoped>
.profile__image_overlay {
    position: relative;
    width: 150px;
    height: 150px;
    margin: 0 auto;
}
.profile__image_input {
    display: none;
}
.profile__image {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}
</style>
