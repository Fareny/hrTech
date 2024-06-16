<template>
    <details
        ref="detailsRef"
        class="details"
        v-click-out-side="hideDetails"
        @click="openDetails"
    >
        <summary class="details__summary">
            <slot name="summary"></slot>
        </summary>

        <ul class="details__content">
            <LoaderIcon v-if="props.loader" class="details__content-loader" />
            <slot name="content" v-else></slot>
        </ul>
    </details>
</template>

<script setup>
    import './AppDetails.scss'

    import { clickOutSide as vClickOutSide } from '@mahdikhashan/vue3-click-outside'
    import DetailsScripts from "~/components/AppDetails/DetailsScripts.js";

    import LoaderIcon from '~/components/AppIcons/Loader.vue';

    const props = defineProps({
        closeByClick: {
            default: false,
            type: Boolean
        },
        disabled: {
            default: false,
            type: Boolean
        },
        loader: {
            default: false,
            type: Boolean
        }
    })

    const detailsRef = ref(null)

    const hideDetails = () => detailsRef.value.open = false

    const hideDetailForItem = () => props.closeByClick ? hideDetails() : null

    const openDetails = (event) => {
        if (props.disabled) event.preventDefault()

        if (!detailsRef.value.open) {
            DetailsScripts.setDetailsPosition(detailsRef.value)
        } else {
            detailsRef.value.classList.remove('details_top')
            detailsRef.value.classList.remove('details_left')
        }
    }

    provide('hideDetailForItem', hideDetailForItem)

    defineExpose({
        detailsRef
    })

</script>