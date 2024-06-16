<template>
    <AppSection class="section_center vacancy">
        <div class="vacancy__header">
            <div class="vacancy__header-item vacancy-info">
                <h2 class="vacancy__title">{{ currentVacancy.title }}</h2>
                <p class="vacancy__salary">{{ vacancyStore.getVacancySalary(currentVacancy) }}</p>

                <p class="vacancy__experience">
                    Требуемый опыт работы: {{ currentVacancy.experience ? currentVacancy.experience : 'Без опыта' }}
                </p>

                <p class="vacancy__schedule">{{ vacancySchedule }}</p>

                <div class="vacancy__actions">
                    <div class="vacancy__buttons">
                        <AppButton
                            class="vacancy__button"
                            @click="responseVacancy"
                        >
                            Откликнуться
                        </AppButton>
                        <AppButton
                            class="vacancy__button vacancy__button_icon"
                            @click="saveVacancy"
                        >
                            <HeartIcon />
                        </AppButton>
                        <AppButton
                            class="vacancy__button vacancy__button_icon"
                            @click="hideVacancy"
                        >
                            <EyeSlashedIcon />
                        </AppButton>
                    </div>

                    <div class="vacancy__test-info">
                        <TimerIcon />
                        <span>Экспресс тест / 30 минут</span>
                    </div>
                </div>
            </div>

            <div class="vacancy__header-item company-info">
                <div class="company-info__wrapper">
                    <img :src="currentVacancy.companyInfo.logo" :alt="currentVacancy.companyInfo.name">
                    <p class="company-info__name">{{ currentVacancy.companyInfo.name }}</p>
                    <VacancyCompanyRating :rating="currentVacancy.companyInfo.rating" />
                </div>
            </div>
        </div>
        <div class="vacancy__main" v-html="currentVacancy.description" />
        <div class="vacancy__footer">
            <h3 class="vacancy__footer-title">Задайте вопрос работодателю</h3>

            <AppTextarea
                class="vacancy__footer-textarea"
                placeholder="Ваш вопрос"
                @changeValue="(val) => textareaValue = val.value"
            />

            <div class="vacancy__footer-actions">
                <span>Вакансия опубликована 7 мая 2024 в Москве</span>
                <AppButton
                    class="vacancy__footer-button"
                    @click="sendQustion"
                >
                    Отправить
                </AppButton>
            </div>
        </div>
    </AppSection>
</template>

<script setup>
    import './VacancyComponents.scss'

    import AppSection from "~/components/AppSection/AppSection.vue";
    import AppTextarea from "~/components/AppInputs/Textarea/Textarea.vue";
    import VacancyCompanyRating from "~/components/VacancyComponents/VacancyCompanyRating/VacancyCompanyRating.vue";

    import HeartIcon from '~/components/AppIcons/Heart.vue'
    import EyeSlashedIcon from '~/components/AppIcons/EyeSlashed.vue'
    import TimerIcon from '~/components/AppIcons/Timer.vue'

    const props = defineProps({
        id: {
            default: 0,
            type: [String, Number]
        }
    })

    const vacancyStore = useVacancyStore()

    const currentVacancy = ref(await vacancyStore.getVacancyById(props.id))

    const vacancySchedule = computed(() => {
        return [currentVacancy.value.schedule.name, currentVacancy.value.employmentType.name].join(', ')
    })

    const textareaValue = ref('')

    const sendQustion = () => {
        console.log('sendQustion')
    }

    const responseVacancy = () => {
        console.log('responseVacancy')
    }

    const saveVacancy = () => {
        console.log('saveVacancy')
    }

    const hideVacancy = () => {
        console.log('hideVacancy')
    }

</script>