<template>
     <AppDetails v-if="chatId !== 'special' && userStore.recruiter" class="vacancy__details">
            <template #summary>
              <DotsIcon class="chat__header_dots" />
            </template>

            <template #content>
                <DetailsItem v-if="userStore.recruiter"
                    :item="{
                        name: 'Запланировать встречу',
                        value: 'add'
                    }"
                    @selectItem="selectOption"
                >
                  <ChatModal :chatId="chatId" />
                </DetailsItem>
            </template>
      </AppDetails>
</template>

<script setup>
import './ChatMessageActions.scss'

import AppDetails from '~/components/AppDetails/AppDetails.vue'
import ChatModal from '~/components/ChatComponents/ChatModal/ChatModal.vue'
import DetailsItem from '~/components/AppDetails/DetailsItem/DetailsItem.vue'
import DotsIcon from '~/components/AppIcons/Dots.vue'

const userStore = useUserStore();

const props = defineProps({
  chatId: {
    default: null,
    type: String
  },
  userInfo: {
    default: null
  }
})

</script>