<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-xl w-full bg-white shadow-lg rounded-lg p-6">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">Отчет об инциденте</h2>
      <form @submit.prevent="submitReport">
        <div class="mb-4">
          <label for="name" class="block text-sm font-medium text-gray-700">Ваше имя</label>
          <input
            v-model="form.name"
            id="name"
            type="text"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            v-model="form.email"
            id="email"
            type="email"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div class="mb-4">
          <label for="incident" class="block text-sm font-medium text-gray-700">Описание инцидента</label>
          <textarea
            v-model="form.incident"
            id="incident"
            rows="4"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          ></textarea>
        </div>
        <button
          type="submit"
          class="w-full py-2 px-4 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 transition"
        >
          Отправить
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PublicReportForm",
  data() {
    return {
      form: {
        name: "",
        email: "",
        incident: "",
      },
    };
  },
  methods: {
    async submitReport() {
      try {
        const payload = {
          name: this.form.name,
          email: this.form.email,
          incident: this.form.incident,
        };
        console.log("Отправка данных:", payload);
        await axios.post("http://127.0.0.1:8000/api/incidents/public/create/", payload);
        alert("Ваш отчет успешно отправлен!");
        this.form.name = "";
        this.form.email = "";
        this.form.incident = "";
      } catch (error) {
        console.error("Ошибка при отправке отчета:", error);
        alert("Произошла ошибка при отправке отчета. Пожалуйста, попробуйте снова.");
      }
    }
  },
};
</script>

<style scoped>
body {
  font-family: 'Inter', sans-serif;
  background-color: #f9fafb;
}
</style>
