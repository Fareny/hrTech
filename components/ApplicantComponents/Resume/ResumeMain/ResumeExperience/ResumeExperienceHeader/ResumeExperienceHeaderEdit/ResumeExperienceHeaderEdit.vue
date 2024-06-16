<template>
    <ResumeEditItem
        :disableSave="validate"
        @saveModal="saveModal"
        @closeModal="resetResumeInfo"
    >
        <template #title>Редактирование</template>

        <template #content>
            <div class="experience-header__content">
                <AppInput
                    name="Желаемая должность"
                    :value="resumeInfoEdit.name"
                    @changeValue="(val) => resumeInfoEdit.name = val.value"
                />
                <AppInput
                    name="Желаемая зарплата"
                    :value="resumeInfoEdit.sallary"
                    @changeValue="(val) => resumeInfoEdit.sallary = val.value"
                />
                <AppSelect
                    :id="resumeInfoEdit.conditions[0].id"
                    name="Тип занятости"
                    :value="resumeInfoEdit.conditions[0].value"
                    :options="resumeInfoEdit.conditions[0].options"
                    :isMultiple="true"
                    :isFiltered="true"
                    @changeValue="(val) => resumeInfoEdit.conditions[0].value = val.value"
                />
                <AppSelect
                    :id="resumeInfoEdit.conditions[1].id"
                    name="График работы"
                    :value="resumeInfoEdit.conditions[1].value"
                    :options="resumeInfoEdit.conditions[1].options"
                    :isMultiple="true"
                    :isFiltered="true"
                    @changeValue="(val) => resumeInfoEdit.conditions[1].value = val.value"
                />
            </div>
        </template>
    </ResumeEditItem>
</template>

<script setup>
    import './ResumeExperienceHeaderEdit.scss'

    import AppSelect from "~/components/AppInputs/Select/Select.vue";
    import AppInput from "~/components/AppInputs/Input/Input.vue";
    import ResumeEditItem from "~/components/ApplicantComponents/Resume/ResumeEditItem/ResumeEditItem.vue";

    const resumeStore = useResumeStore()

    const validate = ref(false)

    const resumeInfoEdit = ref()

    const resetResumeInfo = () => {
        resumeInfoEdit.value = JSON.parse(JSON.stringify(resumeStore.resumeInfo))
    }

    const saveModal = () => {
        resumeStore.resumeInfo = JSON.parse(JSON.stringify(resumeInfoEdit.value))
    }

    resetResumeInfo()
</script>