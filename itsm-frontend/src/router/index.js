import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/Dashboard.vue";
import ServiceCatalog from "../components/ServiceCatalog.vue";
import IncidentList from "../components/IncidentList.vue";
import MessageList from "../components/MessageList.vue";

// Определяем маршруты
const routes = [
  { path: "/", component: DashboardView },
  { path: "/services", component: ServiceCatalog },
  { path: "/incidents", component: IncidentList },
  { path: "/messages", component: MessageList },
];

// Создаём экземпляр маршрутизатора
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
