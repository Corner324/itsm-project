import { createRouter, createWebHistory } from "vue-router";
import PublicReportForm from "@/views/PublicReportForm.vue"; // Убедитесь, что путь к компоненту правильный

const routes = [
  {
    path: "/",
    name: "PublicReportForm",
    component: PublicReportForm,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
