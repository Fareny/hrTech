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
    import api from '~/http/api'

    const negotiation = ref([]);

    onMounted(() => {
        const getNegotiationInfo = async () => {
            const data = await api.get('negotiations');
            negotiation.value = data.responses
        }

        getNegotiationInfo();
    });
</script>
