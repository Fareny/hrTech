<template>
    <ResumePersonalItem
        @saveModal="saveModal"
    >
        <template #title>
            Обо мне
        </template>

        <template #info>
            <div
                v-if="data.aboutMe !== ''"
                v-html="data.aboutMe"
            />

            <span v-else class="resume__main-empty">Нет указано</span>
        </template>

        <template #edit>
            <AppTextarea
                resize="vertical"
                name="О себе"
                :value="data.aboutMe"
                @changeValue="(val) => dataEdit = val.value"
            />
        </template>
    </ResumePersonalItem>
</template>

<script setup>
    import './ResumePersonalInfo.scss'

    import AppTextarea from "~/components/AppInputs/Textarea/Textarea.vue";
    import ResumePersonalItem from "../ResumePersonalItem/ResumePersonalItem.vue";

    const resumeStore = useResumeStore()

    const data = ref(resumeStore.personalInfo)
    const dataEdit = ref(data.value.aboutMe)

    const saveModal = () => {
        data.value.aboutMe = dataEdit.value
    }

</script>