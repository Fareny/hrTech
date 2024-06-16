<template>
    <div class="experience-edit__item edit-item">
        <div class="edit-item__month item-month">
            <AppSelect
                :id="0"
                name="Начало работы"
                :value="currentExperience.timeStart.month"
                :options="monthsOptions"
                @changeValue="(val) => currentExperience.timeStart.month = val.value"
            />

            <AppInput
                :value="currentExperience.timeStart.year"
                @changeValue="(val) => currentExperience.timeStart.year = val.value"
            />
        </div>

        <div class="edit-item__month item-month item-month_checkbox">
            <AppSelect
                :id="0"
                name="Окончание работы"
                :value="currentExperience.timeEnd.month"
                :options="monthsOptions"
                :disabled="currentExperience.timeEnd.now"
                @changeValue="(val) => currentExperience.timeEnd.month = val.value"
            />

            <AppInput
                :value="currentExperience.timeEnd.year"
                :disabled="currentExperience.timeEnd.now"
                @changeValue="(val) => currentExperience.timeEnd.year = val.value"
            />

            <span
                v-show="!validateTime"
                class="item-month__error"
            >
                Неккоректная дата
            </span>

            <AppCheckBox
                class="item-month__checkbox"
                :checked="currentExperience.timeEnd.now"
                @changeValue="(val) => currentExperience.timeEnd.now = val.value"
            >
                <span class="item-month__checkbox-text">По настоящее время</span>
            </AppCheckBox>
        </div>

        <AppInput
            name="Название организации"
            :value="currentExperience.companyInfo.name"
            @changeValue="(val) => currentExperience.companyInfo.name = val.value"
        />

        <AppInput
            name="Регион"
            :value="currentExperience.companyInfo.location"
            @changeValue="(val) => currentExperience.companyInfo.location = val.value"
        />

        <AppInput
            name="Сайт"
            :value="currentExperience.companyInfo.site"
            @changeValue="(val) => currentExperience.companyInfo.site = val.value"
        />

        <AppInput
            name="Должность"
            :value="currentExperience.positionName"
            @changeValue="(val) => currentExperience.positionName = val.value"
        />

        <AppTextarea
            name="Обязанности"
            resize="vertical"
            :value="currentExperience.responsibility"
            @changeValue="(val) => currentExperience.responsibility = val.value"
        />

    </div>
</template>

<script setup>
    import './ResumeExperienceListEditItem.scss'

    import monthsOptions from "~/data/monthsOptions.js";

    import AppSelect from "~/components/AppInputs/Select/Select.vue";
    import AppInput from "~/components/AppInputs/Input/Input.vue";
    import AppTextarea from "~/components/AppInputs/Textarea/Textarea.vue";
    import AppCheckBox from "~/components/AppInputs/Checkbox/Checkbox.vue";
    import AppCheckbox from "~/components/AppInputs/Checkbox/Checkbox.vue";

    const props = defineProps({
        experienceId: {
            default: 0,
            type: [Number, String]
        }
    })

    const experienceEdit = inject('experienceEdit')

    const currentExperience = computed(() => {
        return experienceEdit.value.find((item) => item.id === props.experienceId)
    })

    const validateTime = computed(() => {
        const timeStartYear = currentExperience.value.timeStart.year
        const timeEndYear = currentExperience.value.timeEnd.year

        const timeStartMonth = currentExperience.value.timeStart.month
        const timeEndMonth = currentExperience.value.timeEnd.month

        const validateAnswer = timeStartYear < timeEndYear || timeStartYear === timeEndYear &&
            timeStartMonth < timeEndMonth && timeStartMonth !== timeEndMonth

        currentExperience.value.validateTime = validateAnswer

        return validateAnswer
    })
</script>