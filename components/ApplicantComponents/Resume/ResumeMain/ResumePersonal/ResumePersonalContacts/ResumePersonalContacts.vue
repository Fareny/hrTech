<template>
    <ResumePersonalItem
        @saveModal="saveModal"
        @closeModal="closeModal"
    >
        <template #title>
            Контакты
        </template>

        <template #info>
            <p>Телефон: <span v-html="setValue(data.contacts.phone)"/></p>
            <p>Telegram: <span v-html="setValue(data.contacts.tellegram, true, 'telegram')"/></p>
            <p>Почта: <span v-html="setValue(data.contacts.email, true, 'email')"/></p>
        </template>

        <template #edit>
            <div
                class="resume-personal__contacts"
            >
                <AppInput
                    id="0"
                    name="Телефон"
                    :value="data.contacts.phone"
                    @changeValue="(val) => dataEdit.phone = val.value"
                />
                <AppInput
                    id="1"
                    name="Телеграм"
                    :value="data.contacts.tellegram"
                    @changeValue="(val) => dataEdit.tellegram = val.value"
                />
                <AppInput
                    id="2"
                    name="Почта"
                    :value="data.contacts.email"
                    @changeValue="(val) => dataEdit.email = val.value"
                />
            </div>
        </template>
    </ResumePersonalItem>
</template>

<script setup>
    import './ResumePersonalContacts.scss'

    import AppInput from "~/components/AppInputs/Input/Input.vue";
    import ResumePersonalItem from "../ResumePersonalItem/ResumePersonalItem.vue";

    const resumeStore = useResumeStore()

    const data = ref(resumeStore.personalInfo)

    const dataEdit = ref()

    const resetDataEdit = () => {
        dataEdit.value = {
            phone: data.value.contacts.phone,
            tellegram: data.value.contacts.tellegram,
            email: data.value.contacts.email
        }
    }

    const getLinkElem = (typeLink, textLink) => {
        let link = ''

        switch (typeLink) {
            case 'telegram':
                if (textLink.startsWith('@')) {
                    link = `https://t.me/${textLink.slice(1)}`
                } else {
                    link = textLink
                }
                break;
            case 'email':
                link = `mailto:${textLink}`
                break;
            default:
                link = '#'
        }

        return `<a href="${link}" target="_blank">${textLink}</a>`
    }

    const setValue = (val, isLink = false, typeLink) => {
        const editVal = isLink ? getLinkElem(typeLink, val) : val

        return val !== '' ? editVal : '<span class="resume__main-empty">Не указано</span>'
    }

    const saveModal = () => {
        data.value.contacts.phone = dataEdit.value.phone
        data.value.contacts.tellegram = dataEdit.value.tellegram
        data.value.contacts.email = dataEdit.value.email
    }

    const closeModal = () => {
        resetDataEdit()
    }

    resetDataEdit()
</script>