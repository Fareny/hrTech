<template>
    <ResumePersonalItem
        @saveModal="saveModal"
        @closeModal="closeModal"
    >
        <template #title>
            Ключевые навыки
        </template>

        <template #info>
            <AppTiles
                v-if="tilesItems.length > 0"
                :items="tilesItems"
            />

            <span v-else class="resume__main-empty">Нет указано</span>
        </template>

        <template #edit>
            <AppSelect
                :id="dataEdit.id"
                name="Ключевые навыки"
                :value="dataEdit.value"
                :options="dataEdit.options"
                :isMultiple="true"
                :isFiltered="true"
                @changeValue="(val) => dataEdit.value = val.value"
            />
        </template>
    </ResumePersonalItem>
</template>

<script setup>
    import './ResumePersonalSkills.scss'

    import ResumePersonalItem from "../ResumePersonalItem/ResumePersonalItem.vue";
    import AppSelect from "~/components/AppInputs/Select/Select.vue";

    const resumeStore = useResumeStore()

    const data = ref(resumeStore.personalInfo)
    const dataEdit = ref(Object.assign({}, data.value.skills))

    const tilesItems = computed(() => {
        if (data.value.skills.value === null) return []

        return data.value.skills.value.map(val => {
            const option = data.value.skills.options.find(opt => opt.value === val);
            return option ? option.label : null;
        });
    })

    const closeModal = () => {
        dataEdit.value = Object.assign({}, data.value.skills)
    }

    const saveModal = () => {
        data.value.skills.value = dataEdit.value.value
    }
</script>