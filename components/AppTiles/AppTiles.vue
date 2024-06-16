<template>
    <ul class="tiles">
        <Tile
            v-for="item in props.items"
            :item="item"
        >
            {{ item }}
        </Tile>
    </ul>
</template>

<script setup>
    import './AppTiles.scss'

    import Tile from "./Tile/Tile.vue";

    const props = defineProps({
        items: {
            default: [],
            type: Array
        }
    })
</script>