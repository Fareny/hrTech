<template>
    <AppSection class="main-content__events section_padding-small">
        <SectionTitle>Мои события</SectionTitle>

<!--        <NuxtLink to="/" class="main-content__events-item">-->
<!--        <span class="main-content__events-name">-->
<!--                <UserCheckIcon />-->
<!--                <span class="main-content__events-link">Отклики и приглашения</span>-->
<!--            </span>-->
<!--            <span class="main-content__events-count">0</span>-->
<!--        </NuxtLink>-->
        <!--        <NuxtLink to="/" class="main-content__events-item">-->
<!--            <span class="main-content__events-name">-->
<!--                <EyeSlashedIcon />-->
<!--                <span class="main-content__events-link">Просмотры резюме</span>-->
<!--            </span>-->
<!--            <span class="main-content__events-count main-content__events-count_green">+1</span>-->
<!--        </NuxtLink>-->
        <NuxtLink to="/" class="main-content__events-item">
            <span class="main-content__events-name">
                <HeartIcon />
                <span class="main-content__events-link">Избранные вакансии</span>
            </span>
            <span class="main-content__events-count">0</span>
        </NuxtLink>

    </AppSection>
</template>

<script setup>
    import './Events.scss'

    import AppSection from "~/components/AppSection/AppSection.vue";
    import SectionTitle from "~/components/AppSection/SectionTitle/SectionTitle.vue";

    import UserCheckIcon from '~/components/AppIcons/UserCheck.vue';
    import EyeSlashedIcon from '~/components/AppIcons/EyeSlashed.vue';
    import HeartIcon from '~/components/AppIcons/Heart.vue';

</script>