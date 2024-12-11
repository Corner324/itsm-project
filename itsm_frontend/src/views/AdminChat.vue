<template>
    <div class="p-6 max-w-6xl mx-auto bg-white rounded shadow-md">
      <h1 class="text-2xl font-bold mb-6">Чат с {{ user.username }}</h1>
      <div class="bg-gray-100 p-4 rounded shadow mb-4">
        <ul>
          <li
            v-for="message in messages"
            :key="message.id"
            class="mb-4"
          >
            <span v-if="message.sender === authStore.user?.id" class="text-blue-600">
              Вы:
            </span>
            <span v-else class="text-gray-800">{{ user.username }}:</span>
            <p>{{ message.content }}</p>
          </li>
        </ul>
      </div>
      <textarea
        v-model="newMessage"
        rows="4"
        class="w-full border-gray-300 rounded-md"
        placeholder="Введите сообщение..."
      ></textarea>
      <button
        @click="sendMessage"
        class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md"
      >
        Отправить
      </button>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import { authStore } from "@/store/auth";
  
  export default {
    name: "AdminChat",
    data() {
      return {
        user: {},
        messages: [],
        newMessage: "",
      };
    },
    async created() {
      try {
        const API_URL = "http://127.0.0.1:8000";
        const userId = this.$route.params.id;
        const token = localStorage.getItem("accessToken");
  
        const userResponse = await axios.get(`${API_URL}/api/auth/users/${userId}/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.user = userResponse.data;
  
        const messagesResponse = await axios.get(`${API_URL}/api/messaging/`, {
          headers: { Authorization: `Bearer ${token}` },
          params: { receiver: userId },
        });
        this.messages = messagesResponse.data;
      } catch (error) {
        console.error("Ошибка загрузки чата:", error);
      }
    },
    methods: {
      async sendMessage() {
        const API_URL = "http://127.0.0.1:8000";
        if (!this.newMessage.trim()) return;
        try {
          const token = localStorage.getItem("accessToken");
          await axios.post(
            `${API_URL}/api/messaging/`,
            { content: this.newMessage, receiver: this.user.id },
            { headers: { Authorization: `Bearer ${token}` } }
          );
          this.newMessage = "";
          this.created();
        } catch (error) {
          console.error("Ошибка отправки сообщения:", error);
        }
      },
    },
    setup() {
      return { authStore };
    },
  };
  </script>
  