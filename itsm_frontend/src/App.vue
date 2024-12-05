<template>
  <div id="app">
    <!-- Хедер отображается только для авторизованных пользователей -->
    <header v-if="authStore.isAuthenticated">
      <AppHeader />
    </header>
    <div class="flex">
      <!-- Сайдбар отображается только для авторизованных пользователей -->
      <AppSidebar v-if="authStore.isAuthenticated" />
      <main class="flex-1 p-4">
        <!-- Основной контент -->
        <router-view />
      </main>
    </div>
  </div>
</template>

<script>
import AppHeader from "@/components/layout/Header.vue"; // Подключаем хедер
import AppSidebar from "@/components/layout/Sidebar.vue"; // Подключаем сайдбар
import { authStore } from "@/store/auth"; // Подключаем хранилище авторизации

export default {
  name: "App",
  components: {
    AppHeader, // Регистрируем компонент хедера
    AppSidebar, // Регистрируем компонент сайдбара
  },
  setup() {
    return { authStore }; // Используем authStore для управления состоянием авторизации
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>
