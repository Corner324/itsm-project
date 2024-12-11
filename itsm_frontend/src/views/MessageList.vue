<template>
  <div class="p-6 max-w-3xl mx-auto bg-white rounded shadow-md">
    <h1 class="text-3xl font-bold mb-6">Мои сообщения</h1>

    <!-- Список сообщений -->
    <div v-if="messages.length">
      <div v-for="message in messages" :key="message.id" class="mb-4">
        <div class="bg-gray-100 p-4 rounded shadow">
          <p class="text-sm text-gray-500">{{ formatDate(message.created_at) }}</p>
          <p class="mt-2">{{ message.content }}</p>
          <p
            class="text-sm text-blue-500 mt-2"
            v-if="currentUser && message.sender === currentUser.id"
          >
            Отправлено администратору
          </p>
        </div>
      </div>
    </div>
    <p v-else class="text-gray-500">Сообщений пока нет.</p>

    <!-- Поле ввода нового сообщения -->
    <textarea
      v-model="newMessage"
      rows="4"
      class="mt-4 block w-full border-gray-300 rounded-md shadow-sm"
      placeholder="Введите сообщение..."
    ></textarea>

    <!-- Кнопка отправки -->
    <button
      @click="sendMessage"
      class="mt-4 w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
    >
      Отправить
    </button>
  </div>
</template>

<script>
import axios from "axios";
import { API_URL } from "@/config.js";


export default {
  name: "MessageList",
  data() {
    return {
      messages: [], 
      newMessage: "", 
      currentUser: null, 
    };
  },
  async created() {
    try {
      await this.loadMessages(); 
    } catch (error) {
      console.error("Ошибка загрузки сообщений:", error);
    }
  },
  methods: {
    
    async loadMessages() {
      try {
        const token = localStorage.getItem("accessToken");

        
        const userResponse = await axios.get(`${API_URL}/api/auth/user/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.currentUser = userResponse.data;

        
        const messagesResponse = await axios.get(`${API_URL}/api/messaging/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.messages = messagesResponse.data;
      } catch (error) {
        console.error("Ошибка при загрузке данных:", error);
        throw error; 
      }
    },

    
    async sendMessage() {
      if (!this.newMessage.trim()) {
        alert("Сообщение не может быть пустым!");
        return;
      }

      try {
        const token = localStorage.getItem("accessToken");

        
        const adminResponse = await axios.get(`${API_URL}/api/auth/admin/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        const adminId = adminResponse.data.id;

        
        await axios.post(
          `${API_URL}/api/messaging/`,
          {
            content: this.newMessage.trim(),
            receiver: adminId,
          },
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );

        this.newMessage = ""; 
        alert("Сообщение успешно отправлено!");

        
        await this.loadMessages();
      } catch (error) {
        console.error("Ошибка отправки сообщения:", error);

        if (error.response?.data?.detail) {
          alert(`Ошибка: ${error.response.data.detail}`);
        } else {
          alert("Не удалось отправить сообщение. Проверьте соединение или повторите попытку.");
        }
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
