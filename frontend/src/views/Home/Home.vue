<template>
  <div>
    <Toast
      :pt="{
        container: { class: 'bg-white' },
      }"
    ></Toast>

    <Dashboard v-if="!quizStarted && !quizFinished"></Dashboard>
    <SelectDifficulty v-if="!quizStarted && !quizFinished" class="mt-6" />
    <SelectCategories v-if="!quizStarted && !quizFinished" class="mt-6" />
    <div
      v-if="
        quizStore.quizStatus !== 'STARTED' &&
        quizStore.quizStatus !== 'FINISHED' &&
        quizStore.selectedCategory
      "
      class="mt-6"
    >
      <SelectQuiz />
    </div>
    <div class="text-center mt-6">
      <Button
        @click="startQuiz"
        raised
        text
        label="Start!"
        :disabled="!quizStore.selectedQuiz"
      ></Button>
    </div>
    <div class="text-center mt-6">
      <Button @click="createQuiz" raised text label="Create Quiz."></Button>
    </div>
    <div class="text-center mt-6">
      <Button
        @click="createQuestion"
        raised
        text
        label="Create Question."
      ></Button>
    </div>
    <div class="text-center mt-6">
      <GenerateQuizzes></GenerateQuizzes>
    </div>
    <Quiz v-if="quizStarted || quizFinished" class="mt-6" />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import SelectCategories from "@/components/SelectCategories.vue";
import SelectDifficulty from "@/components/SelectDifficulty.vue";
import SelectQuiz from "@/components/SelectQuiz.vue";
import Quiz from "@/components/Quiz.vue";
import QuizApi from "@/api/quiz";
import { useQuiz } from "@/store/modules/quiz";
import { useRouter } from "vue-router";
import GenerateQuizzes from "../../components/GenerateQuizzes.vue";
import Dashboard from "../../components/Dashboard.vue";
import { useToast } from "primevue/usetoast";

const quizApi = new QuizApi();
const quizStore = useQuiz();
const router = useRouter();
const toast = useToast();

// Using refs to make template cleaner and more reactive
const quizStarted = ref(quizStore.quizStatus === "STARTED");
const quizFinished = ref(quizStore.quizStatus === "FINISHED");

const startQuiz = () => {
  quizStore.setQuizStatus("STARTED");
  router.push({ name: "Quiz", params: { id: quizStore.selectedQuiz.id } });
};

const createQuiz = () => {
  router.push("/createquiz");
};

const createQuestion = () => {
  router.push("/createquestion");
};

const processToasts = (toasts) => {
  toasts.forEach((toastMessage) => {
    toast.add({
      ...toastMessage,
      onClose: () => {
        quizStore.removeToastById(toastMessage.id);
      },
    });
    setTimeout(() => {
      quizStore.removeToastById(toastMessage.id);
    }, toastMessage.life || 3000);
  });
};

watch(
  () => quizStore.toastQueue,
  (newQueue, oldQueue) => {
    const newToasts = [...newQueue].filter(
      (nt) => ![...oldQueue].some((ot) => ot.id === nt.id)
    );
    processToasts(newToasts);
  },
  { deep: true }
);

onMounted(async () => {
  try {
    if (quizStore.toastQueue.length) {
      processToasts([...quizStore.toastQueue]);
    }
    const quizzesResponse = await quizApi.getAllQuizzes();
    const usersResponse = await quizApi.getAllUsers();
    const categoriesResponse = await quizApi.getAllCategories();
    const popularQuiz = await quizApi.getMostPopularQuiz();
    const popularCategory = await quizApi.getMostPopularCategory();
    const bestUser = await quizApi.getTopPerformer();
    const worstUser = await quizApi.getLeastCorrectResultsUser();

    quizStore.setTopPerformer(bestUser.data.value);
    quizStore.setWorstPerformer(worstUser.data.value);
    quizStore.setPopularQuiz(popularQuiz.data.value);
    quizStore.setPopularCategory(popularCategory.data.value);
    quizStore.setCategories(categoriesResponse.data.value);
    quizStore.setSelectedUser(usersResponse.data.value[0]);
   
    if (quizzesResponse.data && usersResponse.data) {
      const quizzes = quizzesResponse.data.value;
      const uniqueCategories = quizzes
        .map((quiz) => quiz.category)
        .reduce((acc, current) => {
          const x = acc.find((item) => item.id === current.id);
          if (!x) {
            return acc.concat([current]);
          } else {
            return acc;
          }
        }, []);
      quizStore.setQuizzes(quizzes);
      quizStore.setCategories(uniqueCategories);
      quizStore.setUsers(usersResponse.data);
    } else {
      console.error("API response is missing data.");
    }
  } catch (error) {
    console.error("An error occurred while fetching data:", error);
  }
});
</script>
