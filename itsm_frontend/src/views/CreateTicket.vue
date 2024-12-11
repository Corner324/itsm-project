<template>
  <div class="p-6 max-w-3xl mx-auto bg-white rounded shadow-md">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">Создать заявку</h1>
    <form @submit.prevent="submitTicket" class="space-y-6">
      <!-- Тип заявки -->
      <div>
        <label for="type" class="block text-sm font-medium text-gray-700">
          Тип заявки
        </label>
        <select
          id="type"
          v-model="form.type"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          required
        >
          <option value="issue">Проблема</option>
          <option value="request">Запрос</option>
          <option value="incident">Инцидент</option>
        </select>
      </div>

      <!-- Тема -->
      <div>
        <label for="topic" class="block text-sm font-medium text-gray-700">
          Тема
        </label>
        <input
          type="text"
          id="topic"
          v-model="form.topic"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          placeholder="Кратко опишите проблему"
          required
        />
      </div>

      <!-- Описание -->
      <div>
        <label for="description" class="block text-sm font-medium text-gray-700">
          Описание
        </label>
        <textarea
          id="description"
          v-model="form.description"
          rows="4"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          placeholder="Опишите проблему подробнее"
          required
        ></textarea>
      </div>

      <!-- Ответственный -->
      <div>
        <label for="responsible" class="block text-sm font-medium text-gray-700">
          Ответственный
        </label>
        <input
          type="text"
          id="responsible"
          v-model="form.responsible"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          placeholder="Введите имя сотрудника"
        />
      </div>

      <!-- Команда -->
      <div>
        <label for="team" class="block text-sm font-medium text-gray-700">
          Команда
        </label>
        <input
          type="text"
          id="team"
          v-model="form.team"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          placeholder="Введите название команды"
        />
      </div>

      <!-- Кнопка отправки -->
      <div>
        <button
          type="submit"
          class="w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 shadow-md transition duration-200"
        >
          Отправить заявку
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { notification } from "@/App.vue";
import { API_URL } from "@/config.js";

export default {
  name: "CreateTicket",
  data() {
    return {
      form: {
        type: "issue",
        topic: "",
        description: "",
        responsible: "",
        team: "",
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
        console.error("Ошибка при создании заявки:", error);
        notification.show("Ошибка при создании заявки. Попробуйте снова.", "error");
      }
    },
  },
};
</script>

<style>
body {
  background-color: #f9fafb; /* Нежно-серый фон */
}
</style>
