<template>
    <ResumeEditItem
        :disableSave="validateTimes"
        @saveModal="saveModal"
        @closeModal="resetExperienceEdit"
    >
        <template #title>Редактирование</template>

        <template #content>
            <div class="resume-experience__edit experience-edit">
                <ResumeExperienceEditItem
                    v-for="experienceItem in experienceEdit"
                    :key="experienceItem.id"
                    :experienceId="experienceItem.id"
                    :resumeStore="resumeStore"
                />

                <AppButton
                    class="experience-edit__btn edit-btn__add"
                    @click="addWorkPlace"
                >
                    Добавить место работы
                </AppButton>
            </div>
        </template>
    </ResumeEditItem>
</template>

<script setup>
    import './ResumeExperienceListEdit.scss'

    import ResumeEditItem from "~/components/ApplicantComponents/Resume/ResumeEditItem/ResumeEditItem.vue";
    import ResumeExperienceEditItem from "~/components/ApplicantComponents/Resume/ResumeMain/ResumeExperience/ResumeExperienceList/ResumeExperienceListEdit/ResumeExperienceListEditItem/ResumeExperienceListEditItem.vue";

    const props = defineProps({
        experience: {
            default: {},
            type: Object
        }
    })

    const resumeStore = useResumeStore()

    const experienceEdit = ref()
    const validateTimes = ref(false)

    const resetExperienceEdit = () => {
        experienceEdit.value = JSON.parse(JSON.stringify(resumeStore.resumeInfo.experience))
    }

    const addWorkPlace = () => {
        experienceEdit.value.push(resumeStore.getNewWorkPlace())
    }

    const saveModal = () => {
        resumeStore.resumeInfo.experience = JSON.parse(JSON.stringify(experienceEdit.value))
    }

    watch(() => experienceEdit.value, () => {
        validateTimes.value = !!experienceEdit.value.find((item) => !item.validateTime)
    }, { deep: true })

    resetExperienceEdit()

    provide('experienceEdit', experienceEdit)
</script>