<template>
    <figure class="icon icon-loader">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M2 11h5v2H2zm15 0h5v2h-5zm-6 6h2v5h-2zm0-15h2v5h-2zM4.222 5.636l1.414-1.414 3.536 3.536-1.414 1.414zm15.556 12.728-1.414 1.414-3.536-3.536 1.414-1.414zm-12.02-3.536 1.414 1.414-3.536 3.536-1.414-1.414zm7.07-7.071 3.536-3.535 1.414 1.415-3.536 3.535z"/>
        </svg>
    </figure>
</template>

<script setup>

</script>

<style lang="scss">
    .icon-loader {
        svg {
            animation: {
                name: loaderAnimation;
                iteration-count: infinite;
                duration: 1s;
                timing-function: linear;
            }
        }
    }

    @keyframes loaderAnimation {
        0% {
            transform: rotate(0deg);
        }

        100% {
            transform: rotate(360deg);
        }
    }
</style>