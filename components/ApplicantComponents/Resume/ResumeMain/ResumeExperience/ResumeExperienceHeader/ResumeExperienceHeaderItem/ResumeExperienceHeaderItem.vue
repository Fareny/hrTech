<template>
    <p class="header-condition__item">
        {{ props.condition.name }}: {{ conditionValues }}
    </p>
</template>

<script setup>
    import './ResumeExperienceHeaderItem.scss'

    const props = defineProps({
        condition: {
            default: {},
            type: Object
        }
    })

    const conditionValues = computed(() => {
        const { value, options } = props.condition;

        const filteredOptions = options.filter(option => value.includes(option.value));

        return filteredOptions.map(option => option.label).join(', ')
    })
</script>