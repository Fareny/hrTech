<template>
    <div class="resume-experience__header experience-header">
        <div class="experience-header__title">
            <h4 class="experience-header__title-text">{{ props.resumeInfo.name }}</h4>
            <ResumeExperienceHeaderEdit />
        </div>
        <span class="experience-header__sallary">
            {{ props.resumeInfo.sallary }} {{ props.resumeInfo.currencySymbol }}
        </span>
        <div class="experience-header__conditions">
            <ResumeExperienceHeaderItem
                v-for="condition in props.resumeInfo.conditions"
                :key="condition.id"
                class="experience-header__condition header-condition"
                :condition="condition"
            />
        </div>
    </div>
</template>

<script setup>
    import './ResumeExperienceHeader.scss'

    import ResumeExperienceHeaderItem from "./ResumeExperienceHeaderItem/ResumeExperienceHeaderItem.vue";
    import ResumeExperienceHeaderEdit from "./ResumeExperienceHeaderEdit/ResumeExperienceHeaderEdit.vue";

    const props = defineProps({
        resumeInfo: {
            default: {},
            type: Object
        }
    })

</script>