import { createRouter, createWebHistory } from "vue-router";
import { authStore } from "@/store/auth";
import Welcome from "@/views/Welcome.vue";
import DashboardView from "@/views/Dashboard.vue";
import NotFound from "@/views/NotFound.vue";
import Login from "@/views/Login.vue";
import Registration from "@/views/Registration.vue";
import CreateTicket from "@/views/CreateTicket.vue";
import SupportDashboard from "@/views/SupportDashboard.vue";
// import IncidentList from "@/components/IncidentList.vue";
import MyIncidents from "@/views/MyIncidents.vue";
import IncidentDetails from "@/components/IncidentDetails.vue";
import IncidentsList from "@/components/IncidentList.vue";
import Approvals from "@/views/Approvals.vue";
import Outgoing from "@/views/Outgoing.vue";
import Subscriptions from "@/views/Subscriptions.vue";
import Reports from "@/views/Reports.vue";

import ServiceCatalog from "@/views/ServiceCatalog.vue"; // Список услуг
import CreateService from "@/views/CreateService.vue"; // Создание услуги
import EditService from "@/views/EditService.vue"; // Редактирование услуги

const routes = [
  // Страница приветствия
  {
    path: "/welcome",
    component: Welcome,
    name: "Welcome",
    meta: { requiresGuest: true },
  },
  // Авторизация и регистрация
  {
    path: "/login",
    component: Login,
    name: "Login",
    meta: { requiresGuest: true },
  },
  {
    path: "/register",
    component: Registration,
    name: "Register",
    meta: { requiresGuest: true },
  },
  // Главная страница
  {
    path: "/dashboard",
    component: DashboardView,
    name: "Dashboard",
    meta: { requiresAuth: true },
  },
  // Для сотрудников
  {
    path: "/create-ticket",
    component: CreateTicket,
    name: "CreateTicket",
    meta: { requiresAuth: true, role: "employee" },
  },
  {
    path: "/my-incidents",
    component: MyIncidents,
    name: "MyIncidents",
    meta: { requiresAuth: true, role: "employee" },
  }, 
  // Для специалистов поддержки
  {
    path: "/support-dashboard",
    component: SupportDashboard,
    name: "SupportDashboard",
    meta: { requiresAuth: true, role: "support" },
  },
  {
    path: "/incidents",
    component: IncidentsList,
    name: "IncidentsList",
    meta: { requiresAuth: true, role: "support" },
  },
  {
    path: "/incident/:id",
    component: IncidentDetails,
    name: "IncidentDetails",
    props: true,
  },
  // Другие страницы
  {
    path: "/approvals",
    component: Approvals,
    name: "Approvals",
    meta: { requiresAuth: true },
  },
  {
    path: "/outgoing",
    component: Outgoing,
    name: "Outgoing",
    meta: { requiresAuth: true },
  },
  {
    path: "/subscriptions",
    component: Subscriptions,
    name: "Subscriptions",
    meta: { requiresAuth: true },
  },
  {
    path: "/reports",
    component: Reports,
    name: "Reports",
    meta: { requiresAuth: true },
  },
  {
    path: "/service-catalog",
    component: ServiceCatalog,
    name: "ServiceCatalog",
  },
  {
    path: "/service-catalog/create",
    component: CreateService,
    name: "CreateService",
  },
  {
    path: "/service-catalog/edit/:id",
    component: EditService,
    name: "EditService",
    props: true, // Передаём ID как пропс
  },
  // Страница 404
  {
    path: "/:pathMatch(.*)*",
    component: NotFound,
    name: "NotFound",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Проверка аутентификации и ролей
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/login");
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next("/dashboard");
  } else if (to.meta.role && authStore.user?.role !== to.meta.role) {
    next("/dashboard");
  } else {
    next();
  }
});

export default router;
