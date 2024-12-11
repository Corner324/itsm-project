<template>
  <aside class="bg-gray-100 text-gray-800 h-full w-60 p-4 shadow-sm">
    <nav class="space-y-2">
      <router-link
        v-for="item in menu"
        :key="item.title"
        :to="item.link"
        class="flex items-center gap-3 p-3 rounded-lg hover:bg-gray-200 hover:text-blue-600 transition"
        :class="{ 'bg-gray-200 text-blue-600': $route.path === item.link }"
      >
        <template v-if="item.icon">
          <component :is="item.icon" class="h-5 w-5 text-gray-500" />
        </template>
        <span class="font-medium">{{ item.title }}</span>
      </router-link>
    </nav>
  </aside>
</template>


<script>
import { authStore } from "@/store/auth";
import { 
  HomeIcon, 
  ChatBubbleBottomCenterIcon, 
  ClipboardDocumentIcon 
} from "@heroicons/vue/24/outline";

export default {
  name: "Sidebar",
  setup() {
    return { authStore };
  },
  computed: {
    menu() {
      const common = [
        { title: "Главная", link: "/dashboard", icon: HomeIcon },
      ];
      const employeeMenu = [
        { title: "Создать заявку", link: "/create-ticket", icon: ClipboardDocumentIcon },
        { title: "Мои заявки", link: "/my-incidents", icon: ClipboardDocumentIcon },
        { title: "Сообщения", link: "/messaging", icon: ChatBubbleBottomCenterIcon },
      ];
      const supportMenu = [
        { title: "Панель техподдержки", link: "/support-dashboard", icon: HomeIcon },
        { title: "Каталог услуг", link: "/service-catalog", icon: ClipboardDocumentIcon },
      ];
      const adminMenu = [
        { title: "Каталог услуг", link: "/service-catalog", icon: ClipboardDocumentIcon },
        { title: "Чаты с сотрудниками", link: "/admin-messages", icon: ChatBubbleBottomCenterIcon },
      ];

      
      if (authStore.user?.role === "employee") return [...common, ...employeeMenu];
      if (authStore.user?.role === "support") return [...common, ...supportMenu];
      if (authStore.user?.role === "admin") return [...common, ...adminMenu];
      return common;
    },
  },
};
</script>

<style scoped>
aside {
  background-color: #f7f9fc; /* Светло-серый фон */
  border-right: 1px solid #e0e0e0; /* Лёгкая граница для разделения */
}

router-link {
  color: #374151; /* Нейтральный серый цвет текста */
}

router-link.active {
  background-color: #e0e7ff; /* Мягкий акцент для активного элемента */
  color: #2563eb; /* Акцентный синий */
}

router-link:hover {
  background-color: #f3f4f6; /* Светло-серый при наведении */
  color: #2563eb; /* Синий цвет текста при наведении */
}
</style>
