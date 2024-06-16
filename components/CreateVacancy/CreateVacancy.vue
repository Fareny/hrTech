<template>
    <AppSection class="create-vacancy__section">
        <h2>Создание вакансии</h2>

        <form @submit.prevent="createJobPosting" class="create-vacancy">
            <div class="create-vacancy__input_vacancy">
                <AppInput
                    class="create-vacancy__input"
                    labelText="Название компании"
                    placeholder="ООО «Компания»"
                    :value="form.name"
                    @changeValue="(val) => { form.name = val.value; validateField('name'); }"
                    type="text"
                />
                <span v-if="errors.name" class="error">{{ errors.name }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppInput
                    class="create-vacancy__input"
                    labelText="Город"
                    placeholder="Москва"
                    :value="form.location"
                    @changeValue="(val) => { form.location = val.value; validateField('location'); }"
                    type="text"
                />
                <span v-if="errors.location" class="error">{{ errors.location }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppInput
                    class="create-vacancy__input"
                    labelText="Метро"
                    placeholder="Ленинский проспект"
                    :value="form.subway"
                    @changeValue="(val) => { form.subway = val.value; validateField('subway'); }"
                    type="text"
                />
                <span v-if="errors.subway" class="error">{{ errors.subway }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppInput
                    class="create-vacancy__input"
                    labelText="Название вакансии"
                    placeholder="Back-end разработчик"
                    :value="form.title"
                    @changeValue="(val) => { form.title = val.value; validateField('title'); }"
                    type="text"
                />
                <span v-if="errors.title" class="error">{{ errors.title }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppInput
                    class="create-vacancy__input"
                    labelText="Зарплата От"
                    placeholder="50000"
                    :value="form.salaryStart"
                    @changeValue="(val) => { form.salaryStart = val.value; validateField('salaryStart'); }"
                    type="text"
                />
                <span v-if="errors.salaryStart" class="error">{{ errors.salaryStart }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppInput
                    class="create-vacancy__input"
                    labelText="Зарплата До"
                    placeholder="100000"
                    :value="form.salaryEnd"
                    @changeValue="(val) => { form.salaryEnd = val.value; validateField('salaryEnd'); }"
                    type="text"
                />
                <span v-if="errors.salaryEnd" class="error">{{ errors.salaryEnd }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppSelect
                    class="create-vacancy__input"
                    :id="experience.id"
                    :name="experience.name"
                    :value="experience.type"
                    :options="experience.options"
                    @changeValue="(val) => { form.experience = val.value; validateField('experience'); }"
                />
                <span v-if="errors.experience" class="error">{{ errors.experience }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppSelect
                    class="create-vacancy__input"
                    :id="typeOfEmployment.id"
                    :name="typeOfEmployment.name"
                    :value="typeOfEmployment.type"
                    :options="typeOfEmployment.options"
                    :isMultiple="true"
                    @changeValue="(val) => { form.typeOfEmployment = val.value; validateField('typeOfEmployment'); }"
                />
                <span v-if="errors.typeOfEmployment" class="error">{{ errors.typeOfEmployment }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppSelect
                    class="create-vacancy__input"
                    :id="educations.id"
                    :name="educations.name"
                    :value="educations.type"
                    :options="educations.options"
                    :isMultiple="true"
                    @changeValue="(val) => { form.educations = val.value; validateField('educations'); }"
                />
                <span v-if="errors.educations" class="error">{{ errors.educations }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppSelect
                    class="create-vacancy__input"
                    :id="workSchedule.id"
                    :name="workSchedule.name"
                    :value="workSchedule.type"
                    :options="workSchedule.options"
                    :isMultiple="true"
                    @changeValue="(val) => { form.workSchedule = val.value; validateField('workSchedule'); }"
                />
                <span v-if="errors.workSchedule" class="error">{{ errors.workSchedule }}</span>
            </div>

            <div class="create-vacancy__input_vacancy logo-upload">
                <AppInput
                    labelText="Логотип компании"
                    type="file"
                    accept="image/png, image/jpeg"
                    @change="handleFileUpload"
                />
                <img v-if="logoPreview" :src="logoPreview" alt="Логотип компании" class="logo-preview"/>
                <span v-if="errors.logo" class="error">{{ errors.logo }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppTextarea
                    labelText="Описание вакансии"
                    placeholder="Краткое описание вакансии"
                    :value="form.description"
                    @changeValue="(val) => { form.description = val.value; validateField('description'); }"
                    resize="vertical"
                />
                <span v-if="errors.description" class="error">{{ errors.description }}</span>
            </div>

            <div class="create-vacancy__input_vacancy">
                <AppSelect
                    class="create-vacancy__input"
                    :options="testsSelect.options"
                    @changeValue="(val) => { form.testId = val.value; }"
                />
                <span v-if="errors.testId" class="error">{{ errors.testId }}</span>
            </div>

            <div class="create-vacancy__buttons">
                <AppButton class="create-vacancy__button" type="submit">Создать вакансию</AppButton>
            </div>
        </form>
    </AppSection>
</template>

<script setup>
    import './CreateVacancy.scss'

    import {ref} from 'vue';

    import AppSection from '../AppSection/AppSection.vue';
    import AppInput from '../AppInputs/Input/Input.vue';
    import AppTextarea from '../AppInputs/Textarea/Textarea.vue';
    import AppSelect from '../AppInputs/Select/Select.vue';
    import AppButton from '../AppButton/AppButton.vue'
    import {createNewVacancy} from '~/http/http';
    import api from "~/http/api.js";

    const form = ref({
        name: '',
        location: '',
        subway: '',
        title: '',
        salaryStart: '',
        salaryEnd: '',
        experience: '',
        workSchedule: [],
        educations: [],
        typeOfEmployment: [],
        description: '',
        logo: null,
        testId: ''
    });

    const errors = ref({
        name: '',
        location: '',
        subway: '',
        title: '',
        salaryStart: '',
        salaryEnd: '',
        experience: '',
        workSchedule: '',
        educations: '',
        typeOfEmployment: '',
        description: '',
        logo: '',
        testId: ''
    });

    const workSchedule = ref({
        options: [
            {value: 'full-day', label: 'Полный день'},
            {value: 'remote', label: 'Удалённая работа'},
            {value: 'flexible', label: 'Гибкий график'},
            {value: 'shift', label: 'Сменный график'},
            {value: 'wfh', label: 'Вахтовый метод'}
        ]
    });

    const experience = ref({
        options: [
            {value: 'Без опыта', label: 'Без опыта'},
            {value: '1-3 года', label: 'От 1 года до 3 лет'},
            {value: '3-6 лет', label: 'От 3 до 6 лет'},
            {value: '>6 лет', label: 'Более 6 лет'}
        ]
    });

    const educations = ref({
        options: [
            {value: 'Не требуется', label: 'Не требуется'},
            {value: 'secondary', label: 'Среднее'},
            {value: 'secondary-special', label: 'Среднее специальное'},
            {value: 'secondary-professional', label: 'Среднее профессиональное'},
            {value: 'high', label: 'Высшее'},
        ]
    });

    const typeOfEmployment = ref({
        options: [
            {value: 'full-time', label: 'Полная занятость'},
            {value: 'part-time', label: 'Частичная занятость'},
            {value: 'project', label: 'Проектная работа'},
        ]
    });

    const logoPreview = ref(null);

    const validateField = (field) => {
        if (form.value[field] === '' || (Array.isArray(form.value[field]) && form.value[field].length === 0)) {
            errors.value[field] = 'Это поле не может быть пустым';
        } else {
            if (field === 'salaryStart' || field === 'salaryEnd') {
                if (isNaN(form.value[field])) {
                    errors.value[field] = 'Это поле должно содержать только числа';
                } else {
                    errors.value[field] = '';
                }
            } else {
                errors.value[field] = '';
            }
        }
    };

    const handleFileUpload = (event) => {
        const file = event.target.files[0];
        form.value.logo = file;
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                logoPreview.value = e.target.result;
            };
            reader.readAsDataURL(file);
        } else {
            logoPreview.value = null;
        }
    };

    const validateForm = () => {
        Object.keys(form.value).forEach(validateField);
        return Object.values(errors.value).every(error => error === '');
    };

    const createJobPosting = async () => {
        if (!validateForm()) {
            return;
        }

        const formData = new FormData();
        formData.append('name', form.value.name);
        formData.append('location', form.value.location);
        formData.append('subway', form.value.subway);
        formData.append('title', form.value.title);
        formData.append('salaryStart', form.value.salaryStart);
        formData.append('salaryEnd', form.value.salaryEnd);
        formData.append('experience', JSON.stringify(form.value.experience));
        formData.append('workSchedule', JSON.stringify(form.value.workSchedule));
        formData.append('educations', JSON.stringify(form.value.educations));
        formData.append('typeOfEmployment', JSON.stringify(form.value.typeOfEmployment));
        formData.append('description', form.value.description);
        formData.append('id_test', form.value.testId);
        if (form.value.logo) {
            formData.append('logo', form.value.logo);
        }

        const data = await createNewVacancy(formData);
        if (data.status === 'ok') {
            navigateTo('/my-vacancies')
        }
    };

    const testsSelect = ref({
        options: []
    })

    const getTestsOptions = () => {
        const optionsTest = ref([])

        api.get('get-tests')
            .then((data) => {
                data.forEach(test => {
                    optionsTest.value.push({label: test.name, value: test.id})
                })

                testsSelect.value.options = optionsTest.value
            })
    }

    getTestsOptions()
</script>
