<template>
  <section class="section__chat">
      <div class="chat__header" v-if="userInfo && chatId">
          <div class="chat__header_info">
              <div v-if="loading" class="chat__header_dot"></div>
              <img v-else class="chat__header_image" :src="userInfo.avatar" alt="User Avatar">
              <div>
                  <p class="chat__header_name">{{!loading ? userInfo.name : 'Загружаю ФИО...' }}</p>
                  <p class="chat__header_date">{{!loading ? userInfo.last_seen : 'Загружаю дату последнего общения...' }}</p>
              </div>
          </div>
          <ChatMessageActions v-if="!loading" :chatId="chatId" :userInfo="userInfo" />
      </div>

      <div class="chat__messages" :class="{ 'chat__messages_active': messages.length === 0 && chatId || !chatId || loading }">
          <div v-if="chatId && loading">
              <LoaderIcon class="chat__messages_loader" />
          </div>
          <div v-if="messages.length === 0 && chatId && !loading">
              <p class="chat__messages_text">Здесь пока ничего нет...</p>
          </div>
          <div v-if="!chatId">
              <p class="chat__messages_text">Выберите, кому хотели бы написать</p>
          </div>
          <div v-else class="chat__messages_wrapper" ref="chatMessagesContainerRef">
              <ul class="chat__messages_list">
                  <template v-for="(message, index) in messages" :key="message.id">
                        <li v-if="message.chatId === chatId"
                          class="chat__message"
                          :class="{ 'chat__message_me': message.user_name === userStore.email }"
                        >
                          <div class="chat__message_info" :class="{ 'chat__message_info_me': message.user_name === userStore.email }">
                              <p v-if="index === 0 || messages[index - 1].user_name !== message.user_name" class="chat__message_author">
                                  {{ message.user_name }}
                              </p>
                              <div class="chat__message_text_wrapper">
                                  <template v-if="message.image">
                                      <img class="chat__message_image" :src="message.image" alt="Message Image">
                                  </template>
                                  <template v-else-if="message.video">
                                      <video class="chat__message_video" controls>
                                          <source :src="message.video" type="video/mp4">
                                          Your browser does not support the video tag.
                                      </video>
                                  </template>
                                  <template v-else-if="message.file">
                                      <a :href="message.file" class="chat__message_file" download target="_blank">
                                          <MemoCheckIcon class="chat__message_file_icon" />
                                          Скачать файл
                                      </a>
                                  </template>
                                  <template v-else>
                                      <p v-if="message.type === 'conference'">
                                          Ссылка на конференцию <a :href="message.message" class="chat__message_file" target="_blank">{{ message.message }}</a>
                                      </p>
                                      <p v-else class="chat__message_text">{{ message.message }}</p>
                                  </template>
                                  <p class="chat__message_time" :class="{ 'chat__message_time_me': message.user_name === userStore.email }">
                                      {{ message.time.split(' ')[0] }}
                                  </p>
                              </div>
                          </div>
                      </li>
                  </template>
              </ul>
          </div>
      </div>

      <ChatControl :chatId="chatId" :loading="loading" :socket="socketService.socket" :chatMessagesContainerRef="chatMessagesContainerRef" />
  </section>
</template>

<script setup>
import './ChatMessageComponents.scss'
import { ref, watch, onMounted, onBeforeUnmount, nextTick, inject } from 'vue'
import { useRoute } from 'vue-router'
import { getChatMessages } from '~/http/http'
import { useUserStore } from '~/stores/userStore'
import ChatControl from '../ChatControl/ChatControl.vue'
import LoaderIcon from '~/components/AppIcons/Loader.vue'
import MemoCheckIcon from '~/components/AppIcons/MemoCheck.vue'
import ChatMessageActions from '../ChatMessageActions/ChatMessageActions.vue'
import socketService from '~/helpers/mainSocketConnection'

const route = useRoute()
const chatId = ref(route.query.chatId || null)
const userInfo = ref(null)
const chatMessagesContainerRef = ref(null)
const messages = inject('messages')
const loading = ref(true)

const userStore = useUserStore()

const loadMessages = async (id) => {
    try {
        loading.value = true
        const data = await getChatMessages(id)
        messages.value = data.messages
        userInfo.value = data.secondUser
        await nextTick()
    } catch (error) {
        console.error('Failed to load messages:', error)
    } finally {
        loading.value = false
    }
}

const scrollToBottom = () => {
    const chatMessagesContainer = chatMessagesContainerRef.value
    if (chatMessagesContainer) {
        chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight
    }
}

watch(messages, () => nextTick(scrollToBottom))

watch(() => route.query.chatId, async (newChatId) => {
    chatId.value = newChatId
    if (newChatId) {
        await loadMessages(newChatId)
        scrollToBottom()
    }
})

onMounted(async () => {
    if (chatId.value) {
        await loadMessages(chatId.value)
        scrollToBottom()
    }
    socketService.onEvent('newMessage', async (message) => {
        messages.value.push(message)
        await nextTick()
        scrollToBottom()
    });
})

onBeforeUnmount(() => {
    socketService.offEvent('newMessage');
})
</script>
