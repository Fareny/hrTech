<template>
    <component
        :is="scripts.getFieldComponent(props.field.type)"
        :id="props.field.id"
        :type="props.field.type"
        :value="props.isPagePassing ? props.field.type === 'checkbox' && props.field.type === 'radio' ? [] : '' : props.field.value"
        :options="props.field.options"
        :required="props.field.required"
        :placeholder="props.field.placeholder"
        :isEdit="props.isEdit"
        :isPagePassing="props.isPagePassing"
        @changeValue="(val) => emit('changeValue', val)"
        @changeLabel="(val) => emit('changeLabel', val)"
        @deleteOption="(val) => emit('deleteOption', val)"
        @addFieldOption="() => emit('addFieldOption')"
    />
</template>

<script setup>
    import './TestPageComponent.scss'

    import scripts from "~/components/TestsComponents/scripts.js";

    const props = defineProps({
        field: {
            type: Object,
            default: {
                id: 0,
                isNoAnswer: false,
                name: 'Test',
                options: [
                    {
                        label: 'test',
                        value: '0_0'
                    }
                ],
                required: false,
                type: 'text',
                value: '',
            }
        },
        isEdit: {
            type: Boolean,
            default: false
        },
        isPagePassing: {
            type: Boolean,
            default: false
        }
    })

    const emit = defineEmits(['changeValue', 'changeLabel', 'deleteOption', 'addFieldOption'])
</script>