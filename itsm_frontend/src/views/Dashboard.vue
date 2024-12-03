<template>
    <div class="dashboard">
      <h1>ITSM-Система</h1>
      <p>Выберите раздел:</p>
      <div class="navigation">
        <router-link to="/services" class="link">Каталог услуг</router-link>
        <router-link to="/incidents" class="link">Инциденты</router-link>
        <router-link to="/messages" class="link">Мессенджер</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "DashboardView",
  };
  </script>
  
  <style scoped>
  .dashboard {
    text-align: center;
    padding: 50px;
  }
  
  .navigation {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
  }
  
  .link {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
  }
  
  .link:hover {
    background-color: #0056b3;
  }
  </style>
  