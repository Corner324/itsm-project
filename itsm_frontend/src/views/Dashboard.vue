<template>
  <div class="p-6">
    <!-- Приветствие -->
    <h1 class="text-3xl font-bold mb-4">Добро пожаловать, {{ authStore.user?.username }}!</h1>
    <p class="text-gray-600 mb-8">Роль: {{ formatRole(authStore.user?.role) }}</p>

    <!-- Карточки модулей -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div
        v-for="item in menu"
        :key="item.title"
        class="p-6 bg-white shadow rounded-lg hover:shadow-lg transition"
      >
        <div class="flex items-center gap-3 mb-4">
          <component :is="item.icon" class="h-6 w-6 text-blue-600" v-if="item.icon" />
          <h2 class="text-xl font-semibold">{{ item.title }}</h2>
        </div>
        <p class="text-gray-600 mb-4">{{ item.description }}</p>
        <router-link
          :to="item.link"
          class="inline-block px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Перейти
        </router-link>
      </div>
    </div>

    <!-- Статистика -->
    <div class="mt-10 grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="p-6 bg-blue-100 shadow rounded-lg">
        <h3 class="text-lg font-semibold mb-2">Активные заявки</h3>
        <p class="text-4xl font-bold text-blue-600">{{ stats.incidents }}</p>
      </div>
      <div class="p-6 bg-green-100 shadow rounded-lg">
        <h3 class="text-lg font-semibold mb-2">Каталог услуг</h3>
        <p class="text-4xl font-bold text-green-600">{{ stats.services }}</p>
      </div>
      <div class="p-6 bg-yellow-100 shadow rounded-lg">
        <h3 class="text-lg font-semibold mb-2">Новые сообщения</h3>
        <p class="text-4xl font-bold text-yellow-600">{{ stats.messages }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { authStore } from "@/store/auth";
import {
  HomeIcon,
  ChatBubbleBottomCenterIcon,
  ClipboardDocumentIcon,
} from "@heroicons/vue/24/outline";
import axios from "axios";

export default {
  name: "Dashboard",
  data() {
    return {
      stats: {
        incidents: 0,
        services: 0,
        messages: 0,
      },
    };
  },
  computed: {
    menu() {
      const common = [
        {
          title: "Главная",
          description: "Обзор системы.",
          link: "/dashboard",
          icon: HomeIcon,
        },
      ];
      const employeeMenu = [
        {
          title: "Создать заявку",
          description: "Создавайте и отслеживайте свои заявки.",
          link: "/create-ticket",
          icon: ClipboardDocumentIcon,
        },
        {
          title: "Мои заявки",
          description: "Просматривайте и управляйте вашими заявками.",
          link: "/my-incidents",
          icon: ClipboardDocumentIcon,
        },
        {
          title: "Сообщения",
          description: "Общайтесь с администрацией через сообщения.",
          link: "/messaging",
          icon: ChatBubbleBottomCenterIcon,
        },
      ];
      const supportMenu = [
        {
          title: "Панель техподдержки",
          description: "Управляйте инцидентами и решайте проблемы.",
          link: "/support-dashboard",
          icon: HomeIcon,
        },
        {
          title: "Каталог услуг",
          description: "Редактируйте и управляйте каталогом услуг.",
          link: "/service-catalog",
          icon: ClipboardDocumentIcon,
        },
      ];
      const adminMenu = [
        {
          title: "Панель техподдержки",
          description: "Контролируйте все действия в системе.",
          link: "/support-dashboard",
          icon: HomeIcon,
        },
        {
          title: "Каталог услуг",
          description: "Обновляйте и поддерживайте актуальность услуг.",
          link: "/service-catalog",
          icon: ClipboardDocumentIcon,
        },
        {
          title: "Чаты с сотрудниками",
          description: "Просматривайте и отвечайте на сообщения.",
          link: "/admin-messages",
          icon: ChatBubbleBottomCenterIcon,
        },
      ];

      
      if (authStore.user?.role === "employee") return [ ...employeeMenu];
      if (authStore.user?.role === "support") return [ ...supportMenu];
      if (authStore.user?.role === "admin") return [ ...adminMenu];
      return common;
    },
  },
  async created() {
    const token = localStorage.getItem("accessToken");
    try {
      const [incidentsResponse, servicesResponse, messagesResponse] = await Promise.all([
        axios.get("http://127.0.0.1:8000/api/incidents/my/", {
          headers: { Authorization: `Bearer ${token}` },
        }),
        axios.get("http://127.0.0.1:8000/api/services/", {
          headers: { Authorization: `Bearer ${token}` },
        }),
        axios.get("http://127.0.0.1:8000/api/messaging/", {
          headers: { Authorization: `Bearer ${token}` },
        }),
      ]);
      this.stats.incidents = incidentsResponse.data.length;
      this.stats.services = servicesResponse.data.length;
      this.stats.messages = messagesResponse.data.filter((msg) => !msg.is_read).length;
    } catch (error) {
      console.error("Ошибка загрузки статистики:", error);
    }
  },
  setup() {
    return { authStore };
  },
  methods: {
    formatRole(role) {
      const roles = {
        employee: "Сотрудник",
        support: "Техподдержка",
        admin: "Администратор",
      };
      return roles[role] || "Неизвестная роль";
    },
  },
};
</script>
