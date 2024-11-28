<template>
  <div>
    <h2>Каталог услуг</h2>
    <ul>
      <li v-for="service in services" :key="service.id">
        <strong>{{ service.name }}</strong>: {{ service.description }} ({{ service.status }})
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ServiceCatalog",
  data() {
    return {
      services: [],
    };
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/catalog/services/")
      .then((response) => {
        this.services = response.data;
      })
      .catch((error) => {
        console.error("Ошибка загрузки каталога услуг:", error);
      });
  },
};
</script>
