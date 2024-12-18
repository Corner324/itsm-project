<template>
  <div id="app" class="min-h-screen flex flex-col bg-gray-100">
    <!-- Хедер -->
    <header class="bg-blue-600 text-white p-4 shadow">
      <div class="container mx-auto">
        <h1 class="text-xl font-bold">Отчет об инциденте</h1>
      </div>
    </header>

    <!-- Основной контент -->
    <main class="flex-1">
      <router-view /> <!-- Подключение маршрутов -->
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: 'Arial', sans-serif;
  color: #374151;
}
</style>
