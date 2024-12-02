<template>
    <div class="flex items-center gap-4 mb-4">
      <div>
        <label for="status" class="block text-sm font-medium text-gray-700">Статус</label>
        <select
          id="status"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          v-model="filters.status"
          @change="applyFilters"
        >
          <option value="">Все</option>
          <option value="new">Новый</option>
          <option value="in_progress">В работе</option>
          <option value="completed">Завершён</option>
        </select>
      </div>
      <div>
        <label for="date" class="block text-sm font-medium text-gray-700">Дата</label>
        <input
          type="date"
          id="date"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          v-model="filters.date"
          @change="applyFilters"
        />
      </div>
      <button
        class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md shadow hover:bg-blue-700"
        @click="resetFilters"
      >
        Сбросить фильтры
      </button>
    </div>
  </template>
  
  <script>
  export default {
    name: "FilterControls",
    data() {
      return {
        filters: {
          status: "",
          date: "",
        },
      };
    },
    methods: {
      applyFilters() {
        this.$emit("filter-changed", this.filters);
      },
      resetFilters() {
        this.filters = { status: "", date: "" };
        this.applyFilters();
      },
    },
  };
  </script>
  