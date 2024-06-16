<template>
    <div class="checkbox">
        <input
            class="checkbox__input"
            :id="props.id"
            :type="props.type"
            :name="props.itemName"
            :checked="props.checked"
            :disabled="props.disabled"
            @change="emit('changeValue', {id: props.id, value: $event.target.checked})"
        >

        <label :for="props.id" class="checkbox__label">
            <slot></slot>
        </label>
    </div>
</template>

<script setup>
    import './Checkbox.scss'

    const props = defineProps({
        id: {
            default: 0,
            type: [String, Number]
        },
        type: {
            default: 'checkbox',
            validator(value) {
                return ['checkbox', 'radio'].includes(value)
            }
        },
        itemName: {
            default: '0_checkbox',
            type: String
        },
        checked: {
            default: false,
            type: Boolean
        },
        disabled: {
            default: false,
            type: Boolean
        }
    })

    const emit = defineEmits(['changeValue'])
</script>
