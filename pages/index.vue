<template>
    <MainComponents
        :data="props.data"
        @search="(val) => emit('search', val)"
    />
</template>

<script setup>
    import MainComponents from "~/components/MainComponents/MainComponents.vue";

    const props = defineProps({
        data: {
            default: [],
            type: Array
        }
    })

    const emit = defineEmits(['search'])

</script>