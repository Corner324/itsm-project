<template>
  <div>
    <h1 class="text-2xl font-bold">Добро пожаловать!</h1>
    <!-- Проверяем, определён ли authStore.user -->
    <p v-if="authStore.user">
      Привет, {{ authStore.user.username }}! Ваша роль: {{ getTranslatedRole(authStore.user.role) }}.
    </p>
    <p v-else>
      Загрузка информации о пользователе...
    </p>
  </div>
</template>

<script>
import { authStore } from "@/store/auth";

export default {
  name: "Dashboard",
  setup() {
    const roleTranslation = {
      employee: "Сотрудник",
      support: "Техподдержка",
    };

    const getTranslatedRole = (role) => roleTranslation[role] || "Неизвестная роль";

    return { authStore, getTranslatedRole };
  },
};
</script>

  
  <style scoped>
  .dashboard {
    text-align: center;
    padding: 50px;
  }
  
  .navigation {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
  }
  
  .link {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
  }
  
  .link:hover {
    background-color: #0056b3;
  }
  </style>
  