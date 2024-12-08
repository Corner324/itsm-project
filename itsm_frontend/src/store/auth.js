import { reactive } from "vue";

export const authStore = reactive({
  isAuthenticated: false,
  user: null, // Хранит имя пользователя и роль
  setAuth(isAuth, user = null) {
    this.isAuthenticated = isAuth;
    this.user = user; // Пример: { username: "john_doe", role: "support" }
  },
  hasRole(role) {
    return this.user?.role === role; // Проверка роли
  },
});