<template>
  <div class="catalog">
    <h2>Каталог услуг</h2>
    <table>
      <thead>
        <tr>
          <th>Название</th>
          <th>Описание</th>
          <th>Статус</th>
          <th>Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="service in services" :key="service.id">
          <td>{{ service.name }}</td>
          <td>{{ service.description }}</td>
          <td>{{ service.status }}</td>
          <td>
            <button @click="editService(service)">Редактировать</button>
            <button @click="deleteService(service.id)">Удалить</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import { notification } from "@/App.vue";
import { API_URL } from "@/config.js";

export default {
  name: "ServiceCatalog",
  data() {
    return {
      services: [],
    };
  },
  methods: {
    fetchServices() {
      axios.get(`${API_URL}/api/catalog/services/`).then((response) => {
        this.services = response.data;
      });
    },
    editService(service) {
      notification.show(`Редактирование услуги: ${service.name}`);
    },
    deleteService(id) {
      axios.delete(`${API_URL}/api/catalog/services/${id}/`).then(() => {
        this.fetchServices();
      });
    },
  },
  mounted() {
    this.fetchServices();
  },
};
</script>

<style scoped>
.catalog table {
  width: 100%;
  border-collapse: collapse;
}

.catalog th,
.catalog td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.catalog th {
  background-color: #007bff;
  color: white;
}
</style>
