import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { authStore } from "@/store/auth";
import "@fortawesome/fontawesome-free/css/all.css";

import "./main.css";

// Проверяем токен в localStorage
const token = localStorage.getItem("accessToken");
if (token) {
  authStore.setAuth(true, { username: "Пользователь" }); // Добавьте реальное имя пользователя
}

const app = createApp(App);
app.use(router);
app.mount("#app");
