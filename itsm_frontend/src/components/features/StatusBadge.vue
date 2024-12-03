<template>
    <span
      :class="[
        'px-2 inline-flex text-xs leading-5 font-semibold rounded-full',
        statusClass,
      ]"
    >
      {{ status }}
    </span>
  </template>
  
  <script>
  export default {
    name: "StatusBadge",
    props: {
      status: {
        type: String,
        required: true,
      },
    },
    computed: {
      statusClass() {
        switch (this.status.toLowerCase()) {
          case "new":
            return "bg-red-100 text-red-800";
          case "in_progress":
            return "bg-yellow-100 text-yellow-800";
          case "completed":
            return "bg-green-100 text-green-800";
          default:
            return "bg-gray-100 text-gray-800";
        }
      },
    },
  };
  </script>
  
  <style scoped>
  </style>
  