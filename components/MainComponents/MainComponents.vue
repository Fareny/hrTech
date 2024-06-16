<template>
    <client-only>
        <MainSearch v-show="userStore.isAuth" />
        <MainContent />
    </client-only>
</template>

<script setup>
    import './MainComponents.scss'

    import MainContent from "~/components/MainComponents/MainContent/MainContent.vue";
    import MainSearch from "~/components/MainComponents/MainSearch/MainSearch.vue";

    const userStore = useUserStore();

</script>
