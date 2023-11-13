<template>
  <div class="text-center mb-2 text-2xl">Select Quiz</div>
  <div class="text-center">
              <SelectButton
                text raised rounded class="large"
                severity="info"
                v-model="state.selectQuiz"
                :options="filteredQuizTitles"
                aria-labelledby="basic"
                :pt="{ button: 'm-1' }"
                @update:modelValue="handleSelection"
              />
          </div>
</template>

<script setup>
import { reactive, computed, watch } from 'vue';
import { useQuiz } from '@/store/modules/quiz';

const quizStore = useQuiz();

const state = reactive({
  selectQuiz: null,
});

const filteredQuizTitles = computed(() => {
  let filtered = quizStore.quizzes;

  if (quizStore.selectedCategory) {
    filtered = filtered.filter(quiz => quiz.category.name === quizStore.selectedCategory);
  }
  if (quizStore.selectedDifficulty) {
    filtered = filtered.filter(quiz => quiz.difficulty === quizStore.selectedDifficulty);
  }
  const titles = filtered.map(quiz => quiz.title);
  return [...new Set(titles)];
});

const handleSelection = (newQuizTitle) => {
  if (newQuizTitle) {
    const selectedQuiz = filteredQuizTitles.value.find(quizTitle => quizTitle === newQuizTitle);
    const fullQuizDetails = quizStore.quizzes.find(quiz => quiz.title === selectedQuiz);
    quizStore.setSelectedQuiz(fullQuizDetails);
  } else {
    quizStore.setSelectedQuiz(null);
  }
};
</script>
