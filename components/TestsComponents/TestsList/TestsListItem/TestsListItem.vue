<template>
    <li class="tests__list-item list-item">
        <div class="list-item__container">
            <h4 class="list-item__title">{{ props.test.name }}</h4>

            <div class="list-item__links">
                <NuxtLink :to="`/profile/tests/edit/${props.test.id}`" class="list-item__link">Редактировать</NuxtLink>
                <NuxtLink :to="`/tests/${props.test.id}`" class="list-item__link">Пройти</NuxtLink>
                <AppButton
                    class="list-item__link list-item__link_delete button_clear"
                    @click="deleteTest(props.test.id)"
                >
                    Удалить
                </AppButton>
            </div>

            <span class="list-item__percent">Процент прохождения: {{ props.test.passingPercentage }}%</span>
        </div>

        <span class="list-item__questions-count">Вопросов: {{ props.test.questions }}</span>

        <span class="list-item__date-created">дата создания: {{ props.test.dateCreated }}</span>
    </li>
</template>

<script setup>
    import './TestsListItem.scss'

    import {toast} from "vue3-toastify";

    const testsStore = useTestsStore()

    const props = defineProps({
        test: {
            default: {
                id: 0,
                name: 'Test',
                questionsCount: 54,
                passingPercentage: 33,
                dateCreated: '11.01.2023'
            },
            type: Object
        }
    })

    const deleteTest = (id) => {
        try {
            testsStore.deleteTest(id)

            setTimeout(() => {
                toast.success('Тест удален')
            }, 100)
        } catch (error) {
            toast.error(error.response.data)
        }
    }
</script>