<template>
  <div class="flex items-center justify-center h-screen bg-gray-100">
    <div class="w-full max-w-md bg-white rounded-lg shadow-lg p-6">
      <h1 class="text-3xl font-semibold text-center text-blue-600 mb-6">Вход</h1>
      <form @submit.prevent="handleLogin" class="space-y-4">
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
          Войти
        </button>
      </form>
      <p class="mt-4 text-center text-sm text-gray-600">
        Нет аккаунта? 
        <router-link to="/register" class="text-blue-600 hover:underline">Зарегистрируйтесь</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import { login } from "@/api/auth";
import { authStore } from "@/store/auth";

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

        authStore.setAuth(true, { username: this.form.username });

        this.$router.push("/dashboard");
      } catch (error) {
        console.error(error);
        alert("Ошибка входа");
      }
    },
  },
};
</script>
