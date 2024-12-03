<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Согласования</h1>
      <table class="table-auto w-full border-collapse border border-gray-300">
        <thead class="bg-gray-100">
          <tr>
            <th class="border border-gray-300 px-4 py-2">Дата</th>
            <th class="border border-gray-300 px-4 py-2">Номер заявки</th>
            <th class="border border-gray-300 px-4 py-2">Согласующий</th>
            <th class="border border-gray-300 px-4 py-2">Статус</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="approval in approvals" :key="approval.id">
            <td class="border border-gray-300 px-4 py-2">{{ approval.date }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ approval.ticketNumber }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ approval.approver }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ approval.status }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: "Approvals",
    data() {
      return {
        approvals: [
          { id: 1, date: "2024-01-01", ticketNumber: "T-101", approver: "Иванов", status: "Согласовано" },
          { id: 2, date: "2024-01-02", ticketNumber: "T-102", approver: "Петров", status: "Отклонено" },
        ],
      };
    },
  };
  </script>
  