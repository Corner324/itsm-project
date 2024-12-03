<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Исходящие заявки</h1>
      <table class="table-auto w-full border-collapse border border-gray-300">
        <thead class="bg-gray-100">
          <tr>
            <th class="border border-gray-300 px-4 py-2">Дата</th>
            <th class="border border-gray-300 px-4 py-2">Номер</th>
            <th class="border border-gray-300 px-4 py-2">Получатель</th>
            <th class="border border-gray-300 px-4 py-2">Описание</th>
            <th class="border border-gray-300 px-4 py-2">Статус</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="ticket in tickets" :key="ticket.id">
            <td class="border border-gray-300 px-4 py-2">{{ ticket.date }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ ticket.number }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ ticket.receiver }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ ticket.description }}</td>
            <td class="border border-gray-300 px-4 py-2">
              <span :class="getStatusClass(ticket.status)">{{ ticket.status }}</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: "Outgoing",
    data() {
      return {
        tickets: [
          { id: 1, date: "2024-01-01", number: "T-101", receiver: "Иванов", description: "Запрос на обновление ПО", status: "В работе" },
          { id: 2, date: "2024-01-02", number: "T-102", receiver: "Петров", description: "Установка нового сервера", status: "Завершён" },
        ],
      };
    },
    methods: {
      getStatusClass(status) {
        switch (status) {
          case "В работе":
            return "text-yellow-500 font-semibold";
          case "Завершён":
            return "text-green-500 font-semibold";
          default:
            return "text-gray-500";
        }
      },
    },
  };
  </script>
  