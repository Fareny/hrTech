<template>
    <details class="dropdown" :open="props.startOpen">
        <summary class="dropdown__summary">
            <slot name="summary"></slot>
        </summary>

        <ul class="dropdown__content">
            <slot name="content"></slot>
        </ul>
    </details>
</template>

<script setup>
    import './AppDropdown.scss'

    const props = defineProps({
        startOpen: {
            default: false,
            type: Boolean
        }
    })
</script>