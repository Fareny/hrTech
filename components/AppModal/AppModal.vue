<template>
    <AppModalContent
        :disableSave="props.disableSave"
        @saveModal="() => emit('saveModal')"
        @closeModal="() => emit('closeModal')"
    >
        <template #summary>
            <div class="modal__summary" @click="modalState = true">
                <slot name="summary"></slot>
            </div>
        </template>

        <template #title>
            <slot name="title"></slot>
        </template>

        <template #content>
            <slot name="content"></slot>
        </template>
    </AppModalContent>
</template>

<script setup>
    import './AppModal.scss'

    import AppModalContent from "./AppModalContent/AppModalContent.vue";

    const props = defineProps({
        disableSave: {
            default: false,
            type: Boolean
        }
    })

    const emit = defineEmits(['saveModal', 'closeModal'])

    const modalState = ref(false)

    provide('modalState', modalState)
</script>