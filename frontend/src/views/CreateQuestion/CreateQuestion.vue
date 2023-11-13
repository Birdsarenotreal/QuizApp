<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-6">Create a New Question</h1>
    <form @submit.prevent="submitQuestion">
      <!-- Question Text Field -->
      <div class="mb-6">
        <label for="questionText" class="block text-base font-medium mb-2"
          >Question Text:</label
        >
        <InputText
          id="questionText"
          v-model="questionForm.question_text"
          class="w-full"
          :class="{
            'p-invalid': isSubmitted && !questionForm.question_text.trim(),
          }"
        />
        <small
          v-show="isSubmitted && !questionForm.question_text.trim()"
          class="p-error"
          >Question text is required.</small
        >
      </div>

      <!-- Options Fields -->
      <div
        class="mb-6"
        v-for="(option, index) in questionForm.options"
        :key="index"
      >
        <label :for="'option' + index" class="block text-base font-medium mb-2"
          >Option {{ index + 1 }}:</label
        >
        <InputText
          :id="'option' + index"
          v-model="option.text"
          class="w-full"
          :class="{ 'p-invalid': isSubmitted && !option.text.trim() }"
        />
        <small v-show="isSubmitted && !option.text.trim()" class="p-error"
          >Option text is required.</small
        >
      </div>

      <!-- Correct Answer Field -->
      <div class="mb-6">
        <label class="block text-base font-medium mb-2">Correct Answer:</label>
        <div
          v-for="(option, index) in questionForm.options"
          :key="'correct' + index"
          class="flex items-center mb-2"
        >
          <RadioButton
            v-model="questionForm.correct_answer"
            :value="index + 1"
            :class="{
              'p-invalid': isSubmitted && !questionForm.correct_answer,
            }"
          />
          <label :for="option.text" class="ml-2">{{ option.text }}</label>
        </div>
        <small
          v-show="isSubmitted && !questionForm.correct_answer"
          class="p-error"
          >A correct answer must be selected.</small
        >
      </div>

      <!-- Quiz Dropdown -->
      <div class="mb-6">
        <label for="quiz" class="block text-base font-medium mb-2">Quiz:</label>
        <Dropdown
          id="quiz"
          v-model="questionForm.quiz_id"
          :options="quizzes"
          optionLabel="name"
          optionValue="id"
          placeholder="Select a Quiz"
          :class="{ 'p-invalid': isSubmitted && !questionForm.quiz_id }"
        />
        <small v-show="isSubmitted && !questionForm.quiz_id" class="p-error"
          >Please select a quiz.</small
        >
      </div>

      <!-- Submit Button -->
      <div class="flex justify-end mt-8">
        <Button
          label="Create Question"
          type="submit"
          class="p-button-rounded p-button-success p-button-lg"
          :disabled="!canSubmit"
        />
        <Button
          label="Cancel"
          class="p-button-rounded p-button-success p-button-lg ml-2"
          @click="goHome"
        />
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import QuizApi from "@/api/quiz";
import { useQuiz } from "@/store/modules/quiz";

const quizApi = new QuizApi();
const router = useRouter();
const quizzes = ref([]);
const isSubmitted = ref(false);
const quizStore = useQuiz();

const goHome = () => {
  router.push("/");
};

const questionForm = ref({
  question_text: "",
  options: Array.from({ length: 4 }, () => ({ text: "" })),
  correct_answer: "",
  quiz_id: null,
});

const canSubmit = computed(() => {
  return (
    questionForm.value.question_text.trim() &&
    questionForm.value.options.every((option) => option.text.trim()) &&
    questionForm.value.correct_answer &&
    questionForm.value.quiz_id
  );
});

onMounted(() => {
  quizzes.value = quizStore.quizzes.map((quiz) => ({
    name: quiz.title,
    id: quiz.id,
  }));
});

const submitQuestion = async () => {
  isSubmitted.value = true;
  const optionsString = questionForm.value.options
    .map((option) => option.text)
    .join(",");

  if (!canSubmit.value) {
    console.error("The form is invalid.");
    return;
  }

  const payload = {
    question_text: questionForm.value.question_text,
    options: optionsString,
    correct_answer: questionForm.value.correct_answer.toString(),
    quiz_id: questionForm.value.quiz_id,
  };

  try {
    await quizApi.createQuestion(payload);
    quizStore.enqueueToast({
      severity: "success",
      summary: "Question was added.",
      detail: "Question was successfully added to the quiz.",
      life: 3000, // Duration in milliseconds
    });
    router.push("/");
  } catch (error) {
    console.error("Error creating question:", error);
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
}

.p-error {
  color: var(--danger-color);
  font-size: 0.875em;
}

.p-invalid {
  border: 1px solid var(--danger-color) !important;
}
</style>
