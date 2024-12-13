import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; // Подключение маршрутизатора
import "./assets/tailwind.css"; // Подключение TailwindCSS

createApp(App).use(router).mount("#app");
