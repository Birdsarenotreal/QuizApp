<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-6">Add Questions to Quiz</h1>

    <div
      v-for="(questionForm, index) in questionForms"
      :key="index"
      class="mb-6"
    >
      <CreateQuestion
        :question="questionForm"
        @update-question="updateQuestion(index, $event)"
      />
      <Button
        label="Remove Question"
        @click="removeQuestionForm(index)"
        class="p-button-danger mt-2 ml-4"
      />
    </div>

    <Button
      label="Add Another Question"
      @click="addQuestionForm"
      class="p-button-success mt-4 ml-4"
    />
    <Button
      label="Submit"
      @click="submitAllQuestions"
      class="p-button-info mt-4 ml-4"
      :disabled="!allQuestionsValid"
    />
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import QuizApi from "@/api/quiz";
import CreateQuestion from "@/components/CreateQuestion.vue";
import Button from "primevue/button";
import { useQuiz } from "@/store/modules/quiz";

const quizStore = useQuiz();
const router = useRouter();
const route = useRoute();
const quizApi = new QuizApi();
const quizId = ref(route.params.quizId);
const questionForms = ref([
  {
    question_text: "",
    options: [{ text: "" }, { text: "" }, { text: "" }, { text: "" }],
    correct_answer: "",
  },
]);

const allQuestionsValid = computed(() => {
  return questionForms.value.every((questionForm) => {
    const hasText = questionForm.question_text.trim() !== "";
    const allOptionsFilled = questionForm.options.every(
      (option) => option.text.trim() !== ""
    );
    const hasCorrectAnswer =
      questionForm.correct_answer !== null &&
      questionForm.correct_answer !== "";
    return hasText && allOptionsFilled && hasCorrectAnswer;
  });
});

const addQuestionForm = () => {
  questionForms.value.push({
    question_text: "",
    options: [{ text: "" }, { text: "" }, { text: "" }, { text: "" }],
    correct_answer: "",
  });
};

const removeQuestionForm = (index) => {
  questionForms.value.splice(index, 1);
};

const updateQuestion = (index, questionData) => {
  questionForms.value[index] = questionData;
};

const submitAllQuestions = async () => {
  if (!allQuestionsValid) {
    return;
  }
  try {
    await Promise.all(
      questionForms.value.map((form) => {
        const optionsString = form.options
          .map((option) => option.text)
          .join(",");
        const payload = {
          question_text: form.question_text,
          options: optionsString,
          correct_answer: form.correct_answer.toString(),
          quiz_id: quizId.value,
        };
        return quizApi.createQuestion(payload);
      })
    );
    quizStore.enqueueToast({
      severity: "success",
      summary: "Quiz Created",
      detail: "The quiz and all questions were successfully created.",
      life: 3000, // Duration in milliseconds
    });
    router.push("/");
  } catch (error) {
    quizStore.enqueueToast({
      severity: "error",
      summary: "Error",
      detail: "There was a problem saving the questions",
      life: 3000, // Duration in milliseconds
    });
    router.push("/");
    console.error("Error submitting questions:", error);
  }
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
}
</style>
