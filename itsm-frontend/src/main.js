import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; // Импорт маршрутизатора

import "./main.css"; // Подключение Tailwind CSS

const app = createApp(App);

app.use(router); // Подключение маршрутизатора
app.mount("#app");
