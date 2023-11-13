<template>
  <div>
    <Button label="Generate Quiz" @click="generateQuiz" />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import QuizApi from "@/api/quiz";
import { useQuiz } from "@/store/modules/quiz";

const quizApi = new QuizApi();
const quizStore = useQuiz();
const apiUrl =
  "https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=multiple";
const categories = ref(quizStore.categories);

const ensureCategoryExists = async (categoryName) => {
  let category = categories.value.find((c) => c.name === categoryName);
  if (!category) {
    const newCategory = await quizApi.createCategory({ name: categoryName });
    categories.value.push(newCategory.data);
    category = newCategory.data.value;
  }
  return category.id;
};

const createQuiz = async (categoryName, difficulty) => {
  const category_id = await ensureCategoryExists(categoryName);

  const newQuiz = {
    title: `${Math.random()} Quiz`,
    description: `A quiz about ${categoryName}`,
    category_id,
    difficulty,
    owner_id: quizStore.selectedUser.id,
  };

  const createdQuiz = await quizApi.createQuiz(newQuiz);
  return createdQuiz.data.value.id;
};

const shuffleArray = (array) => {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
};

const createQuestionsForQuiz = async (quizId, questions) => {
  for (const question of questions) {
    // Combine and shuffle the options
    const options = shuffleArray([
      question.correct_answer,
      ...question.incorrect_answers,
    ]);
    // Find the index of the correct answer in the shuffled array
    const correctAnswerIndex = options.indexOf(question.correct_answer) + 1; // +1 because index is 0-based and we need 1-based

    const newQuestion = {
      question_text: question.question,
      options: options.join(","),
      correct_answer: correctAnswerIndex.toString(),
      quiz_id: quizId,
    };

    await quizApi.createQuestion(newQuestion);
  }
};

// Generate a new quiz using the OTDB API
const generateQuiz = async () => {
  try {
    const otbdResponse = await axios.get(apiUrl);
    if (otbdResponse.data.response_code !== 0) {
      throw new Error("Failed to retrieve quizzes from Open Trivia Database");
    }
    const quizzes = otbdResponse.data.results;
    const quizId = await createQuiz(quizzes[0].category, "medium");

    for (const quizData of quizzes) {
      await createQuestionsForQuiz(quizId, [quizData]);
      console.log(`Quiz and questions created for quizId: ${quizId}`);
    }
    quizStore.enqueueToast({
      severity: "success",
      summary: "Quiz Created",
      detail: "The quiz and all questions were successfully created.",
      life: 3000, // Duration in milliseconds
    });
  } catch (error) {
    console.error("There was an error generating the quiz:", error);
    quizStore.enqueueToast({
      severity: "error",
      summary: "Error",
      detail: "There was a problem generating the quiz.",
      life: 3000, // Duration in milliseconds
    });
  }
};
</script>
