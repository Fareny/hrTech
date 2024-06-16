<template>
    <VacancyComponents :id="route.params.id" />
</template>

<script setup>
    import VacancyComponents from '~/components/VacancyComponents/VacancyComponents.vue'

    const route = useRoute()
</script>