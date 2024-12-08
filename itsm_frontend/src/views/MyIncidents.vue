<template>
    <div class="p-4">
      <h1 class="text-3xl font-bold mb-6">Мои заявки</h1>
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
              <th class="p-3 border border-gray-200">Описание</th>
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
              <td class="p-3 border border-gray-200">{{ incident.description }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import { notification } from "@/App.vue";
  
  const API_URL = "http://127.0.0.1:8000";
  
  export default {
    name: "MyIncidents",
    data() {
      return {
        incidents: [],
      };
    },
    async created() {
      try {
        const token = localStorage.getItem("accessToken");
        const response = await axios.get(`${API_URL}/api/incidents/my/`, {
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
    },
  };
  </script>
  