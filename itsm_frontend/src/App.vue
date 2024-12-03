<template>
  <div id="app">
    <header>
      <AppHeader /> <!-- Ваша шапка -->
    </header>
    <div class="flex">
      <AppSidebar /> <!-- Боковая панель -->
      <main class="flex-1 p-4">
        <router-view /> <!-- Рендер текущего маршрута -->
      </main>
    </div>
  </div>
</template>

<script>
import AppHeader from "@/components/layout/Header.vue";
import AppSidebar from "@/components/layout/Sidebar.vue";

export default {
  name: "App",
  components: {
    AppHeader,
    AppSidebar,
  },
};
</script>

<style>
/* Пример глобальных стилей */
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>
