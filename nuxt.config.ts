export default defineNuxtConfig({
    devtools: { enabled: true },
    ssr: true,
    modules: [
        '@pinia/nuxt',
        '@pinia-plugin-persistedstate/nuxt',
    ],
    vite: {
        define: {
            global: {},
            process: { env: {} }
        },
        resolve: {
            alias: {
                stream: 'stream-browserify',
                crypto: 'crypto-browserify'
            }
        }
    }
})
