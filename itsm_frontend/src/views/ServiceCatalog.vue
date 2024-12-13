<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-6">Каталоги услуг</h1>

    <!-- Бизнес-каталог услуг -->
    <div class="mb-8">
      <h2 class="text-xl font-semibold mb-4">Бизнес-каталог услуг</h2>
      <button
        @click="openCreateBusinessModal"
        class="mb-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Добавить услугу
      </button>
      <table class="w-full border-collapse border border-gray-300">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 p-2">Линия услуг</th>
            <th class="border border-gray-300 p-2">Название</th>
            <th class="border border-gray-300 p-2">Описание</th>
            <th class="border border-gray-300 p-2">Статус</th>
            <th class="border border-gray-300 p-2">Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="service in businessServices"
            :key="service.id"
            class="hover:bg-gray-50"
          >
            <td class="border border-gray-300 p-2">{{ service.category }}</td>
            <td class="border border-gray-300 p-2">{{ service.name }}</td>
            <td class="border border-gray-300 p-2">{{ service.description }}</td>
            <td class="border border-gray-300 p-2">{{ statusText(service.status) }}</td>
            <td class="border border-gray-300 p-2">
              <button
                @click="editBusinessService(service.id)"
                class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
              >
                Редактировать
              </button>
              <button
                @click="deleteBusinessService(service.id)"
                class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
              >
                Удалить
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Технический каталог услуг -->
    <div>
      <h2 class="text-xl font-semibold mb-4">Технический каталог услуг</h2>
      <button
        @click="openCreateTechnicalModal"
        class="mb-4 px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
      >
        Добавить техническую услугу
      </button>
      <table class="w-full border-collapse border border-gray-300">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 p-2">Линия услуг</th>
            <th class="border border-gray-300 p-2">Название</th>
            <th class="border border-gray-300 p-2">Конфигурационные единицы</th>
            <th class="border border-gray-300 p-2">Статус</th>
            <th class="border border-gray-300 p-2">Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="service in technicalServices"
            :key="service.id"
            class="hover:bg-gray-50"
          >
            <td class="border border-gray-300 p-2">{{ service.category }}</td>
            <td class="border border-gray-300 p-2">{{ service.name }}</td>
            <td class="border border-gray-300 p-2">{{ service.configuration_items }}</td>
            <td class="border border-gray-300 p-2">{{ statusText(service.status) }}</td>
            <td class="border border-gray-300 p-2">
              <button
                @click="editTechnicalService(service.id)"
                class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
              >
                Редактировать
              </button>
              <button
                @click="deleteTechnicalService(service.id)"
                class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
              >
                Удалить
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
import { API_URL } from "@/config.js";

export default {
  name: "ServiceCatalog",
  data() {
    return {
      businessServices: [],
      technicalServices: [],
    };
  },
  async created() {
    try {
      const token = localStorage.getItem("accessToken");
      const [businessResponse, technicalResponse] = await Promise.all([
        axios.get(`${API_URL}/api/services/business/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
        axios.get(`${API_URL}/api/services/technical/`, {
          headers: { Authorization: `Bearer ${token}` },
        }),
      ]);
      this.businessServices = businessResponse.data;
      this.technicalServices = technicalResponse.data;
    } catch (error) {
      console.error("Ошибка загрузки данных:", error);
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
    openCreateBusinessModal() {
      this.$router.push("/service-catalog/create");
    },
    openCreateTechnicalModal() {
      this.$router.push("/service-catalog/create");
    },
    editBusinessService(id) {
      this.$router.push(`/service-catalog/edit/${id}`);
    },
    editTechnicalService(id) {
      this.$router.push(`/service-catalog/edit/${id}`);
    },
    async deleteBusinessService(id) {
      try {
        const token = localStorage.getItem("accessToken");
        await axios.delete(`${API_URL}/api/services/business/${id}/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.businessServices = this.businessServices.filter(
          (service) => service.id !== id
        );
      } catch (error) {
        console.error("Ошибка удаления услуги:", error);
      }
    },
    async deleteTechnicalService(id) {
      try {
        const token = localStorage.getItem("accessToken");
        await axios.delete(`${API_URL}/api/services/technical/${id}/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.technicalServices = this.technicalServices.filter(
          (service) => service.id !== id
        );
      } catch (error) {
        console.error("Ошибка удаления технической услуги:", error);
      }
    },
  },
};
</script>
