import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'
// import VueResource from 'vue-resource'


let app = createApp(App);
app.use(router).use(naive).mount('#app');
// app.component(
//     () => {import * as ms from "ms-toollib"}
// )
