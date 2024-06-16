<template>
         <AppSection class="section_no-background section_no-padding">
            <div class="myVacancy">
                <h2 class="myVacancy__title">Мои вакансии</h2>
                <AppButton class="button_clear">
                    <NuxtLink to="/create-vacancy" class="content-actions__item">Создать вакансию</NuxtLink>
                </AppButton>
            </div>

            <ul v-if="myVacancies.length > 0">
                <VacanciesItem
                    v-for="vacancy in myVacancies"
                    :vacancy="vacancy"
                    :key="vacancy.id"
                    :isRecruiter="false"
                />
            </ul>
            <p v-else class="myVacancy__empty" >У вас нет созданных вакансий</p>
         </AppSection>
</template>

<script setup>
    import './MyVacancy.scss'
    import AppSection from '../AppSection/AppSection.vue';
    import { onMounted, ref } from "vue";
    import AppButton from "../AppButton/AppButton.vue";
    import { getMyVacancies } from "~/http/http";
    import VacanciesItem from "../MainComponents/MainContent/Vacancies/VacanciesItem/VacanciesItem.vue";

    const myVacancies = ref([]);

    onMounted(() => {
        const getMyVacanciesInfo = async () => {
            const data = await getMyVacancies()
            myVacancies.value = data.jobs
        }

        getMyVacanciesInfo()
    })

</script>