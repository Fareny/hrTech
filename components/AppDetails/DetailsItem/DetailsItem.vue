<template>
    <li
        class="details__content-item"
        :class="{
            'details__content-item_active' : props.item.active,
            'details__content-item_no-clickable' : props.noClickable
        }"
        @click="selectItem" 
    >
        <slot></slot>
    </li>
</template>

<script setup>
    import './DetailsItem.scss'

    const props = defineProps({
        itemKey: {
            default: '',
            type: String
        },
        item: {
            default: {
                name: 'Не найдено',
                value: null
            },
            type: Object
        },
        noClickable: {
            default: false,
            type: Boolean
        }
    })

    const emit = defineEmits([
        'selectItem',
    ])

    const hideDetailForItem = inject('hideDetailForItem')

    const selectItem = () => {
        hideDetailForItem()
        emit('selectItem', { key: props.itemKey, value: props.item.value })
    }
</script>