<template>
  <div class="text-center mb-2 text-2xl">Select Category</div>
  <div class="text-center">
    <SelectButton
      text
      raised
      rounded
      class="large categories-identifier"
      severity="info"
      v-model="state.selectCategory"
      :options="uniqueCategories"
      aria-labelledby="basic"
    />
  </div>
</template>

<script setup>
import { reactive, computed, watch } from 'vue';
import { useQuiz } from '@/store/modules/quiz';

const quizStore = useQuiz();

const state = reactive({
    selectCategory: null,
});

// Computed property to get unique categories
const uniqueCategories = computed(() => {
  const categoryNames = quizStore.categories.map(c => c.name);
  return [...new Set(categoryNames)];
});

// Watcher to respond to selection changes
watch(
  () => state.selectCategory,
  async (value) => {
    quizStore.setCategory(value);
  }
);
</script>
