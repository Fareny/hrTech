import axios from 'axios';

// P.s Охуеть какой казырный апи
const VUE_BASE_URL = 'https://julia.endless-summer.ru/api';

export async function login(credentials) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/authorization`, credentials, {
            withCredentials: true
        });
        return data
    } catch (error) {
        throw error.response.data;
    }
}

export async function registration(credentials) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/registration`, credentials, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function checkAuth() {
    try {
        const { data } = await axios.get(`${VUE_BASE_URL}/check-auth`, {
            withCredentials: true,
        });
        return data;
    } catch (error) {
        return error.response.data;
    }
}

export async function uploadFile(formData) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/upload-file`, formData, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}
export async function createMeet(meetingData) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/create-meeting`, {
            meetingData
        }, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        console.log(error);
    }
}

export async function blockUser(chatId) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/delete-chat`, {
            chatId
        }, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        console.log(error);
    }
}

export async function getMyProfile() {
    try {
        const { data } = await axios.get(`${VUE_BASE_URL}/get-profile`, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getChats() {
    try {
        const { data } = await axios.get(`${VUE_BASE_URL}/get-chats`, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getChatMessages(chatId) {
    try {
        const { data } = await axios.get(`${VUE_BASE_URL}/get-messages`, {
            params: {
                chatId: chatId
            },
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function profileUpdate(profile) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/profile-update`, profile, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        return error.response.data
    }
}

export async function updateProfileAvatar(formData) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/update-profile-avatar`, formData, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getUserNotifications() {
    try {
        const { data } = await axios.get(`${VUE_BASE_URL}/get-notifications`, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getFavouriteVacancies() {
    try {
        const { data } = await axios.get(`${VUE_BASE_URL}/get-favourites`, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getMyVacancies() {
    try {
        const { data } = await axios.get(`${VUE_BASE_URL}/get-my-vacancies`, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function createNewVacancy(info) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/create-vacancy`, info, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function removeFavouriteVacancy(vacancyId) {
    try {
        const { data } = await axios.post(`${VUE_BASE_URL}/remove-favourite`, {
            vacancyId
        }, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getResponses() {
    try {
        const { data } = await axios.get(`${VUE_BASE_URL}/get-responses`, {
            withCredentials: true
        });
        return data;
    } catch (error) {
        throw error.response.data;
    }
}