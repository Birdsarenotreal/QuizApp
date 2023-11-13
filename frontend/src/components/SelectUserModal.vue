<template>
  <div class="mb-6 modal-window">
    <label for="userSelect" class="block text-base font-medium mb-2"
      >User:</label
    >
    <Dropdown
      id="userSelect"
      v-model="selectedUserId"
      :options="simpleUsers"
      optionLabel="name"
      optionValue="id"
      placeholder="Select a User"
      :class="{ 'p-invalid w-full ': isSubmitted && !selectedUserId }"
    />
    <small v-show="isSubmitted && !selectedUserId" class="p-error"
      >Please select a user.</small
    >
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useQuiz } from "@/store/modules/quiz";

const quizStore = useQuiz();
const isSubmitted = ref(false);

// Mapping users to simpler objects for the dropdown
const simpleUsers = quizStore.users.map((u) => ({
  id: u.id,
  name: u.username,
}));

const selectedUserId = computed({
  get: () => (quizStore.selectedUser ? quizStore.selectedUser.id : null),
  set: (id) => {
    const user = quizStore.users.find((u) => u.id === id);
    quizStore.setSelectedUser(user);
  },
});
</script>

<style scoped>
.modal-window {
    min-width: 300px;
}

.modal-window > div {
    width: 100%;
}
</style>
