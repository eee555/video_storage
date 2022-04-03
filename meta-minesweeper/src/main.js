import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'
// import VueResource from 'vue-resource'


createApp(App).use(router).use(naive).mount('#app')
