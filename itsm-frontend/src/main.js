import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import './main.css';

const app = createApp(App);

// Подключаем маршрутизатор
app.use(router);

app.mount("#app");
