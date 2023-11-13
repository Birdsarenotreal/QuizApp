<template>
    <Card>
      <template #title>
        <span class="modal-title">Best user: {{ userData.username }}</span>
      </template>
      <template #content>
        <div class="user-info">
          <div class="user-email">Email: {{ userData.email }}</div>
          <div class="user-details">
            <h5>Results</h5>
            <ul class="results-list">
              <li v-for="result in userData.results" :key="result.id" class="result-item">
                <span class="quiz-title">{{ result.quiz.title }}:</span>
                <span class="quiz-score">Score: {{ result.score }}</span>
                <span class="quiz-time">Time: {{ result.time_taken }}</span>
              </li>
            </ul>
          </div>
        </div>
      </template>
    </Card>
</template>

<script setup>
import { ref } from 'vue';
import { useQuiz } from '@/store/modules/quiz';

const quizStore = useQuiz();
const userData = ref(quizStore.topPerformer);

</script>

<style scoped>
.modal-title {
  font-weight: bold;
  font-size: 1.5rem;
  color: #d9e3ec;
}

.user-info {
  display: flex;
  flex-direction: column;
  color: #d9e3ec;
}

.user-email {
  margin-bottom: 1em;
  font-size: 1.1rem;
}

.user-details h5 {
  font-size: 1.2em;
  margin-bottom: 0.5em;
}

.results-list {
  list-style-type: none;
  padding-left: 0;
  margin-left: 0;
}

.result-item {
  background: #ffffff; /* Light background for results */
  color: #2c3e50; /* Dark text for readability */
  margin: 0.5em 0;
  padding: 0.5em;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 5px 0 rgba(44, 62, 80, 0.2);
}

.quiz-title {
  font-weight: bold;
}

.quiz-score, .quiz-time {
  margin-left: 0.5em;
}
</style>
