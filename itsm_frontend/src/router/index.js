import { createRouter, createWebHistory } from "vue-router";
import { authStore } from "@/store/auth";
import DashboardView from "../views/Dashboard.vue";
import TicketTable from "../components/features/TicketTable.vue";
import NotFound from "../views/NotFound.vue"; // Страница 404
import Registration from "@/views/Registration.vue";
import Login from "@/views/Login.vue";
import Welcome from "@/views/Welcome.vue";

const routes = [
  { path: "/", component: DashboardView, name: "Dashboard", meta: { requiresAuth: true } },
  { path: "/welcome", component: Welcome, name: "Welcome", meta: { requiresGuest: true } },
  { path: "/tickets", component: TicketTable, name: "Tickets", meta: { requiresAuth: true } },
  { path: "/outgoing", component: () => import("../views/Outgoing.vue"), name: "Outgoing", meta: { requiresAuth: true } },
  { path: "/create-ticket", component: () => import("../views/CreateTicket.vue"), name: "CreateTicket", meta: { requiresAuth: true } },
  { path: "/subscriptions", component: () => import("../views/Subscriptions.vue"), name: "Subscriptions", meta: { requiresAuth: true } },
  { path: "/approvals", component: () => import("../views/Approvals.vue"), name: "Approvals", meta: { requiresAuth: true } },
  { path: "/reports", component: () => import("../views/Reports.vue"), name: "Reports", meta: { requiresAuth: true } },
  { path: "/register", component: Registration, name: "Register", meta: { requiresGuest: true } },
  { path: "/login", component: Login, name: "Login", meta: { requiresGuest: true } },
  // Заглушка для несуществующих маршрутов
  { path: "/:pathMatch(.*)*", component: NotFound, name: "NotFound" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Добавляем глобальный guard
router.beforeEach((to, from, next) => {
  // Если маршрут требует авторизации
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/login"); // Перенаправляем на логин, если пользователь не авторизован
  }
  // Если маршрут доступен только для гостей (неавторизованных пользователей)
  else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next("/"); // Перенаправляем на главную, если пользователь уже авторизован
  } else {
    next(); // Разрешаем переход
  }
});

export default router;
