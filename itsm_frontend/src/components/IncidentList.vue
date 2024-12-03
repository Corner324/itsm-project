<template>
  <div class="incident-list">
    <h2>Список инцидентов</h2>
    <table>
      <thead>
        <tr>
          <th>Название</th>
          <th>Описание</th>
          <th>Статус</th>
          <th>Дата создания</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="incident in incidents" :key="incident.id">
          <td>{{ incident.title }}</td>
          <td>{{ incident.description }}</td>
          <td>{{ incident.status }}</td>
          <td>{{ incident.created_at }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "IncidentList",
  data() {
    return {
      incidents: [],
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/api/incidents/incidents/").then((response) => {
      this.incidents = response.data;
    });
  },
};
</script>

<style scoped>
.incident-list table {
  width: 100%;
  border-collapse: collapse;
}

.incident-list th,
.incident-list td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.incident-list th {
  background-color: #007bff;
  color: white;
}
</style>
