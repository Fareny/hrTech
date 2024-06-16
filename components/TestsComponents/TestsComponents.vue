<template>
    <AppSection class="tests">
        <div class="tests__header">
            <h2 class="tests__header-title">
                Тесты
                <span class="tests__header-title__number">{{ testsStore.tests.length }}</span>
            </h2>
            <AppButton
                class="tests__header-btn"
                :link="`${useRoute().fullPath}/create`"
            >
                Создать Тест
            </AppButton>
        </div>

        <TestsList :tests="testsStore.tests" />
    </AppSection>
</template>

<script setup>
    import './TestsComponents.scss'

    import TestsList from "./TestsList/TestsList.vue";

    const testsStore = useTestsStore()

    testsStore.getTests()
</script>