<template>
  <AppSection class="section__hub">
    <ChatUsersComponents :lastMessageChats="lastMessageChats" :messages="messages" :users="users" />
    <ChatMessageComponents />
  </AppSection>
</template>

<script setup>
  import './ChatComponents.scss'
  import AppSection from '~/components/AppSection/AppSection.vue'
  import ChatUsersComponents from './ChatUsersComponents/ChatUsersComponents.vue'
  import ChatMessageComponents from './ChatMessageComponents/ChatMessageComponents.vue'
  import { getChats } from '~/http/http.js'

  import { onMounted, watch, ref, provide } from 'vue'

  const users = ref([]);
  const loading = ref(true);
  const messages = ref([]);
  const lastMessageChats = ref([]);

  onMounted(() => {
    const getChatsInfo = async () => {
      loading.value = true;
      const data = await getChats();
      users.value = data;
      loading.value = false;
    }

    getChatsInfo();
  });

  watch(() => messages.value, () => {
    const lastMessage = messages.value[messages.value.length - 1];
    if (lastMessage?.chatId) {
      const existingIndex = lastMessageChats.value.findIndex(chat => chat.chatId === lastMessage.chatId);
      if (existingIndex !== -1) {
        lastMessageChats.value.splice(existingIndex, 1);
      }
      lastMessageChats.value.push({
        chatId: lastMessage.chatId,
        lastMessage:  lastMessage.image && 'Новое изображение' || 
                      lastMessage.video && 'Новый видео файл' || 
                      lastMessage.file && 'Новый файл' || 
                      lastMessage.message 
      });
    }
  }, { deep: true })

  provide('messages', messages);
  provide('users', users);
</script>
