<template>
  <aside class="bg-gray-100 h-full w-60 p-4">
    <nav class="flex flex-col gap-2">
      <router-link to="/tickets" class="hover:text-blue-600">В зоне ответственности</router-link>
      <router-link to="/outgoing" class="hover:text-blue-600">Исходящие</router-link>
      <router-link to="/create-ticket" class="hover:text-blue-600">Создать заявку</router-link>
      <router-link to="/subscriptions" class="hover:text-blue-600">Подписки</router-link>
      <router-link to="/approvals" class="hover:text-blue-600">Согласования</router-link>
      <router-link to="/reports" class="hover:text-blue-600">Отчёты</router-link>
    </nav>
  </aside>
</template>

<script>
export default {
  name: "AppSidebar",
};
</script>
