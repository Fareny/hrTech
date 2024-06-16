<template>
    <div class="chat__control" v-if="chatId && !loading">
      <div class="chat__control_input">
        <LoaderIcon v-if="fileLoading" class="chat__icon" :class="{ 'chat__messages_loader': fileLoading }" />
        <PaperClipIcon v-else class="chat__icon" @click="triggerFileInput" />
        <input type="file" ref="fileInputRef" @change="handleFileUpload" style="display: none;" multiple />
        <div
          ref="chatInputRef"
          class="chat__input"
          :class="{ 'chat__input_filled': text.length > 0 }"
          contenteditable="true"
          @input="handleInput"
          @keydown.enter="handleKeyDown"
        ></div>
      </div>
      <AppButton class="chat__button" @click="sendMessage(chatId, text)">
        Отправить
      </AppButton>
    </div>
</template>

<script setup>
    import './ChatControl.scss'
    import AppButton from '~/components/AppButton/AppButton.vue'
    import PaperClipIcon from '~/components/AppIcons/PaperClip.vue'
    import LoaderIcon from '~/components/AppIcons/Loader.vue'

    import { inject, ref } from 'vue'
    import { uploadFile } from '~/http/http'

    const fileLoading = ref(false);
    const fileInputRef = ref(null);
    const text = ref('');
    const chatInputRef = ref(null);

    const messages = inject('messages');

    const props = defineProps({
        chatId: {
            type: String,
            default: null
        },
        loading: {
            type: Boolean,
            default: false
        },
        socket: {
            type: Object,
            default: null
        },
        chatMessagesContainerRef: {
            type: Object,
            default: null
        }
    })

    const userStore = useUserStore();

    const handleKeyDown = (event) => {
        if (event.key === 'Enter' && !event.shiftKey && !fileLoading.value) {
            event.preventDefault();
            sendMessage(props.chatId, text.value);
        }
    }

    const handleInput = (event) => {
    text.value = event.target.innerText;
    }

    const triggerFileInput = () => {
    fileInputRef.value.click();
    }

    const handleFileUpload = async (event) => {

    if(props.chatId === 'special') return

    const files = event.target.files;
    for (let file of files) {
        fileLoading.value = true;
        const formData = new FormData();
        formData.append('file', file);
        formData.append('chatId', props.chatId);
        formData.append('user_name', userStore.email);

        const data = await uploadFile(formData);

        const now = new Date();
        const timeString = now.toLocaleTimeString('ru-RU', {
            hour: '2-digit',
            minute: '2-digit',
        });
        const dateString = now.toLocaleDateString('ru-RU', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
        });
        const timestamp = `${timeString} ${dateString}`;

        let message = {
            user_name: userStore.email,
            chatId: props.chatId,
            time: timestamp,
        };

        const fileType = file.type.split('/')[0];
        if (fileType === 'image') {
            message.image = data.link;
        } else if (fileType === 'video') {
            message.video = data.link;
        } else {
            message.file = data.link;
        }

        fileLoading.value = false;
        messages.value.push(message);
        props.socket.emit('sendMessage', message);
        await nextTick();
        scrollToBottom();
    }
        fileInputRef.value.value = '';
    }

    const scrollToBottom = () => {
        const chatMessagesContainer = props.chatMessagesContainerRef;
        if (chatMessagesContainer) {
            chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight
        }
    }

    const sendMessage = async (chatId, thisText) => {
    if (thisText.trim() !== '' && !fileLoading.value && chatId !== 'special') {
        const now = new Date();
        const timeString = now.toLocaleTimeString('ru-RU', {
            hour: '2-digit',
            minute: '2-digit',
        });
        const dateString = now.toLocaleDateString('ru-RU', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
        });
        const timestamp = `${timeString} ${dateString}`;

        const message = {
        user_name: userStore.email,
        chatId,
        message: thisText,
        time: timestamp,
        };
        messages.value.push(message);
        props.socket.emit('sendMessage', message);
        text.value = '';
        chatInputRef.value.textContent = ''
        
        await nextTick()
        scrollToBottom();
    }
}

</script>