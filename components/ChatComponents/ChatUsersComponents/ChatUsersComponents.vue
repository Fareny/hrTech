<template>
  <ul class="chat__users">
    <li class="chat__user" v-for="user in users" :key="user.chatId" @click="selectChat(user.chatId)">
      <div class="chat__user_image_wrapper">
        <img class="chat__users_image" :class="{ 'chat__users_image_active': user.chatId === route.query.chatId }" :src="user.avatar" alt="">
        <div v-if="user.chatId === route.query.chatId" class="chat__users_dot"></div>
      </div>
      <div class="chat__user_info_wrapper">
        <div class="chat__user_info">
          <p class="chat__user_name">{{ user.name }}</p>
          <p class="chat__user_date">{{ user.lastDate }}</p>
        </div>
        <div>
          <p class="chat__user_last_message">{{ checkLastMessage(user) }}</p>
        </div>
      </div>
    </li>
  </ul>
</template>

<script setup>
import './ChatUsersComponents.scss'
import { useRouter } from 'vue-router'

const router = useRouter();
const route = useRoute();

const props = defineProps({
  users: {
    default: [],
    type: Array
  },
  messages: {
    default: [],
    type: Array
  },
  lastMessageChats: {
    default: [],
    type: Array
  }
})

const checkLastMessage = (user) => {
  if (props.lastMessageChats.find(el => el.chatId === user.chatId)) {
    return props.lastMessageChats.find(el => el.chatId === user.chatId).lastMessage
  } else {
    return user.lastMessage
  }
}

const selectChat = (chatId) => {
  router.push({ path: '/chats', query: { chatId } })
}

</script>
