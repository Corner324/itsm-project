<template>
  <div class="p-6">
    <h1 class="text-3xl font-bold mb-6">Детали заявки</h1>
    <div class="border border-gray-200 rounded shadow p-4 bg-white">
      <p><strong>Дата регистрации:</strong> {{ incident.created_at }}</p>
      <p><strong>Номер:</strong> {{ incident.id }}</p>
      <p><strong>Статус:</strong> {{ statusText(incident.status) }}</p>
      <p><strong>Тип заявки:</strong> {{ incident.type }}</p>
      <p><strong>Ответственный:</strong>
        <input
          v-model="incident.responsible"
          type="text"
          class="mt-1 p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          placeholder="Введите имя ответственного"
        />
      </p>
      <p><strong>Команда:</strong> {{ incident.team }}</p>
      <p><strong>Тема:</strong> {{ incident.topic }}</p>
      <p><strong>Описание:</strong> {{ incident.description }}</p>
    </div>
    <div class="mt-4 flex gap-4">
      <button
        @click="updateResponsible"
        class="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700"
      >
        Сохранить ответственного
      </button>
      <button
        @click="$router.push('/support-dashboard')"
        class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
      >
        Назад к списку
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { notification } from "@/App.vue";
import { API_URL } from "@/config.js";

export default {
  name: "IncidentDetails",
  data() {
    return {
      incident: {}, // Хранение данных инцидента
    };
  },
    async created() {
    try {
      const token = localStorage.getItem("accessToken");
      const response = await axios.get(`${API_URL}/api/incidents/${this.$route.params.id}/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      this.incident = response.data;  // Используем response
    } catch (error) {
      console.error("Ошибка загрузки деталей заявки:", error);
      notification.show("Ошибка при загрузке заявки.", "error");
      this.$router.push("/support-dashboard");
    }
  },
  methods: {
    statusText(status) {
      const statuses = {
        new: "Новая",
        in_progress: "В работе",
        resolved: "Завершена",
        rejected: "Отклонена",
      };
      return statuses[status] || "Неизвестно";
    },

    async updateResponsible() {
      try {
        const token = localStorage.getItem("accessToken");
        await axios.patch(
          `${API_URL}/api/incidents/${this.incident.id}/`, // Используем ID инцидента
          { responsible: this.incident.responsible }, // Обновляем только ответственного
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        notification.show("Ответственный обновлен успешно", "success");
      } catch (error) {
        console.error("Ошибка при обновлении ответственного:", error);
        notification.show("Ошибка при обновлении ответственного", "error");
      }
    },
  },
};
</script>

<style scoped>
body {
  background-color: #f9fafb; /* Нежно-серый фон */
}
</style>
