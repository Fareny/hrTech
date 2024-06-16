<template>
    <ul class="tests__list">
        <TestsListItem
            v-for="test in props.tests"
            :key="test.id"
            :test="test"
        />
    </ul>
</template>

<script setup>
    import './TestsList.scss'

    import TestsListItem from "./TestsListItem/TestsListItem.vue";

    const props = defineProps({
        tests: {
            default: [],
            type: Array
        }
    })
</script>