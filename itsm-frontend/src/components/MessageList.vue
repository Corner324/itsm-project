<template>
  <div>
    <h2>Сообщения</h2>
    <ul>
      <li v-for="message in messages" :key="message.id">
        От: {{ message.sender }} - Кому: {{ message.receiver }}
        <p>{{ message.content }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MessageList",
  data() {
    return {
      messages: [],
    };
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/messaging/messages/")
      .then((response) => {
        this.messages = response.data;
      })
      .catch((error) => {
        console.error("Ошибка загрузки сообщений:", error);
      });
  },
};
</script>
