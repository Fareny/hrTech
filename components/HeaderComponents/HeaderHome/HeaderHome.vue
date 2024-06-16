<template>
    <section
        class="header__homepage"
    >
        <div class="header__homepage-preview homepage-preview">
            <p class="homepage-preview__tagline">Уютное место работы для каждого</p>

            <AppSearch
                class="homepage-preview__search"
            />

            <button class="homepage-preview__next" @click="scrollToMain">
                <img src="~/public/icons/arrow-next.svg" class="homepage-preview__next-icon" alt="arrow-next">
            </button>
        </div>

        <div class="header__homepage-statistics homepage-statistics">
            <div class="homepage-statistics__item">
                <p class="homepage-statistics__item-value">69 332 090</p>
                <p class="homepage-statistics__item-label">Резюме</p>
            </div>
            <div class="homepage-statistics__item">
                <p class="homepage-statistics__item-value">1 469 017</p>
                <p class="homepage-statistics__item-label">Вакансий</p>
            </div>
            <div class="homepage-statistics__item">
                <p class="homepage-statistics__item-value">2 189 288</p>
                <p class="homepage-statistics__item-label">Компаний</p>
            </div>
        </div>

    </section>
</template>

<script setup>
    import './HeaderHome.scss'

    import AppSearch from "~/components/AppInputs/Search/Search.vue";

    // import { getCurrentInstance } from 'vue';
    // const thisInstance = getCurrentInstance();
    // console.log('thisInstance', thisInstance?.vnode?.props?.onSearch)

    const scrollToMain = () => {
        const main = document.querySelector('.main');
        main.scrollIntoView({ behavior: 'smooth' });
    }
</script>