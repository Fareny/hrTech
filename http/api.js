import axios from "axios";

// P.s Охуеть какой казырный апи
const VUE_BASE_URL = 'https://julia.endless-summer.ru/api';

export default {
    async get(url, params = {}, options = {}) {
        try {
            const { data } = await axios.get(`${VUE_BASE_URL}/${url}`, {
                withCredentials: true,
                ...options,
                params
            });

            return data;
        } catch (error) {
            throw error.response.data;
        }
    },

    async post(url, body = {}, options = {}) {
        try {
            const { data } = await axios.post(`${VUE_BASE_URL}/${url}`, body, {
                withCredentials: true,
                ...options,
            });

            return data;
        } catch (error) {
            throw error.response.data;
        }
    }
}