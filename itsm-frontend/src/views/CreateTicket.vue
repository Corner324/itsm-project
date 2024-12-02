<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Создать заявку</h1>
      <form class="space-y-4">
        <div>
          <label for="title" class="block text-sm font-medium text-gray-700">Название заявки</label>
          <input type="text" id="title" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm" placeholder="Введите название" />
        </div>
        <div>
          <label for="description" class="block text-sm font-medium text-gray-700">Описание</label>
          <textarea id="description" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm" placeholder="Введите описание"></textarea>
        </div>
        <div>
          <label for="receiver" class="block text-sm font-medium text-gray-700">Получатель</label>
          <input type="text" id="receiver" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm" placeholder="Введите получателя" />
        </div>
        <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">Создать</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "CreateTicket",
  };
  </script>
  