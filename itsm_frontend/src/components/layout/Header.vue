<template>
<header class="text-white p-4 flex justify-between items-center" style="background-color: #085896;">
    <div class="flex items-center gap-4">
      <img src="/logo.png" alt="Logo" class="h-8" />
      <h1 class="text-lg font-bold">ITSM | BPMIntegrator</h1>
    </div>
    <nav class="flex gap-4">
      <!-- Если пользователь авторизован -->
      <template v-if="authStore.isAuthenticated">
        <span>Привет, {{getTranslatedRole(authStore.user?.role) }} {{authStore.user?.username }}!</span>
        <a href="#" @click.prevent="logout" class="hover:underline">Выйти</a>
      </template>

      <!-- Если пользователь НЕ авторизован -->
      <template v-else>
        <router-link to="/login" class="hover:underline">Войти</router-link>
        <router-link to="/register" class="hover:underline">Регистрация</router-link>
      </template>
    </nav>
  </header>
</template>

<script>
import { authStore } from "@/store/auth";



export default {
  name: "AppHeader",
  setup() {
    const roleTranslation = {
      employee: "сотрудник",
      support: "специалист",
    };

    
    const getTranslatedRole = (role) => roleTranslation[role] || "";

    const logout = () => {
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      authStore.setAuth(false);
      window.location.href = "/welcome";
    };

    return { authStore, logout, getTranslatedRole };
  },
};
</script>