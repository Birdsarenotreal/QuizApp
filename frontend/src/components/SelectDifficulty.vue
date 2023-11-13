<template>
  <div class="mb-2 text-center text-2xl mt-6">Difficulty</div>
  <div class="grid text-center">
        <div class="col" v-for="difficulty in state.difficulties" :key="difficulty">
          <Button
            text raised rounded class="large"
            severity="info"
            :class="{ 'btn-selected': difficulty === quizStore.selectedDifficulty }"
            @click="selectDifficulty(difficulty)"
            :label="difficulty"
          />
        </div>
      </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useQuiz } from '@/store/modules/quiz';

const quizStore = useQuiz();

const state = reactive({
  difficulties: ["Easy", "Medium", "Hard"],
});

const selectDifficulty = (difficulty) => {
  if (quizStore.selectedDifficulty === difficulty) {
    quizStore.setDifficulty(null);
  } else {
    quizStore.setDifficulty(difficulty);
  }
};
</script>

<style scoped>
.btn-selected {
  background-color: #f9fafc;
}
</style>
