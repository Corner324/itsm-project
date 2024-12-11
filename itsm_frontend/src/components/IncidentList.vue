<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Все заявки</h1>
    <table class="w-full border-collapse border border-gray-300">
      <thead>
        <tr class="bg-gray-100">
          <th class="border border-gray-300 p-2">ID</th>
          <th class="border border-gray-300 p-2">Заголовок</th>
          <th class="border border-gray-300 p-2">Статус</th>
          <th class="border border-gray-300 p-2">Дата</th>
          <th class="border border-gray-300 p-2">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="incident in incidents" :key="incident.id" class="hover:bg-gray-50">
          <td class="border border-gray-300 p-2">{{ incident.id }}</td>
          <td class="border border-gray-300 p-2">{{ incident.title }}</td>
          <td class="border border-gray-300 p-2">{{ incident.status }}</td>
          <td class="border border-gray-300 p-2">{{ incident.created_at }}</td>
          <td class="border border-gray-300 p-2">
            <router-link :to="`/incident-details/${incident.id}`" class="text-blue-600 hover:underline">
              Открыть
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import { API_URL } from "@/config.js";

export default {
  name: "IncidentsList",
  data() {
    return {
      incidents: [],
    };
  },
  async created() {
    try {
      const response = await axios.get(`${API_URL}/api/incidents/`);
      console.log(`${API_URL}/api/incidents/`)
      this.incidents = response.data;
    } catch (error) {
      console.error("Ошибка загрузки заявок:", error);
    }
  },
};
</script>
