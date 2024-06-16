<template>
    <!-- <AppSection> -->
        <div>
            <h2 class="favourites__title">Избранные вакансии</h2>
            <ul v-if="favouriteVacancies.length > 0" class="favourites__list">
                <VacanciesItem v-for="vacancy in favouriteVacancies" :vacancy="vacancy" :favouriteVacancies="favouriteVacancies" :isFavorite="true" :key="vacancy.id" />
            </ul>
            <p v-else class="favourites__empty" >У вас нет избранных вакансий</p>
        </div>
    <!-- </AppSection> -->
</template>

<script setup>
    import './FavouriteComponents.scss'
    import { onMounted, ref } from "vue";
    import { getFavouriteVacancies } from "~/http/http";
    import VacanciesItem from "~/components/MainComponents/MainContent/Vacancies/VacanciesItem/VacanciesItem.vue";

    const favouriteVacancies = ref([]);

    onMounted(() => {
        const getFavouriteInfo = async () => {
            const data = await getFavouriteVacancies()
            favouriteVacancies.value = data.favourites
        }

        getFavouriteInfo()
    })

    provide('favouriteVacancies', favouriteVacancies)
</script>