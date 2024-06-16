<template>
    <AppSection class="section_no-background">
        <section class="main__search main-search">
            <div class="main-search__actions">
                <AppSearch
                    @search="(val) => search(val)"
                />
                <AppDetails
                    v-for="sortItem in sortItems"
                    class="main-search__action"
                    :key="sortItem.key"
                    :closeByClick="true"
                >
                    <template #summary>
                        <span>{{ getActiveSort(sortItem.items) }}</span>
                        <ArrowDown />
                    </template>
                    <template #content>
                        <DetailsItem
                            v-for="item in sortItem.items"
                            :key="item.value"
                            :itemKey="sortItem.key"
                            :item="item"
                            @selectItem="(val) => selectItem(val)"
                        >
                            <Check />
                            <span>{{ item.name }}</span>
                        </DetailsItem>
                    </template>
                </AppDetails>

            </div>
            <p class="main-search__vacancy-count">
                <span v-if="countVacancy > 0">
                    Кол-во подходящих вакансий: {{ countVacancy }}
                </span>
                    <span v-else>
                    Подходящих вакансий не найдено
                </span>
            </p>
        </section>
    </AppSection>
</template>

<script setup>
    import './MainSearch.scss'

    import sortItemsData from "~/data/mainPage/sortItems.js";

    import AppSearch from "~/components/AppInputs/Search/Search.vue";
    import AppSection from "~/components/AppSection/AppSection.vue";
    import AppDetails from "~/components/AppDetails/AppDetails.vue";
    import DetailsItem from "~/components/AppDetails/DetailsItem/DetailsItem.vue";

    import Check from '~/components/AppIcons/Check.vue'
    import ArrowDown from "~/components/AppIcons/ArrowDown.vue";

    const vacancyStore = useVacancyStore()

    const sortItems = ref(sortItemsData)

    // Когда будем получать вакансии, будем передавать их кол-во в этупеременную
    const countVacancy = ref(0)

    const getActiveSort = (arr) => {
        const activeItem = arr.find(item => item.active)
        return activeItem ? activeItem.name : 'Не найдено'
    }

    // При отправлении данных вверх по компонентам, перехватываем это событие и получаем нужные данные
    const search = (val) => {
        vacancyStore.searchValue = val
        vacancyStore.getVacancies()
    }

    const selectItem = (item) => {
        const currentSort = sortItems.value.find(sort => sort.key === item.key).items
        currentSort.forEach(sortItem => {
            sortItem.active = sortItem.value === item.value
        })
    }
</script>