<template>
    <div class="resume__experience resume-experience">
        <ResumeExperienceHeader
            :resumeInfo="resumeStore.resumeInfo"
        />
        <ResumeExperienceList
            :resumeInfo="resumeStore.resumeInfo"
            :experience="resumeStore.resumeInfo.experience"
        />
    </div>
</template>

<script setup>
    import './ResumeExperience.scss'

    import ResumeExperienceHeader from "./ResumeExperienceHeader/ResumeExperienceHeader.vue";
    import ResumeExperienceList from "./ResumeExperienceList/ResumeExperienceList.vue";

    const resumeStore = useResumeStore()
</script>