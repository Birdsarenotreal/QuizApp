<template>
  <div>
    <div v-if="quizStore.quizStatus !== 'FINISHED'">
      <h1 class="text-center">Quiz</h1>
      <h2 class="text-center">Time remaining: {{ timerCount }} seconds</h2>
      <ViewQuestion
        v-for="(question, index) in questions"
        :question="question"
        :choices="question.choices"
        :onAnswer="handleAnswer"
      />

      <div class="text-center mt-6">
        <Button
          @click="finishQuiz"
          class="text-2xl"
          raised
          text
          label="Finish!"
        ></Button>
      </div>
    </div>

    <div v-if="quizStore.quizStatus === 'FINISHED'" class="text-center">
      <h2>Quiz Completed!</h2>
      <p>Your Score: {{ score }} / {{ questions.length }}</p>
      <div v-for="(question, index) in questions" :key="index" class="mb-4">
        <Card>
          <template #title>
            {{ index + 1 }}. {{ question.question_text }}
          </template>
          <template #content>
            <div class="flex centered-question-feedback">
              <div class="mr-2">Your answer:</div>
              <Tag
                :severity="
                  question.correct_answer == userAnswers[index].answer.index
                    ? 'success'
                    : 'danger'
                "
                class="mr-2"
              >
                {{
                  question.userAnswer
                    ? question.userAnswer.text
                    : "No answer provided"
                }}
              </Tag>
              <div
                v-if="
                  !(question.correct_answer == userAnswers[index].answer.index)
                "
              >
                <span class="text-muted">Correct answer:</span>
                <Tag severity="info" class="ml-1">
                  {{ question.options.split(",")[question.correct_answer - 1] }}
                </Tag>
              </div>
            </div>
          </template>
        </Card>
      </div>
      <CreateFeedback v-if="quizStore.quizStatus === 'FINISHED'" />
      <Button
        @click="backToQuizSelection"
        class="text-2xl"
        raised
        text
        label="Back to Quiz Selection"
      ></Button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import ViewQuestion from "./ViewQuestion.vue";
import { useQuiz } from "@/store/modules/quiz";
import QuizApi from "@/api/quiz";
import CreateFeedback from "@/components/CreateFeedback.vue";

const quizApi = new QuizApi();
const quizStore = useQuiz();
const route = useRoute();
const router = useRouter();
const quizId = route.params.id;
const questions = ref([]);
const score = ref(0);
const userAnswers = ref([]);
const maxTime = 60;
const isQuizSubmitted = ref(false);
const timerCount = ref(maxTime);

watch(timerCount, (newValue) => {
  if (newValue > 0) {
    setTimeout(() => {
      timerCount.value--;
    }, 1000);
  } else {
    finishQuiz();
  }
}, { immediate: true });

onMounted(async () => {
  if (quizId) {
    try {
      const response = await quizApi.getQuiz(quizId);
      if (response.data) {
        questions.value = response.data.value.questions;
        userAnswers.value = questions.value.map(
          (q) => new Object({ questionId: q.id, answer: "" })
        );
      }
    } catch (error) {
      console.error("Error fetching quiz data:", error);
    }
  }
});

const handleAnswer = (choiceIndex, questionId) => {
  const question = questions.value.find((q) => q.id === questionId);
  const choiceText = question
    ? question.options.split(",")[choiceIndex - 1]
    : "";

  const answerIndex = userAnswers.value.findIndex(
    (ans) => ans.questionId === questionId
  );
  if (answerIndex !== -1) {
    userAnswers.value[answerIndex].answer = {
      index: choiceIndex,
      text: choiceText,
    };
  } else {
    userAnswers.value.push({
      questionId,
      answer: { index: choiceIndex, text: choiceText },
    });
  }
};

const submitResults = async () => {
  const resultData = {
    score: score.value,
    time_taken: '5',
    quiz_id: parseInt(quizId),
    user_id: quizStore.selectedUser.id,
  };

  try {
    await quizApi.createResult(resultData);
    console.log("Results submitted successfully");
  } catch (error) {
    console.error("Error submitting results:", error);
  }
};

const finishQuiz = async () => {
  if (isQuizSubmitted.value) {  //we need this to keep track so we dont call the api to submit the values twice
    return;
  }

  isQuizSubmitted.value = true;
  score.value = 0;
  let hasError = false;

  const answersPromises = userAnswers.value.map(async (userAnswer) => {
    const question = questions.value.find(
      (q) => q.id === userAnswer.questionId
    );
    const userAnswerIndex = userAnswer.answer.index.toString();
    if (question) {
      const isCorrect = userAnswerIndex === question.correct_answer;
      if (isCorrect) {
        score.value++;
      }
      question.answeredCorrectly = isCorrect;
      question.userAnswer = userAnswer.answer;

      const payload = {
        question_id: question.id,
        answer: userAnswerIndex,
        user_id: quizStore.selectedUser.id,
      };

      try {
        await quizApi.createAnswer(payload);
      } catch (error) {
        console.error("Error submitting answer:", error);
      }
    }
  });

  await Promise.all(answersPromises);
  if (!hasError) {
    try {
      await submitResults();
      quizStore.enqueueToast({
        severity: "success",
        summary: "Quiz Submitted",
        detail: "Your quiz results were submitted successfully.",
        life: 3000,
      });
      quizStore.setQuizStatus("FINISHED");
    } catch (error) {
      console.error("Error submitting quiz results:", error);
      quizStore.enqueueToast({
        severity: "error",
        summary: "Submission Error",
        detail: "There was an error submitting your quiz results.",
        life: 3000,
      });
    }
  } else {
    quizStore.enqueueToast({
      severity: "error",
      summary: "Answers Submission Error",
      detail: "There was an error submitting one or more of your answers.",
      life: 3000,
    });
  }
};

const backToQuizSelection = () => {
  quizStore.setQuizStatus("NOT_STARTED");
  router.push("/");
};
</script>

<style scoped>
.centered-question-feedback {
  justify-content: center;
}
</style>
