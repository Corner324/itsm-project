<template>
    <div class="dashboard">
      <h1>Добро пожаловать в ITSM-систему</h1>
      <p>Выберите один из модулей:</p>
      <ul>
        <li><router-link to="/services">Каталог услуг</router-link></li>
        <li><router-link to="/incidents">Инциденты</router-link></li>
        <li><router-link to="/messages">Сообщения</router-link></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "DashboardView", // Изменили имя компонента
  };
  </script>
  
  <style scoped>
  .dashboard {
    text-align: center;
    padding: 20px;
  }
  
  .dashboard ul {
    list-style: none;
    padding: 0;
  }
  
  .dashboard li {
    margin: 10px 0;
  }
  
  .dashboard li a {
    color: #007bff;
    text-decoration: none;
  }
  
  .dashboard li a:hover {
    text-decoration: underline;
  }
  </style>
  