<template>
  <div class="flex items-center justify-center h-screen bg-gray-100">
    <div class="w-full max-w-lg bg-white rounded-lg shadow-lg p-6">
      <h1 class="text-3xl font-semibold text-center text-blue-600 mb-6">Регистрация</h1>
      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700">Имя пользователя</label>
          <div class="relative">
            <input
              type="text"
              id="username"
              v-model="form.username"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Введите имя пользователя"
              required
            />
            <span class="absolute inset-y-0 right-3 flex items-center text-gray-400">
              <i class="fas fa-user"></i>
            </span>
          </div>
        </div>
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <div class="relative">
            <input
              type="email"
              id="email"
              v-model="form.email"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Введите email"
              required
            />
            <span class="absolute inset-y-0 right-3 flex items-center text-gray-400">
              <i class="fas fa-envelope"></i>
            </span>
          </div>
        </div>
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <div class="relative">
            <input
              type="password"
              id="password"
              v-model="form.password"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Введите пароль"
              required
            />
            <span class="absolute inset-y-0 right-3 flex items-center text-gray-400">
              <i class="fas fa-lock"></i>
            </span>
          </div>
        </div>
        <button
          type="submit"
          class="w-full bg-blue-600 text-white rounded-md px-4 py-2 text-lg font-semibold hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        >
          Зарегистрироваться
        </button>
      </form>
      <p class="mt-4 text-center text-sm text-gray-600">
        Уже есть аккаунт? 
        <router-link to="/login" class="text-blue-600 hover:underline">Войдите</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import { register } from "@/api/auth";
import { notification } from "@/App.vue";

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
        notification.show("Регистрация прошла успешно!");
        this.$router.push("/login");
      } catch (error) {
        if (error.response && error.response.data) {
          const errors = error.response.data;
          if (errors.username) {
            notification.show(`Ошибка имени пользователя: ${errors.username[0]}`);
          } else if (errors.email) {
            notification.show(`Ошибка email: ${errors.email[0]}`);
          } else {
            notification.show("Произошла ошибка при регистрации. Попробуйте снова.");
          }
        } else {
          console.error(error);
          notification.show("Сбой соединения с сервером. Попробуйте позже.");
        }
      }
    }
  },
};
</script>
