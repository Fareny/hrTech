<template>
    <AppModal
        :disableSave="props.disableSave"
        @saveModal="emit('saveModal')"
        @closeModal="emit('closeModal')"
    >
        <template #summary>
            <Edit />
        </template>

        <template #title>
            <slot name="title"></slot>
        </template>

        <template #content>
            <slot name="content"></slot>
        </template>
    </AppModal>
</template>

<script setup>
    import './ResumeEditItem.scss'

    import AppModal from "~/components/AppModal/AppModal.vue";
    import Edit from "~/components/AppIcons/Edit.vue";

    const props = defineProps({
        disableSave: {
            default: false,
            type: Boolean
        }
    })

    const emit = defineEmits(['saveModal', 'closeModal'])
</script>