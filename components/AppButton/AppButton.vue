<template>
    <button
        class="button"
        :class="{'button_loader': props.loader}"
        :disabled="props.disabled"
    >
        <NuxtLink v-if="props.link" :to="props.link" class="button__content">
            <slot></slot>
        </NuxtLink>

        <span
            v-else
            class="button__content">
            <slot></slot>
        </span>

        <LoaderIcon v-show="props.loader" class="button__loader" />
    </button>
</template>

<script setup>
    import './AppButton.scss'

    import LoaderIcon from '~/components/AppIcons/Loader.vue';

    const props = defineProps({
        disabled: {
            default: false,
            type: Boolean
        },
        loader: {
            default: false,
            type: Boolean
        },
        link: {
            default: null,
            type: String
        }
    })
</script>