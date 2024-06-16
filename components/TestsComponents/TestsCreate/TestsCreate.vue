<template>
    <AppSection class="tests-create">
        <TestPage
            :test="test"
            :isEdit="true"
            :isCreateFields="true"
            @buttonAction="createTest"
        />
    </AppSection>
</template>

<script setup>
    import './TestsCreate.scss'

    import commonScripts from "~/helpers/commonScripts.js";

    import TestPage from "~/components/TestsComponents/TestPage/TestPage.vue";
    import {toast} from "vue3-toastify";

    const testsStore = useTestsStore()
    const router = useRouter()

    const test = ref({
        id: testsStore.tests.length > 0 ? Math.max(...testsStore.tests.map(el => +String(el.id).slice(-1))) + 1 : 0,
        name: 'Название теста',
        questions: 0,
        passingPercentage: 0,
        dateCreated: commonScripts.formatDate(new Date()),
        fields: []
    })

    const createTest = () => {
        test.value.questions = test.value.fields.length

        try {
            testsStore.createTest(test.value)
            router.replace('/profile/tests')

            setTimeout(() => {
                toast.success('Тест создан')
            }, 100)
        } catch (error) {
            toast.error(error.response.data)
        }
    }
</script>