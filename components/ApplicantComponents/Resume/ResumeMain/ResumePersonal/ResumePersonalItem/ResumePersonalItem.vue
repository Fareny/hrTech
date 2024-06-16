<template>
    <div class="resume-personal__item">
        <div class="resume-personal__item-title item-title">
            <h4 class="item-title__text">
                <slot name="title"></slot>
            </h4>
            <ResumeEditItem
                @saveModal="() => emit('saveModal')"
                @closeModal="() => emit('closeModal')"
            >
                <template #title>Редактирование</template>

                <template #content>
                    <slot name="edit"></slot>
                </template>
            </ResumeEditItem>
        </div>
        <div class="resume-personal__item-info">
            <slot name="info"></slot>
        </div>
    </div>

</template>

<script setup>
    import './ResumePersonalItem.scss'

    import ResumeEditItem from "~/components/ApplicantComponents/Resume/ResumeEditItem/ResumeEditItem.vue";

    const emit = defineEmits(['saveModal', 'closeModal'])
</script>