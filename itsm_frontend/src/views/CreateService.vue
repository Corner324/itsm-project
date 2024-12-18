<template>
  <div class="p-6 max-w-3xl mx-auto bg-white rounded shadow-md">
    <h1 class="text-3xl font-bold mb-6">Добавить услугу</h1>
    <form @submit.prevent="submitService" class="space-y-6">
      <div>
        <label for="catalogType" class="block text-sm font-medium text-gray-700">Тип каталога</label>
        <select
          id="catalogType"
          v-model="catalogType"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          required
        >
          <option value="business">Бизнес-каталог</option>
          <option value="technical">Технический каталог</option>
        </select>
      </div>
      <div>
        <label for="category" class="block text-sm font-medium text-gray-700">Категория</label>
        <input
          type="text"
          id="category"
          v-model="form.category"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          placeholder="Введите категорию услуги"
          required
        />
      </div>
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
      <div v-if="catalogType === 'business'">
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
      <div v-if="catalogType === 'technical'">
        <label for="configuration_items" class="block text-sm font-medium text-gray-700">Конфигурационные единицы</label>
        <textarea
          id="configuration_items"
          v-model="form.configuration_items"
          rows="4"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          placeholder="Введите конфигурационные единицы"
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
import { API_URL } from "@/config.js";

export default {
  name: "CreateService",
  data() {
    return {
      catalogType: "business", // По умолчанию выбран бизнес-каталог
      form: {
        category: "",
        name: "",
        description: "",
        configuration_items: "", // Только для технического каталога
        status: "active",
      },
    };
  },
  methods: {
    async submitService() {
      try {
        const token = localStorage.getItem("accessToken");
        const endpoint =
          this.catalogType === "business"
            ? `${API_URL}/api/services/business/`
            : `${API_URL}/api/services/technical/`;

        // Удаляем ненужные поля в зависимости от типа каталога
        const payload = { ...this.form };
        if (this.catalogType === "business") {
          delete payload.configuration_items;
        } else {
          delete payload.description;
        }

        await axios.post(endpoint, payload, {
          headers: { Authorization: `Bearer ${token}` },
        });

        alert("Услуга успешно создана!");
        this.$router.push("/service-catalog");
      } catch (error) {
        console.error("Ошибка при создании услуги:", error);
        alert("Ошибка при создании услуги. Попробуйте снова.");
      }
    },
  },
};
</script>

<style>
body {
  background-color: #f9fafb; /* Нежно-серый фон */
}
</style>
