<template>
    <slot name="summary"></slot>

    <dialog
        v-if="modalState"
        open
        class="modal"
        ref="modal"
        @click.self="closeModal"
    >
        <AppSection
            @mousedown="handleMouseDown"
            @mouseup="handleMouseUp"
        >
            <h4 class="modal__title">
                <slot name="title"></slot>
            </h4>

            <div class="modal__content">
                <slot name="content"></slot>
            </div>

            <div class="modal__actions">
                <AppButton @click="saveModal" :disabled="props.disableSave">Сохранить</AppButton>
                <AppButton @click="closeModal">Отмена</AppButton>
            </div>

            <AppButton class="modal__close" @click="closeModal">
                <CaClose />
            </AppButton>
        </AppSection>
    </dialog>
</template>

<script setup>
    import './AppModalContent.scss'

    import AppButton from '~/components/AppButton/AppButton.vue'

    import CaClose from "~/components/AppIcons/Close.vue";

    const props = defineProps({
        disableSave: {
            default: false,
            type: Boolean
        }
    })

    const emit = defineEmits(['closeModal', 'saveModal'])

    const modal = ref(null)
    const modalState = inject('modalState')

    const isMouseDown = ref(false)

    const closeModal = () => {
        if (isMouseDown.value) {
            isMouseDown.value = false
            return
        }

        emit('closeModal')
        modalState.value = false
    }

    const saveModal = () => {
        modalState.value = false
        emit('saveModal')
    }

    const handleMouseDown = () => {
        isMouseDown.value = true
    }
    const handleMouseUp = () => {
        isMouseDown.value = false
    }

    watch(() => modalState.value, () => {
        if (modalState.value) document.body.classList.add('body_uncscroll')
        else document.body.classList.remove('body_uncscroll')
    })
</script>