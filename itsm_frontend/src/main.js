import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { authStore } from "@/store/auth";
import "@fortawesome/fontawesome-free/css/all.css";
import axios from "axios";
import { API_URL } from "@/config.js";

import "./main.css";

const token = localStorage.getItem("accessToken");

if (token) {
  axios
    .get(`${API_URL}/api/auth/validate-token/`, {
      headers: { Authorization: `Bearer ${token}` },
    })
    .then((response) => {
      authStore.setAuth(true, response.data.user);
    })
    .catch(() => {
      authStore.logout();
    });
}

createApp(App).use(router).mount("#app");

const app = createApp(App);
app.use(router);
app.mount("#app");
