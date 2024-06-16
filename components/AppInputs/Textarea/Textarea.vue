<template>
    <div class="textarea">
        <InputLabel
            v-if="props.name !== ''"
        >
            {{ props.name }}
        </InputLabel>
  
        <textarea
            class="textarea__input"
            :id="props.id"
            :value="props.value"
            :placeholder="props.placeholder"
            :style="`resize: ${props.resize}`"
            @input="(val) => emit('changeValue', {id: props.id, value: val.target.value})"
        />
    </div>
</template>

<script setup>
    import './Textarea.scss'

    import InputLabel from "~/components/AppInputs/InputLabel/InputLabel.vue";

    const props = defineProps({
        id: {
            default: 0,
            type: [String, Number]
        },
        name: {
            default: '',
            type: String
        },
        value: {
            default: '',
            type: String
        },
        placeholder: {
            default: '',
            type: String
        },
        resize: {
            default: 'none',
            type: String
        }
    })

    const emit = defineEmits(['changeValue'])
</script>