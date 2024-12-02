<template>
  <div class="p-4">
    <FilterControls />
    <table class="table-auto w-full mt-4 border-collapse border border-gray-300">
      <thead class="bg-gray-100">
        <tr>
          <th class="border border-gray-300 px-4 py-2">Date</th>
          <th class="border border-gray-300 px-4 py-2">Number</th>
          <th class="border border-gray-300 px-4 py-2">Status</th>
          <th class="border border-gray-300 px-4 py-2">Ticket Type</th>
          <th class="border border-gray-300 px-4 py-2">Responsible</th>
          <th class="border border-gray-300 px-4 py-2">Team</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ticket in tickets" :key="ticket.id">
          <td class="border border-gray-300 px-4 py-2">{{ ticket.date }}</td>
          <td class="border border-gray-300 px-4 py-2">{{ ticket.number }}</td>
          <td class="border border-gray-300 px-4 py-2">
            <StatusBadge :status="ticket.status" />
          </td>
          <td class="border border-gray-300 px-4 py-2">{{ ticket.type }}</td>
          <td class="border border-gray-300 px-4 py-2">{{ ticket.responsible }}</td>
          <td class="border border-gray-300 px-4 py-2">{{ ticket.team }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import FilterControls from "./FilterControls.vue";
import StatusBadge from "./StatusBadge.vue";

export default {
  name: "TicketTable",
  components: { FilterControls, StatusBadge },
  data() {
    return {
      tickets: [
        {
          id: 1,
          date: "2024-01-01",
          number: "TKT-001",
          status: "New",
          type: "Bug",
          responsible: "John Doe",
          team: "Support",
        },
      ],
    };
  },
};
</script>
