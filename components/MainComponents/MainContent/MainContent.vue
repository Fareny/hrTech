<template>
    <AppSection class="main-content section_center section_no-background">
        <aside>
            <Events />
        </aside>

        <Vacancies
            :vacancies="vacancyStore.vacancies"
            @loadVacancies="vacancyStore.loadVacancies"
        />

        <aside>
            <Filters />
        </aside>
    </AppSection>
</template>

<script setup>
    import './MainContent.scss'

    import Events from "~/components/MainComponents/MainContent/Events/Events.vue";
    import Vacancies from "~/components/MainComponents/MainContent/Vacancies/Vacancies.vue";
    import Filters from "~/components/MainComponents/MainContent/Filters/Filters.vue";

    const vacancyStore = useVacancyStore()

    vacancyStore.getVacancies()
    vacancyStore.getFilters()

</script>