<template>
    <div class="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 class="text-4xl font-bold mb-4">Добро пожаловать в ITSM Service Desk</h1>
      <p class="mb-6 text-lg text-gray-700">Пожалуйста, войдите в свой аккаунт или зарегистрируйтесь, чтобы продолжить.</p>
      <div class="flex gap-4">
        <router-link
          to="/login"
          class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
        >
          Войти
        </router-link>
        <router-link
          to="/register"
          class="px-4 py-2 bg-gray-300 text-gray-700 rounded-md hover:bg-gray-400"
        >
          Регистрация
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Welcome",
  };
  </script>
  
  <style scoped>
  h1 {
    color: #085896;
  }
  </style>
  