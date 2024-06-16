<template>
    <div class="resume__personal resume-personal">
        <ResumePersonalInfo />
        <ResumePersonalContacts />
        <ResumePersonalSkills />
    </div>
</template>

<script setup>
    import './ResumePersonal.scss'

    import ResumePersonalInfo from "./ResumePersonalInfo/ResumePersonalInfo.vue";
    import ResumePersonalContacts from "./ResumePersonalContacts/ResumePersonalContacts.vue";
    import ResumePersonalSkills from "./ResumePersonalSkills/ResumePersonalSkills.vue";
</script>