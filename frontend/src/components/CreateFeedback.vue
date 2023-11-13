<template>
  <div class="flex flex-column">
    <Textarea
      v-model="feedbackText"
      placeholder="Your feedback..."
      rows="5"
      class="feedback-textarea"
    />
    <Button
      label="Submit Feedback"
      @click="submitFeedback"
      :disabled="!feedbackText.trim()"
      class="feedback-submit-button max-width-lg"
    />
  </div>
</template>

<script setup>
import { ref } from "vue";
import QuizApi from "@/api/quiz";
import { useQuiz } from "@/store/modules/quiz";
import { useRouter } from "vue-router";

const quizApi = new QuizApi();
const quizStore = useQuiz();
const feedbackText = ref("");
const router = useRouter();

const submitFeedback = async () => {
  const user = quizStore.selectedUser.id;
  if (!user) {
    console.error("User not found in store");
    return;
  }

  try {
    const payload = {
      feedback_text: feedbackText.value,
      user_id: user,
    };
    await quizApi.createFeedback(payload);
    quizStore.setQuizStatus("NOT_STARTED");
    quizStore.enqueueToast({
      severity: "success",
      summary: "Quiz feedback created!",
      detail: "The quiz feedback was submitted.",
      life: 3000,
    });
    router.push("/");
  } catch (error) {
    quizStore.enqueueToast({
      severity: "error",
      summary: "Error",
      detail: "There was a problem submitting the feedback.",
      life: 3000, 
    });
    router.push("/");
    console.error("Error submitting feedback:", error);
  }
};
</script>

<style scoped>
.feedback-textarea {
  margin: 20px 0;
}

.feedback-submit-button {
  max-width: 50%;
  margin: 0 auto 20px auto;
}
</style>
