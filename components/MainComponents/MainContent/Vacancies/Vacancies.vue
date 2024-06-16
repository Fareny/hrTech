<template>
    <AppSection class="main-content__vacancies section_no-padding section_no-background">
        <VacanciesItem
            v-for="vacancy in vacancies"
            :key="vacancy.id"
            :vacancy="vacancy"
        />

        <AppButton
            class="main-content__vacancies-load"
            @click="emit('loadVacancies')"
        >
            Загрузить ещё
        </AppButton>
    </AppSection>
</template>

<script setup>
    import './Vacancies.scss'

    import AppSection from "~/components/AppSection/AppSection.vue";
    import VacanciesItem from "~/components/MainComponents/MainContent/Vacancies/VacanciesItem/VacanciesItem.vue";

    const props = defineProps({
        vacancies: {
            default: [],
            type: Array
        }
    })

    const emit = defineEmits(['loadVacancies'])

</script>