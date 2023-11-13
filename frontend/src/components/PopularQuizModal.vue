<template>
  <div class="modal-content">
    <div class="p-fluid">
      <div class="p-field custom-field">
        <label for="title" class="custom-label">Title</label>
        <InputText id="title" v-model="popularQuiz.title" readonly class="custom-input" />
      </div>
      <div class="p-field custom-field">
        <label for="description" class="custom-label">Description</label>
        <div id="description" class="custom-textarea custom-text-display" readonly>
          {{ popularQuiz.description || 'No description provided' }}
        </div>
      </div>
      <div class="p-field custom-field">
        <label for="category" class="custom-label">Category</label>
        <InputText id="category" v-model="popularQuiz.category.name" readonly class="custom-input" />
      </div>
      <div class="p-field custom-field">
        <label for="difficulty" class="custom-label">Difficulty</label>
        <InputText id="difficulty" v-model="popularQuiz.difficulty" readonly class="custom-input" />
      </div>
      <Button label="Take Quiz" @click="startQuiz" class="custom-button" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useQuiz } from '@/store/modules/quiz';

const router = useRouter();
const quizStore = useQuiz();
const popularQuiz = ref(
  quizStore.popularQuiz
);

const startQuiz = () => {
  quizStore.setQuizStatus('STARTED');
  quizStore.setSelectedQuiz(popularQuiz.value); // Make sure to set the selectedQuiz before navigating
  router.push({ name: 'Quiz', params: { id: popularQuiz.value.id } });
};
</script>

<style scoped>
.modal-content {
  background: #2c3e50; /* Adjust the background color to your preference */
  border-radius: 8px;
  padding: 20px;
  color: #ecf0f1; /* Light text color for better contrast */
}

.custom-field {
  margin-bottom: 1rem;
}

.custom-label {
  color: #7f8c8d;
  font-weight: bold;
  margin-bottom: .5rem;
}

.custom-input,
.custom-textarea {
  background-color: #34495e; /* Darker background for inputs */
  border: none;
  color: #ecf0f1; /* Light text color */
  padding: 10px;
  border-radius: 4px;
  width: 100%; /* Full width */
}

.custom-input::placeholder,
.custom-textarea::placeholder {
  color: #95a5a6;
}

.custom-button {
  background-color: #16a085; /* Vibrant color for the main action */
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.custom-text-display {
  padding: 10px;
  background-color: #34495e; /* Background color */
  border-radius: 4px;
  color: #ecf0f1; /* Text color */
  overflow-y: auto; /* Allows scrolling for overflow text */
  height: auto; /* Adjust height as necessary */
  max-height: 200px; /* Maximum height before scrolling */
  white-space: pre-wrap; /* Maintains whitespace and line breaks */
  word-wrap: break-word; /* Ensures long words do not overflow */
}

.custom-button:hover {
  background-color: #1abc9c; /* Slightly lighter color on hover */
}
</style>