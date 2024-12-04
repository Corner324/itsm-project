<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Вход</h1>
      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium text-gray-700">Имя пользователя</label>
          <input
            type="text"
            id="username"
            v-model="form.username"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
            required
          />
        </div>
        <div class="mb-4">
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <input
            type="password"
            id="password"
            v-model="form.password"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
            required
          />
        </div>
        <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">Войти</button>
      </form>
    </div>
  </template>
  
  <script>
  import { login } from "@/api/auth";
  
  export default {
    name: "Login",
    data() {
      return {
        form: {
          username: "",
          password: "",
        },
      };
    },
    methods: {
      async handleLogin() {
        try {
          const response = await login(this.form);
          localStorage.setItem("accessToken", response.data.access);
          localStorage.setItem("refreshToken", response.data.refresh);
          alert("Успешный вход!");
          this.$router.push("/");
        } catch (error) {
          console.error(error);
          alert("Ошибка входа");
        }
      },
    },
  };
  </script>
  