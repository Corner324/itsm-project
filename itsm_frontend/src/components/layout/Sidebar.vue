<template>
  <aside class="bg-white h-full w-60 p-4 shadow">
    <nav class="flex flex-col gap-4">
      <router-link to="/dashboard" class="hover:text-blue-600">Главная</router-link>
      <!-- Вкладки для роли "Сотрудник" -->
      <template v-if="authStore.user?.role === 'employee'">
        <router-link to="/create-ticket" class="hover:text-blue-600">Создать заявку</router-link>
        <router-link to="/my-incidents" class="hover:text-blue-600">Мои заявки</router-link>
        <router-link to="/service-catalog" class="hover:text-blue-600">
          Каталог услуг
        </router-link>
      </template>
      <!-- Вкладки для роли "Техподдержка" -->
      <template v-if="authStore.user?.role === 'support'">
        <router-link to="/support-dashboard" class="hover:text-blue-600">Панель техподдержки</router-link>
      <!-- Вкладки для Каталога услуг -->
      </template>
    </nav>
  </aside>
</template>

<script>
import { authStore } from "@/store/auth";

export default {
  name: "AppSidebar",
  setup() {
    return { authStore };
  },
};
</script>
