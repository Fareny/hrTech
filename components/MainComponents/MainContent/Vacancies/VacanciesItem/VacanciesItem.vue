<template>
    <AppArticle
        class="main-content__vacancies-item vacancy"
        @click="(event) => openVacancy(event)"
    >
        <NuxtLink :to="getLinkVacancy" target="_blank" class="vacancy__title">{{ props.vacancy.title }}</NuxtLink>
        <p class="vacancy__info">
            <span class="vacancy__salary">{{ vacancyStore.getVacancySalary(props.vacancy) }}</span>
            <span class="vacancy__experience">{{ props.vacancy.experience ? 'Опыт ' + props.vacancy.experience : 'Без опыта' }}</span>
        </p>

        <div class="vacancy__company">
            <span
                class="vacancy__company-name"
            >
                {{ props.vacancy.companyInfo.name }}
                <img
                    v-if="props.vacancy.companyInfo.logo && false"
                    class="vacancy__company-logo"
                    :src="props.vacancy.companyInfo.logo"
                    :alt="props.vacancy.companyInfo.name"
                >
            </span>
            <p class="vacancy__company-location">
                <span class="vacancy__company-city">{{ props.vacancy.companyInfo.location }}</span>
                <span
                    v-if="props.vacancy.companyInfo.subway"
                    class="vacancy__company-subway company-subway"
                >
                    <span
                        class="company-subway__color"
                        :style="`--subway-color: ${props.vacancy.companyInfo.subway.color}`"
                    >
                        ●
                    </span>
                    <span class="company-subway__name">
                        {{ props.vacancy.companyInfo.subway.name }}
                    </span>
                </span>
            </p>
        </div>

        <AppButton
            v-if="!props.isRecruiter"
            class="vacancy__button"
            @click="respondVacancy"
        >
            Откликнуться
        </AppButton>

        <AppDetails
            v-if="!props.isRecruiter"
            class="vacancy__details"
        >
            <template #summary>
                <DotsHorizontal />
            </template>

            <template #content>
                 <DetailsItem
                    v-if="!props.isFavorite"
                    :item="{
                        name: 'Добавить в избранное',
                        value: 'add'
                    }"
                    @selectItem="selectOptionVacancy"
                >
                    Добавить в избранное
                </DetailsItem>
                <DetailsItem
                    v-else
                    :item="{
                        name: 'Удалить из избранного',
                        value: 'remove'
                    }"
                    @selectItem="selectOptionVacancy"
                >
                    Удалить из избранного
                </DetailsItem>
                <DetailsItem
                    :item="{
                        name: 'Скрыть вакансию',
                        value: 'add'
                    }"
                    @selectItem="selectOptionVacancy"
                >
                    Скрыть вакансию
                </DetailsItem>
            </template>
        </AppDetails>
    </AppArticle>
</template>

<script setup>
    import './VacanciesItem.scss'

    import { useVacancyStore } from "~/stores/vacancyStore.js";

    import { removeFavouriteVacancy } from '~/http/http';
    import api from "~/http/api.js";

    import DotsHorizontal from '~/components/AppIcons/DotsHorizontal.vue'

    import AppArticle from "~/components/AppArticle/AppArticle.vue";
    import AppDetails from "~/components/AppDetails/AppDetails.vue";
    import DetailsItem from "~/components/AppDetails/DetailsItem/DetailsItem.vue";

    const props = defineProps({
        vacancy: {
            default: {
                _id: 0,
                title: 'Не найдено',
                date: 'Не найдено',
                salary: null,
                salaryStart: 100000,
                salaryEnd: 200000,
                salaryType: 'between',
                currencySymbol: '₽',
                experience: 'Без опыта',
                companyInfo: {
                    name: 'Не найдено',
                    logo: 'Не найдено',
                    location: 'Не найдено',
                    subway: {
                        name: 'Не найдено',
                        color: 'Не найдено'
                    }
                },
                id_test: ''
            },
            type: Object
        },
        isFavorite: {
            default: false,
            type: Boolean
        },
        isRecruiter: {
            default: false,
            type: Boolean
        }
    })

    const favourites = inject('favouriteVacancies');

    const vacancyStore = useVacancyStore()

    const openVacancy = event => {
        const target = event.target
        if (target.classList.contains('button') ||
            target.tagName === 'svg'
        ) return
        // target.classList.contains('details__content-InputWrapper')
        console.log('openVacancy', event.target)
    }

    const getLinkVacancy = computed(() => {
        return `/vacancy/${props.vacancy._id}`
    })

    const selectOptionVacancy = async (val) => {
        if(val.value === 'remove') {
            favourites.value = favourites.value.filter(vacancy => vacancy._id !== props.vacancy._id)
            await removeFavouriteVacancy(props.vacancy._id)
            // логика загрузки
        }
    }

    const respondVacancy = () => {
        api.post('respond', {
            id: props.vacancy._id
        }).then(() => {
            useRouter().push(`/tests/${props.vacancy.id_test}`)
        })
    }

</script>