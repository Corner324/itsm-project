<template>
  <div id="app">
    <header>
      <nav>
        <router-link to="/services">Каталог услуг</router-link> |
        <router-link to="/incidents">Инциденты</router-link> |
        <router-link to="/messages">Сообщения</router-link>
      </nav>
    </header>
    <router-view /> <!-- Важно: этот тег отвечает за отображение компонентов маршрутов -->
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

header nav a {
  color: #007bff;
  text-decoration: none;
  margin: 0 15px;
}

header nav a:hover {
  text-decoration: underline;
}
</style>
