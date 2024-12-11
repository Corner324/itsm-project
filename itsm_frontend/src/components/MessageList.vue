<template>
  <div class="messenger">
    <h2>Сообщения</h2>
    <ul class="message-list">
      <li v-for="message in messages" :key="message.id">
        <p><strong>От:</strong> {{ message.sender }}</p>
        <p><strong>Кому:</strong> {{ message.receiver }}</p>
        <p><strong>Сообщение:</strong> {{ message.content }}</p>
      </li>
    </ul>
    <form @submit.prevent="sendMessage">
      <h3>Отправить сообщение</h3>
      <div>
        <label for="receiver">Кому:</label>
        <input type="text" id="receiver" v-model="newMessage.receiver" required />
      </div>
      <div>
        <label for="content">Сообщение:</label>
        <textarea id="content" v-model="newMessage.content" required></textarea>
      </div>
      <button type="submit">Отправить</button>
    </form>
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
      newMessage: {
        receiver: "",
        content: "",
      },
    };
  },
  methods: {
    fetchMessages() {
      axios.get(`${API_URL}/api/messaging/messages/`).then((response) => {
        this.messages = response.data;
      });
    },
    sendMessage() {
      axios
        .post(`${API_URL}/api/messaging/messages/`, this.newMessage)
        .then(() => {
          this.newMessage = { receiver: "", content: "" };
          this.fetchMessages();
        });
    },
  },
  mounted() {
    this.fetchMessages();
  },
};
</script>

<style scoped>
.messenger {
  padding: 20px;
}

.message-list {
  list-style: none;
  padding: 0;
}

.message-list li {
  margin-bottom: 20px;
  border: 1px solid #ddd;
  padding: 10px;
}

form {
  margin-top: 20px;
}

form div {
  margin-bottom: 10px;
}
</style>
