import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/Dashboard.vue";
import TicketTable from "../components/features/TicketTable.vue";
import NotFound from "../views/NotFound.vue"; // Страница 404

const routes = [
  { path: "/", component: DashboardView, name: "Dashboard" },
  { path: "/tickets", component: TicketTable, name: "Tickets" },
  { path: "/outgoing", component: () => import("../views/Outgoing.vue"), name: "Outgoing" },
  { path: "/create-ticket", component: () => import("../views/CreateTicket.vue"), name: "CreateTicket" },
  { path: "/subscriptions", component: () => import("../views/Subscriptions.vue"), name: "Subscriptions" },
  { path: "/approvals", component: () => import("../views/Approvals.vue"), name: "Approvals" },
  { path: "/reports", component: () => import("../views/Reports.vue"), name: "Reports" },
  // Заглушка для несуществующих маршрутов
  { path: "/:pathMatch(.*)*", component: NotFound, name: "NotFound" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
