<template>
    <AppModal
        @saveModal="saveModal"
    >
        <template #summary>
            Запланировать встречу
        </template>

        <template #title>
            Планирование встречи
        </template>

        <template #content>
            <div class="chat__modal">
                <div class="chat__modal_fields">
                    <div class="chat__modal_field">
                        <AppInput
                            name="Название встречи"
                            placeholder="Название..."
                            type="text"
                            :value="meetingTitle"
                            @changeValue="(val) => meetingTitle = val.value"/>
                    </div>
                    <div class="chat__modal_field">
                        <AppInput
                            name="Описание встречи"
                            placeholder="Описание..."
                            type="text"
                            :value="meetingDescription"
                            @changeValue="(val) => meetingDescription = val.value"/>
                    </div>
                </div>
                <div class="chat__modal_fields">
                    <div class="chat__modal_field">
                        <AppInput
                            name="Время начала"
                            placeholder="14:37"
                            type="text"
                            :maxlength="5"
                            :value="formattedTime"
                            @input="handleTimeInput"
                        />
                    </div>
                    <div class="chat__modal_field">
                        <AppInput
                            name="Дата начала"
                            type="date"
                            :value="meetingStartDate"
                            @changeValue="(val) => meetingStartDate = val.value"
                        />
                    </div>
                </div>
            </div>
        </template>
    </AppModal>
</template>

<script setup>
import './ChatModal.scss'
import {ref} from 'vue';
import AppModal from '~/components/AppModal/AppModal.vue';
import AppInput from '~/components/AppInputs/Input/Input.vue';
import {createMeet} from '~/http/http.js';
import {toast} from 'vue3-toastify';

const modalState = ref(false);

const meetingTitle = ref('');
const meetingDescription = ref('');
const meetingStartTime = ref('');
const meetingStartDate = ref('');

const formattedTime = ref('');

const props = defineProps({
    chatId: {
        default: null,
        type: String
    }
})

const saveModal = async () => {
    modalState.value = false;

    if (!meetingTitle.value || !meetingDescription.value || !meetingStartTime.value || !meetingStartDate.value) {
        toast.error('Необходимо заполнить все поля!');
        return
    }

    const meetingData = {
        chatId: props.chatId,
        title: meetingTitle.value,
        description: meetingDescription.value,
        startTime: meetingStartTime.value,
        startDate: meetingStartDate.value,
    };

    try {
        toast.info('Планирование встречи...');
        const data = await createMeet(meetingData);
        if (data.status === 'ok') {
            toast.success('Встреча запланирована!');
        } else {
            toast.error('Не удалось запланировать встречу!');
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
};

const handleTimeInput = (event) => {
    let val = event.target.value;
    val = val.replace(/\D/g, '');

    if (val.length > 2) {
        val = val.slice(0, 2) + ':' + val.slice(2);
    }

    formattedTime.value = val;
    meetingStartTime.value = val;
};
</script>
