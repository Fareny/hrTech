<template>
    <div class="vacancy__company-rating company-rating">
        <!--    TODO: Переписать под новые иконки    -->
        <component
            v-for="i in 5"
            :key="i"
            class="company-rating__icon"
            :is="defineStar(i)"
        />
        <span>{{ props.rating }}</span>
    </div>
</template>

<script setup>
    import './VacancyCompanyRating.scss'

    import StarIcon from '~/components/AppIcons/Star.vue';
    import StarHalfIcon from '~/components/AppIcons/StarHalf.vue';
    import StarFillIcon from '~/components/AppIcons/StarFill.vue';

    const props = defineProps({
        rating: {
            default: 0,
            type: Number
        }
    })

    const defineStar = (i) => {
        return props.rating > i ? StarFillIcon : props.rating + 0.5 >= i ? StarHalfIcon : StarIcon
    }
</script>