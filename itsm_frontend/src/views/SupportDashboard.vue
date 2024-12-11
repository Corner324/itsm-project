<template>
  <div class="p-4">
    <h1 class="text-3xl font-bold mb-6">Все заявки</h1>
    <div class="overflow-x-auto">
      <table class="min-w-full border-collapse border border-gray-200 shadow-lg">
        <thead>
          <tr class="bg-gray-100 text-left text-sm uppercase tracking-wider">
            <th class="p-3 border border-gray-200">Дата регистрации</th>
            <th class="p-3 border border-gray-200">Номер</th>
            <th class="p-3 border border-gray-200">Статус</th>
            <th class="p-3 border border-gray-200">Тип заявки</th>
            <th class="p-3 border border-gray-200">Ответственный</th>
            <th class="p-3 border border-gray-200">Команда</th>
            <th class="p-3 border border-gray-200">Тема</th>
            <th class="p-3 border border-gray-200">Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="incident in incidents"
            :key="incident.id"
            class="hover:bg-gray-50 transition-all"
          >
            <td class="p-3 border border-gray-200">
              {{ new Date(incident.created_at).toLocaleString("ru-RU") }}
            </td>
            <td class="p-3 border border-gray-200">{{ incident.id }}</td>
            <td class="p-3 border border-gray-200">
              <span
                :class="statusBadgeClass(incident.status)"
                class="px-2 py-1 rounded text-xs"
              >
                {{ statusText(incident.status) }}
              </span>
            </td>
            <td class="p-3 border border-gray-200">{{ incident.type }}</td>
            <td class="p-3 border border-gray-200">{{ incident.responsible }}</td>
            <td class="p-3 border border-gray-200">{{ incident.team }}</td>
            <td class="p-3 border border-gray-200">{{ incident.topic }}</td>
            <td class="p-3 border border-gray-200">
              <button
                class="px-3 py-1 bg-yellow-500 text-white rounded hover:bg-yellow-600"
                @click="updateIncidentStatus(incident.id, 'in_progress')"
              >
                В работу
              </button>
              <button
                class="px-3 py-1 bg-green-500 text-white rounded hover:bg-green-600"
                @click="updateIncidentStatus(incident.id, 'resolved')"
              >
                Завершить
              </button>
              <button
                class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
                @click="updateIncidentStatus(incident.id, 'rejected')"
              >
                Отклонить
              </button>
            </td>
            <td class="p-3 border border-gray-200">
              <button
                class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
                @click="$router.push(`/incident/${incident.id}`)"
              >
                Открыть
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { notification } from "@/App.vue";
import { API_URL } from "@/config.js";


export default {
  name: "SupportDashboard",
  data() {
    return {
      incidents: [],
    };
  },
  async created() {
    try {
      const token = localStorage.getItem("accessToken");
      const response = await axios.get(`${API_URL}/api/incidents/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      this.incidents = response.data;
    } catch (error) {
      notification.show("Ошибка при загрузке данных", "error");
      console.error(error);
    }
  },
  methods: {
    statusBadgeClass(status) {
      switch (status) {
        case "new":
          return "bg-blue-100 text-blue-600";
        case "in_progress":
          return "bg-yellow-100 text-yellow-600";
        case "resolved":
          return "bg-green-100 text-green-600";
        case "rejected":
          return "bg-red-100 text-red-600";
        default:
          return "bg-gray-100 text-gray-600";
      }
    },
    statusText(status) {
      const statuses = {
        new: "Новая",
        in_progress: "В работе",
        resolved: "Завершена",
        rejected: "Отклонена",
      };
      return statuses[status] || "Неизвестно";
    },
    async updateIncidentStatus(id, status) {
      try {
        const token = localStorage.getItem("accessToken");
        await axios.patch(
          `${API_URL}/api/incidents/${id}/`,
          { status },
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        notification.show(`Статус заявки #${id} обновлён на "${this.statusText(status)}"`, "success");
        this.incidents = this.incidents.map((incident) =>
          incident.id === id ? { ...incident, status } : incident
        );
      } catch (error) {
        notification.show("Ошибка при обновлении статуса", "error");
        console.error(error);
      }
    },
  },
};
</script>
