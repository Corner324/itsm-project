<template>
  <div id="app" class="min-h-screen bg-gray-100">
    <!-- Хедер отображается только для авторизованных пользователей -->
    <header v-if="authStore.isAuthenticated" class="bg-blue-700 text-white shadow">
      <AppHeader />
    </header>
    <div class="flex">
      <!-- Сайдбар отображается только для авторизованных пользователей -->
      <AppSidebar v-if="authStore.isAuthenticated" class="bg-white shadow-md w-60" />
      <main class="flex-1 p-4">
        <!-- Основной контент -->
        <router-view />
      </main>
    </div>

    <!-- Уведомления -->
    <div v-if="notification.visible" :class="notificationClass" class="fixed bottom-4 right-4 p-4 rounded-md shadow-lg transition-all">
      <div class="flex items-center gap-2">
        <span v-if="notification.type === 'success'" class="text-green-500">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
          </svg>
        </span>
        <span v-if="notification.type === 'error'" class="text-red-500">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </span>
        <span v-if="notification.type === 'info'" class="text-blue-500">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M12 18.01V20m0 0H8m4-2h4" />
          </svg>
        </span>
        <p class="text-gray-800">{{ notification.message }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeader from "@/components/layout/Header.vue"; // Подключаем хедер
import AppSidebar from "@/components/layout/Sidebar.vue"; // Подключаем сайдбар
import { authStore } from "@/store/auth"; // Подключаем хранилище авторизации
import { computed, reactive } from "vue"; // Добавлен импорт computed

const notification = reactive({
  visible: false,
  message: "",
  type: "info", // Возможные значения: 'success', 'error', 'info'
  timeout: null,
  show(message, type = "info", duration = 3000) {
    this.message = message;
    this.type = type;
    this.visible = true;

    if (this.timeout) clearTimeout(this.timeout);
    this.timeout = setTimeout(() => {
      this.visible = false;
    }, duration);
  },
});

export default {
  name: "App",
  components: {
    AppHeader,
    AppSidebar,
  },
  setup() {
    const notificationClass = computed(() => {
      if (notification.type === "success") return "bg-green-100 border border-green-300";
      if (notification.type === "error") return "bg-red-100 border border-red-300";
      if (notification.type === "info") return "bg-blue-100 border border-blue-300";
      return "bg-gray-100";
    });

    return { authStore, notification, notificationClass };
  },
};
export { notification };
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f9fafb;
}
</style>
