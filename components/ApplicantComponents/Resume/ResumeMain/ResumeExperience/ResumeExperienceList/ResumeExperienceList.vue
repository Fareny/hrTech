<template>
    <div class="resume-experience__content experience-content">
        <p class="experience-content__title content-title">
            <span class="content-title__overall-time">{{ overallTime }}</span>
            <ResumeExperienceListEdit />
        </p>

        <ul class="experience-content__list">
            <ResumeExperienceListItem
                v-for="experienceItem in props.experience"
                :key="experienceItem.id"
                :experience="experienceItem"
            />
        </ul>
    </div>

</template>

<script setup>
    import './ResumeExperienceList.scss'

    import ResumeExperienceListItem from "./ResumeExperienceListItem/ResumeExperienceListItem.vue";
    import ResumeExperienceListEdit from "./ResumeExperienceListEdit/ResumeExperienceListEdit.vue";

    const resumeStore = useResumeStore()

    const props = defineProps({
        resumeInfo: {
            default: {},
            type: Object
        },
        experience: {
            default: [],
            type: Array
        }
    })

    const overallTime = computed(() => {
        let totalMonth = 0

        props.experience.forEach((item) => {
            const timeStart = item.timeStart
            const timeEnd = item.timeEnd

            totalMonth += resumeStore.countMonth(timeStart, timeEnd)
        })

        return `Опыт работы ${resumeStore.getExperinceTime(totalMonth)}`
    })
</script>