<template>
  <div class="p-6">
    <h1 class="text-3xl font-bold mb-6">Детали заявки</h1>
    <div class="border border-gray-200 rounded shadow p-4 bg-white">
      <p><strong>Дата регистрации:</strong> {{ incident.created_at }}</p>
      <p><strong>Номер:</strong> {{ incident.id }}</p>
      <p><strong>Статус:</strong> {{ statusText(incident.status) }}</p>
      <p><strong>Тип заявки:</strong> {{ incident.type }}</p>
      <p><strong>Ответственный:</strong> {{ incident.responsible }}</p>
      <p><strong>Команда:</strong> {{ incident.team }}</p>
      <p><strong>Тема:</strong> {{ incident.topic }}</p>
      <p><strong>Описание:</strong> {{ incident.description }}</p>
    </div>
    <button
      @click="$router.push('/support-dashboard')"
      class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
    >
      Назад к списку
    </button>
  </div>
</template>

<script>
import axios from "axios";
import { notification } from "@/App.vue";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "IncidentDetails",
  data() {
    return {
      incident: {},
    };
  },
  async created() {
    try {
      const token = localStorage.getItem("accessToken");
      const response = await axios.get(`${API_URL}/api/incidents/${this.$route.params.id}/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      this.incident = response.data;
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
  },
};
</script>
