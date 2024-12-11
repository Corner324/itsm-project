<template>
  <div class="p-6 max-w-4xl mx-auto bg-white rounded shadow-md">
    <h1 class="text-3xl font-bold mb-6">Чаты с сотрудниками</h1>
    <div class="grid grid-cols-3 gap-4">
      <!-- Список пользователей -->
      <div class="border p-4 rounded bg-gray-50 shadow">
        <h2 class="font-medium text-lg mb-2">Список сотрудников</h2>
        <ul>
          <li
            v-for="user in users"
            :key="user.id"
            @click="selectUser(user)"
            class="cursor-pointer p-2 hover:bg-gray-200 rounded"
            :class="{ 'bg-blue-100': selectedUser?.id === user.id }"
          >
            {{ user.username }}
          </li>
        </ul>
      </div>
      <!-- Сообщения -->
      <div class="col-span-2 border p-4 rounded bg-gray-50 shadow">
        <h2 class="font-medium text-lg mb-2">
          Чат с {{ selectedUser?.username || "выберите сотрудника" }}
        </h2>
        <div v-if="selectedUser">
          <div v-for="message in messages" :key="message.id" class="mb-2">
            <div
              class="p-2 rounded"
              :class="message.sender === currentUser.id ? 'bg-blue-100' : 'bg-gray-100'"
            >
              <p>{{ message.content }}</p>
              <small class="text-gray-500">{{ formatDate(message.created_at) }}</small>
            </div>
          </div>
          <textarea
            v-model="newMessage"
            rows="2"
            class="mt-4 block w-full border-gray-300 rounded-md shadow-sm"
            placeholder="Введите сообщение..."
          ></textarea>
          <button
            @click="sendMessage"
            class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
          >
            Отправить
          </button>
        </div>
        <p v-else class="text-gray-500">Выберите сотрудника, чтобы увидеть сообщения</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_URL } from "@/config.js";


export default {
  name: "AdminMessages",
  data() {
    return {
      users: [],
      messages: [],
      selectedUser: null,
      newMessage: "",
      currentUser: null,
    };
  },
  async created() {
    try {
      const token = localStorage.getItem("accessToken");

      const userResponse = await axios.get(`${API_URL}/api/auth/user/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      this.currentUser = userResponse.data;

      const usersResponse = await axios.get(`${API_URL}/api/auth/users/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      this.users = usersResponse.data.filter(user => user.role === "employee");
    } catch (error) {
      console.error("Ошибка загрузки пользователей:", error);
    }
  },
  methods: {
    async selectUser(user) {
      this.selectedUser = user;
      try {
        const token = localStorage.getItem("accessToken");
        const messagesResponse = await axios.get(`${API_URL}/api/messaging/`, {
          headers: { Authorization: `Bearer ${token}` },
          params: { user: user.id },
        });
        this.messages = messagesResponse.data;
      } catch (error) {
        console.error("Ошибка загрузки сообщений:", error);
      }
    },
    async sendMessage() {
      if (!this.newMessage.trim()) {
        alert("Сообщение не может быть пустым!");
        return;
      }
      try {
        const token = localStorage.getItem("accessToken");
        await axios.post(
          `${API_URL}/api/messaging/`,
          { content: this.newMessage.trim(), receiver: this.selectedUser.id },
          { headers: { Authorization: `Bearer ${token}` } }
        );
        this.newMessage = "";
        this.selectUser(this.selectedUser);
      } catch (error) {
        console.error("Ошибка отправки сообщения:", error);
      }
    },
    formatDate(date) {
      return new Date(date).toLocaleString("ru-RU", {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      });
    },
  },
};
</script>
