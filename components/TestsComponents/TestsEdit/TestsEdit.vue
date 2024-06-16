<template>
    <AppSection class="test-edit">
        <TestPage
            v-if="test"
            :test="test"
            :isEdit="true"
            :isCreateFields="true"
            @buttonAction="updateTest"
        />
    </AppSection>
</template>

<script setup>
    import './TestsEdit.scss'

    import TestPage from "~/components/TestsComponents/TestPage/TestPage.vue";
    import {toast} from "vue3-toastify";

    const testsStore = useTestsStore()

    const router = useRouter()
    const route = useRoute()

    const test = ref(JSON.parse(JSON.stringify(testsStore.getTest(route.params.id) ?? null)))

    const updateTest = () => {
        try {
            testsStore.updateTest(test.value)
            router.back()

            setTimeout(() => {
                toast.success('Тест изменен')
            }, 100)
        } catch (error) {
            toast.error(error.response.data)
        }
    }
</script>