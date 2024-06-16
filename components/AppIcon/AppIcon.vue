<template>
    <figure
        class="icon"
        :style="`
            width: ${props.width}px;
            height: ${props.height}px;
            --color: ${props.color};
        `"
    >
        <component :is="props.iconComponent" />
    </figure>
</template>

<script setup>
    import './AppIcon.scss'

    const props = defineProps({
        iconComponent: {
            default: {},
            type: Function,
            required: true
        },
        width: {
            default: "24",
            type: String
        },
        height: {
            default: "24",
            type: String
        },
        color: {
            default: '#1F2D3D',
            type: String
        }
    })
</script>
