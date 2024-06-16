<template>
    <AppSection>
        <div>
            <h2 class="negotiation-title">Отклики и приглашения</h2>
            <table class="negotiation-table" v-if="negotiation.length">
                <thead>
                    <tr>
                        <th>Статус</th>
                        <th>Вакансия</th>
                        <th>Дата</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in negotiation" :key="item.id">
                        <td :class="{
                        'status-red': item.status === 'Отказ', 
                        'status-grey': item.status === 'Резюме не просмотрено',
                        'status-green': item.status === 'Приглашен'
                        }">{{ item.status }}</td>
                        <td class="negotiation-table__vacancy">{{ item.vacancy }}</td>
                        <td>{{ item.date }}</td>
                    </tr>
                </tbody>
            </table>
            <p v-else class="favourites__empty">У вас нет откликов и приглашений</p>
        </div>
    </AppSection>
</template>

<script setup>
    import './NegotiationComponents.scss'
    import { onMounted, ref } from "vue";
    import AppSection from "~/components/AppSection/AppSection.vue";

    const negotiation = ref([
        { id: 1, status: 'Приглашен', vacancy: 'React front-end developer в Перфоманс Лаб', date: '5 декабря 2023' },
        { id: 2, status: 'Отказ', vacancy: 'Frontend developer (react) в Лига Ставок', date: '4 декабря 2023' },
        { id: 3, status: 'Резюме не просмотрено', vacancy: 'Разработчик сайтов (стажер) в Представительство Правительства Ярославской области', date: '2 декабря 2023' },
        { id: 4, status: 'Отказ', vacancy: 'Frontend-разработчик в Сбер. IT', date: '28 ноября 2023' }
    ]);

    onMounted(() => {
        const getNegotiationInfo = async () => {
            // Placeholder for future server request
            console.log(negotiation.value);
        }

        getNegotiationInfo();
    });
</script>
