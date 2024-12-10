<template>
    <div class="p-6 max-w-3xl mx-auto bg-white rounded shadow-md">
      <h1 class="text-3xl font-bold mb-6">Добавить услугу</h1>
      <form @submit.prevent="submitService" class="space-y-6">
        <div>
          <label for="name" class="block text-sm font-medium text-gray-700">Название</label>
          <input
            type="text"
            id="name"
            v-model="form.name"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            placeholder="Введите название услуги"
            required
          />
        </div>
        <div>
          <label for="description" class="block text-sm font-medium text-gray-700">Описание</label>
          <textarea
            id="description"
            v-model="form.description"
            rows="4"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            placeholder="Введите описание услуги"
            required
          ></textarea>
        </div>
        <div>
          <label for="status" class="block text-sm font-medium text-gray-700">Статус</label>
          <select
            id="status"
            v-model="form.status"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          >
            <option value="active">Активная</option>
            <option value="inactive">Неактивная</option>
          </select>
        </div>
        <button
          type="submit"
          class="w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 shadow-md transition duration-200"
        >
          Сохранить
        </button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  const API_URL = "http://127.0.0.1:8000";
  
  export default {
    name: "CreateService",
    data() {
      return {
        form: {
          name: "",
          description: "",
          status: "active",
        },
      };
    },
    methods: {
      async submitService() {
        try {
          const token = localStorage.getItem("accessToken");
          await axios.post(`${API_URL}/api/services/`, this.form, {
            headers: { Authorization: `Bearer ${token}` },
          });
          this.$router.push("/service-catalog");
        } catch (error) {
          console.error("Ошибка при создании услуги:", error);
        }
      },
    },
  };
  </script>
  