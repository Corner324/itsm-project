import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/Dashboard.vue";
import ServiceCatalog from "../components/ServiceCatalog.vue";
import IncidentList from "../components/IncidentList.vue";
import MessageList from "../components/MessageList.vue";
import IncidentDetails from "../components/IncidentDetails.vue";

// Определяем маршруты
const routes = [
  { path: "/", component: DashboardView },
  { path: "/services", component: ServiceCatalog },
  { path: "/incidents", component: IncidentList },
  { path: "/messages", component: MessageList },
  { path: "/incidents/:id", component: IncidentDetails },
];

// Создаём экземпляр маршрутизатора
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
