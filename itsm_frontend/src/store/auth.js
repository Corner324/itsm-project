import { reactive } from "vue";

export const authStore = reactive({
  isAuthenticated: false,
  user: null,
  setAuth(isAuth, user = null) {
    this.isAuthenticated = isAuth;
    this.user = user;
  },
});