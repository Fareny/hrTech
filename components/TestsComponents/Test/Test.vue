<template>
    <AppSection class="test">
        <TestPage
            :test="test"
            :isEdit="false"
            :isCreateFields="false"
            :isPagePassing="true"
            @buttonAction="checkAnswers"
        />
    </AppSection>
</template>

<script setup>
    import './Test.scss'

    import TestPage from "~/components/TestsComponents/TestPage/TestPage.vue";
    import {toast} from "vue3-toastify";

    const testsStore = useTestsStore()
    const userStore = useUserStore()

    const router = useRouter()
    const route = useRoute()

    const test = ref(JSON.parse(JSON.stringify(testsStore.getTest(route.params.id) ?? [])))

    const checkAnswers = async () => {
        try {
            const answers = testsStore.checkAnswers(test.value)
            const data = await testsStore.saveAnswers(test.value, answers, userStore.email)

            setTimeout(() => {
                router.push('/chats?chatId=' + data.chat_id)
            }, 100)

            setTimeout(() => {
                toast.success('Ответы сохранены и отправлены')
            }, 200)
        } catch (error) {
            toast.error(error.response.data)
        }
    }
</script>