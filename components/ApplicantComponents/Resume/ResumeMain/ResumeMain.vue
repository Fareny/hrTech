<template>
    <div class="resume__main resume-main">
        <ResumePersonal />
        <ResumeExperience />
        <ResumeEducation />
        <ResumeLanguage />
        <ResumeCitizenship />
    </div>
</template>

<script setup>
    import './ResumeMain.scss'

    import ResumePersonal from "./ResumePersonal/ResumePersonal.vue";
    import ResumeExperience from "./ResumeExperience/ResumeExperience.vue";
    import ResumeEducation from "./ResumeEducation/ResumeEducation.vue";
    import ResumeLanguage from "./ResumeLanguage/ResumeLanguage.vue";
    import ResumeCitizenship from "./ResumeCitizenship/ResumeCitizenship.vue";


</script>