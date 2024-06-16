<template>
    <form
        class="search"
        @submit.prevent="search"
    >
        <button class="search__button">
            <SearchIcon />
        </button>

        <AppInput
            id="search"
            type="search"
            placeholder="Профессия, должность или компания"
            :value="searchValue"
            @changeValue="(val) => searchValue = val.value"
        />
    </form>
</template>

<script setup>
    import './Search.scss'

    import AppInput from '~/components/AppInputs/Input/Input.vue';
    import SearchIcon from '~/components/AppIcons/Search.vue';

    const emit = defineEmits(['search'])

    const searchValue = ref('')

    const search = () => {
        emit('search', searchValue.value)
    }
</script>