<template>
    <div class="p-6">
      <h1 class="text-2xl font-bold mb-6">Каталог услуг</h1>
      <button
        @click="openCreateModal"
        class="mb-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Добавить услугу
      </button>
      <table class="w-full border-collapse border border-gray-300">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 p-2">Название</th>
            <th class="border border-gray-300 p-2">Описание</th>
            <th class="border border-gray-300 p-2">Статус</th>
            <th class="border border-gray-300 p-2">Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="service in services"
            :key="service.id"
            class="hover:bg-gray-50"
          >
            <td class="border border-gray-300 p-2">{{ service.name }}</td>
            <td class="border border-gray-300 p-2">{{ service.description }}</td>
            <td class="border border-gray-300 p-2">{{ statusText(service.status) }}</td>
            <td class="border border-gray-300 p-2">
              <button
                @click="editService(service.id)"
                class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
              >
                Редактировать
              </button>
              <button
                @click="deleteService(service.id)"
                class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
              >
                Удалить
              </button>
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
    name: "ServiceCatalog",
    data() {
      return {
        services: [],
      };
    },
    async created() {
      try {
        const token = localStorage.getItem("accessToken");
        const response = await axios.get(`${API_URL}/api/services/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.services = response.data;
      } catch (error) {
        console.error("Ошибка загрузки услуг:", error);
      }
    },
    methods: {
      statusText(status) {
        const statuses = {
          active: "Активная",
          inactive: "Неактивная",
        };
        return statuses[status] || "Неизвестно";
      },
      openCreateModal() {
        this.$router.push("/service-catalog/create");
      },
      editService(id) {
        this.$router.push(`/service-catalog/edit/${id}`);
      },
      async deleteService(id) {
        try {
          const token = localStorage.getItem("accessToken");
          await axios.delete(`${API_URL}/api/services/${id}/`, {
            headers: { Authorization: `Bearer ${token}` },
          });
          this.services = this.services.filter((service) => service.id !== id);
        } catch (error) {
          console.error("Ошибка удаления услуги:", error);
        }
      },
    },
  };
  </script>
  