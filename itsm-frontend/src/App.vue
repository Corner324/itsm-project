<template>
  <div class="flex">
    <Sidebar />
    <div class="flex-1">
      <Header />
      <Breadcrumbs />
      <TicketTable />
    </div>
  </div>
</template>

<script>
import Header from "@/components/layout/Header.vue";
import Sidebar from "@/components/layout/Sidebar.vue";
import Breadcrumbs from "@/components/layout/Breadcrumbs.vue";
import TicketTable from "@/components/features/TicketTable.vue";

export default {
  name: "App",
  components: { Header, Sidebar, Breadcrumbs, TicketTable },
};
</script>
