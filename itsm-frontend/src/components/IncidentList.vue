<template>
  <div>
    <h2>Список инцидентов</h2>
    <ul>
      <li v-for="incident in incidents" :key="incident.id">
        <strong>{{ incident.title }}</strong>: {{ incident.description }} ({{ incident.status }})
      </li>
    </ul>
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
  created() {
    axios
      .get("http://127.0.0.1:8000/api/incidents/incidents/")
      .then((response) => {
        this.incidents = response.data;
      })
      .catch((error) => {
        console.error("Ошибка загрузки списка инцидентов:", error);
      });
  },
};
</script>
