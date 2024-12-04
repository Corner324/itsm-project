<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Регистрация</h1>
      <form @submit.prevent="handleRegister">
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
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            type="email"
            id="email"
            v-model="form.email"
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
        <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">Зарегистрироваться</button>
      </form>
    </div>
  </template>
  
  <script>
  import { register } from "@/api/auth";
  
  export default {
    name: "Registration",
    data() {
      return {
        form: {
          username: "",
          email: "",
          password: "",
        },
      };
    },
    methods: {
      async handleRegister() {
        try {
          await register(this.form);
          alert("Регистрация прошла успешно!");
          this.$router.push("/login");
        } catch (error) {
          console.error(error);
          alert("Ошибка регистрации");
        }
      },
    },
  };
  </script>
  