<template>
  <div class="p-6">
    <h1 class="text-3xl font-bold mb-6">Создать заявку</h1>
    <form @submit.prevent="submitTicket" class="space-y-4">
      <div>
        <label for="type" class="block text-sm font-medium text-gray-700">
          Тип заявки
        </label>
        <select
          id="type"
          v-model="form.type"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
        >
          <option value="issue">Проблема</option>
          <option value="request">Запрос</option>
          <option value="incident">Инцидент</option>
        </select>
      </div>
      <div>
        <label for="topic" class="block text-sm font-medium text-gray-700">
          Тема
        </label>
        <input
          type="text"
          id="topic"
          v-model="form.topic"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
          required
        />
      </div>
      <div>
        <label for="description" class="block text-sm font-medium text-gray-700">
          Описание
        </label>
        <textarea
          id="description"
          v-model="form.description"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
          required
        ></textarea>
      </div>
      <button
        type="submit"
        class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
      >
        Отправить заявку
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { notification } from "@/App.vue";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CreateTicket",
  data() {
    return {
      form: {
        type: "issue",
        topic: "",
        description: "",
      },
    };
  },
  methods: {
    async submitTicket() {
      try {
        const token = localStorage.getItem("accessToken");
        await axios.post(`${API_URL}/api/incidents/create/`, this.form, {
          headers: { Authorization: `Bearer ${token}` },
        });
        notification.show("Заявка успешно создана!", "success");
        this.$router.push("/my-incidents");
      } catch (error) {
        notification.show("Ошибка при создании заявки. Попробуйте снова.", "error");
        console.error(error);
      }
    },
  },
};
</script>
