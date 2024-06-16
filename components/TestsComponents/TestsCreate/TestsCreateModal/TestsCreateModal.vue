<template>
    <AppModal
        :disableSave="disableSave"
        @saveModal="saveModal"
        @closeModal="closeModal"
    >
        <template #summary>
            <AppButton>Добавить вопрос</AppButton>
        </template>

        <template #title>
            Создать вопрос
        </template>

        <template #content>
            <div class="tests-create__modal">
                <AppSelect
                    id="question-type"
                    name="Тип вопроса"
                    :value="field.type"
                    :options="types"
                    @changeValue="(val) => changeType(val)"
                />

                <AppCheckbox
                    id="required"
                    :value="field.required"
                    @changeValue="(val) => field.required = val.value"
                >
                    Обязательный вопрос
                </AppCheckbox>

                <AppCheckbox
                    v-if="field.type === 'checkbox' || field.type === 'radio'"
                    id="no-answer"
                    @changeValue="(val) => field.isNoAnswer = val.value"
                >
                    Без правильного ответа
                </AppCheckbox>

                <AppTextarea
                    id="question-text"
                    name="Текст вопроса"
                    :value="field.name"
                    @changeValue="(val) => field.name = val.value"
                />

                <component
                    v-if="field.type !== 'text' && field.type !== 'textarea'"
                    :is="fieldComponent"
                    :id="field.id"
                    name="Варианты выбора"
                    :type="field.type"
                    :value="field.value"
                    :options="field.options"
                    :required="field.required"
                    :placeholder="field.placeholder"
                    :isEdit="true"
                    :isAnswer="field.isNoAnswer"
                    :isModal="true"
                    @changeValue="(val) => emit('changeValue', field, val)"
                    @changeLabel="(val) => emit('changeLabel', field, val)"
                    @deleteOption="(val) => emit('deleteOption', field, val)"
                    @addFieldOption="() => emit('addFieldOption', field)"
                />
            </div>
        </template>
    </AppModal>
</template>

<script setup>
    import './TestsCreateModal.scss'

    import types from "~/data/types.js";

    import scripts from "~/components/TestsComponents/scripts.js";

    import AppModal from "~/components/AppModal/AppModal.vue";
    import AppSelect from "~/components/AppInputs/Select/Select.vue";
    import AppTextarea from "~/components/AppInputs/Textarea/Textarea.vue";
    import AppCheckbox from "~/components/AppInputs/Checkbox/Checkbox.vue";

    const props = defineProps({
        test: {
            type: Object,
            default: {}
        }
    })

    const emit = defineEmits(['saveModal', 'changeValue', 'changeLabel', 'deleteOption', 'addFieldOption'])

    const disableSave = ref(false)

    const field = ref({})

    const setDeafaultField = () => {
        const id = scripts.generateFieldId(props.test.fields)

        field.value = {
            id: id,
            name: 'Test',
            type: 'text',
            value: '',
            options: [{
                label: 'test',
                value: `${id}_0`
            }],
            required: false,
            isNoAnswer: false
        }
    }

    const fieldComponent = computed(() => {
        return scripts.getFieldComponent(field.value.type)
    })

    const changeType = (val) => {
        field.value.type = val.value
        if (field.value.type === 'checkbox') {
            field.value.value = []
        } else {
            field.value.value = ''
        }
    }

    const saveModal = () => {
        emit('saveModal', field.value)
        setDeafaultField()
    }

    const closeModal = () => setDeafaultField()

    setDeafaultField()

</script>