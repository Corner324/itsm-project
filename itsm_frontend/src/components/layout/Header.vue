<template>
  <header class="text-white p-4 flex justify-between items-center" style="background-color: #085896;">
    <div class="flex items-center gap-4">
      <img src="/logo.png" alt="Logo" class="h-8" />
      <router-link to="/" class="text-lg font-bold">Service Desk</router-link>
    </div>
    <nav class="flex gap-4">
      <router-link to="/login" class="hover:underline">Войти</router-link>
      <router-link to="/register" class="hover:underline">Зарегистрироваться</router-link>
      <router-link to="/" class="hover:underline">Главная</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
/* Добавим небольшой отступ между картинкой и текстом */
img {
  max-height: 2rem; /* Ограничение высоты картинки */
}
</style>
