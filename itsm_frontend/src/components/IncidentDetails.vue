<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Детали заявки #{{ incident.id }}</h1>
    <div class="mb-4">
      <p><strong>Заголовок:</strong> {{ incident.title }}</p>
      <p><strong>Описание:</strong> {{ incident.description }}</p>
      <p><strong>Статус:</strong> {{ incident.status }}</p>
      <p><strong>Дата создания:</strong> {{ incident.created_at }}</p>
    </div>
    <div class="flex gap-4">
      <button
        v-for="status in statuses"
        :key="status"
        @click="updateStatus(status)"
        :class="['px-4 py-2 rounded-md', statusButtonClass(status)]"
      >
        {{ status }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "IncidentDetails",
  data() {
    return {
      incident: {},
      statuses: ["В работе", "Завершено", "Отклонено"],
    };
  },
  async created() {
    const { id } = this.$route.params;
    try {
      const response = await axios.get(`/api/incidents/${id}/`);
      this.incident = response.data;
    } catch (error) {
      console.error("Ошибка загрузки заявки:", error);
    }
  },
  methods: {
    async updateStatus(status) {
      const { id } = this.$route.params;
      try {
        const response = await axios.patch(`/api/incidents/${id}/`, { status });
        this.incident.status = response.data.status;
        alert("Статус успешно обновлён!");
      } catch (error) {
        console.error("Ошибка обновления статуса:", error);
        alert("Не удалось обновить статус.");
      }
    },
    statusButtonClass(status) {
      if (status === "В работе") return "bg-blue-600 text-white hover:bg-blue-700";
      if (status === "Завершено") return "bg-green-600 text-white hover:bg-green-700";
      if (status === "Отклонено") return "bg-red-600 text-white hover:bg-red-700";
      return "bg-gray-600 text-white hover:bg-gray-700";
    },
  },
};
</script>
