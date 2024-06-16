<template>
    <div class="tests-checkbox">
        <InputLabel v-if="props.name !== ''">
            {{ props.name }}
        </InputLabel>

        <div
            class="tests-checkbox__item"
            v-for="option in props.options"
            :key="option.value"
        >
            <AppCheckbox
                :id="option.value"
                :type="props.type"
                :itemName="`${props.id}_${props.type}`"
                :checked="props.type === 'checkbox' ? props.value.includes(option.value) : props.value === option.value"
                :blockSelectToLabel="false"
                :disabled="props.isNoAnswer"
                @changeValue="(val) => emit('changeValue', val)"
            >
            <span
                class="tests-checkbox__label"
                :contenteditable="props.isEdit"
                @input="(val) => emit('changeLabel', {id: option.value, value: val.target.innerText})"
                @click="(e) => props.isEdit ? e.preventDefault() : null"
            >
                {{ option.label }}
            </span>
            </AppCheckbox>

            <TrashIcon
                v-if="!props.isPagePassing"
                class="tests-checkbox__delete"
                @click.prevent="() => emit('deleteOption', {id: option.value, value: option.value})"
            />
        </div>

        <AppButton
            v-if="!props.isPagePassing"
            class="tests-checkbox__add button_clear"
            @click="emit('addFieldOption')"
        >
            +
        </AppButton>

        <span
            v-if="props.type === 'checkbox' && props.isModal && !props.isNoAnswer"
            class="tests-checkbox__note"
        >
            <b>Примечание:</b> пункты, которые вы выберите, будут являться правильными вариантами ответа на вопрос
        </span>
    </div>
</template>

<script setup>
    import './TestsCheckbox.scss'

    import TrashIcon from '~/components/AppIcons/Trash.vue';

    import AppCheckbox from "~/components/AppInputs/Checkbox/Checkbox.vue";
    import InputLabel from "~/components/AppInputs/InputLabel/InputLabel.vue";

    const props = defineProps({
        id: {
            type: [String, Number],
            default: 0
        },
        type: {
            type: String,
            default: 'checkbox'
        },
        value: {
            type: [String, Number, Array],
            default: null
        },
        options: {
            type: Array,
            default: []
        },
        name: {
            type: String,
            default: ''
        },
        isEdit: {
            type: Boolean,
            default: false
        },
        isNoAnswer: {
            type: Boolean,
            default: false
        },
        isModal: {
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