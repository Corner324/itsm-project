<template>
    <div class="incident-details">
      <h2>Детали инцидента</h2>
      <div class="details">
        <p><strong>Название:</strong> {{ incident.title }}</p>
        <p><strong>Описание:</strong> {{ incident.description }}</p>
        <p><strong>Статус:</strong> {{ incident.status }}</p>
        <p><strong>Дата создания:</strong> {{ incident.created_at }}</p>
        <p><strong>Пользователь:</strong> {{ incident.user }}</p>
      </div>
      <button @click="goBack">Назад</button>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "IncidentDetails",
    data() {
      return {
        incident: {},
      };
    },
    methods: {
      fetchIncident() {
        const id = this.$route.params.id;
        axios
          .get(`http://127.0.0.1:8000/api/incidents/incidents/${id}/`)
          .then((response) => {
            this.incident = response.data;
          });
      },
      goBack() {
        this.$router.push("/incidents");
      },
    },
    mounted() {
      this.fetchIncident();
    },
  };
  </script>
  
  <style scoped>
  .incident-details {
    padding: 20px;
  }
  
  .details p {
    margin: 10px 0;
  }
  </style>
  