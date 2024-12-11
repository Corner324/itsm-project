import { reactive } from "vue";

const STORAGE_KEY = "authState";

function loadAuthState() {
  const savedState = localStorage.getItem(STORAGE_KEY);
  return savedState ? JSON.parse(savedState) : { isAuthenticated: false, user: null };
}

export const authStore = reactive({
  ...loadAuthState(), 

  setAuth(isAuth, user = null) {
    this.isAuthenticated = isAuth;
    this.user = user;

    localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify({ isAuthenticated: this.isAuthenticated, user: this.user })
    );
  },

  hasRole(role) {
    return this.user?.role === role;
  },

  logout() {
    this.setAuth(false, null);
  },
});
