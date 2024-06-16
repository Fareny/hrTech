<template>
    <div class="input">
        <InputLabel
            v-if="(props.status || props.mask === '') && props.name !== ''"
        >
            {{ props.name }}
        </InputLabel>

        <input
            v-if="props.status || props.mask === ''"
            ref="inputRef"
            class="input__input"
            :type="props.type"
            :value="props.value"
            :required="props.required"
            :placeholder="props.placeholder"
            :autocomplete="props.enabledAutocomplete"
            :maxlength="props.maxlength"
            :disabled="props.disabled"
            :accept="props.accept"
            @input="(val) => emit('changeValue', {id: props.id, value: val.target.value})"

        />

        <InputMask v-else>
            {{ props.mask }}
        </InputMask>

        <slot></slot>
    </div>
</template>

<script setup>
    import './Input.scss';

    import InputMask from './InputMask/InputMask.vue';
    import InputLabel from "../InputLabel/InputLabel.vue";

    const props = defineProps({
        id: {
            type: [String, Number],
            default: 0
        },
        name: {
            type: String,
            default: ''
        },
        value: {
            type: [String, Number],
            default: ''
        },
        type: {
            type: String,
            default: 'text'
        },
        required: {
            type: Boolean,
            default: false
        },
        placeholder: {
            type: String,
            default: ''
        },
        disabled: {
            type: Boolean,
            default: false
        },
        mask: {
            type: String,
            default: ''
        },
        status: {
            type: Boolean,
            default: true
        },
        enabledAutocomplete: {
            type: Boolean,
            default: false
        },
        maxlength: {
            type: Number,
            default: 10000
        },
        accept: {
            type: String,
            default: ''
        }
    });

    const emit = defineEmits(['changeValue'])

    const inputRef = ref(null)

    defineExpose({
        inputRef
    })
</script>