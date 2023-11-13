import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home/Home.vue";
import Quiz from "@/components/Quiz.vue";
import CreateQuiz from "@/views/CreateQuiz/CreateQuiz.vue";
import CreateQuestion from "@/views/CreateQuestion/CreateQuestion.vue";
import AddQuestions from "@/views/CreateQuiz/AddQuestions.vue";
// import QuizFeedback from '@/views/QuizFeedback.vue';
// import QuizResults from '@/views/QuizResults.vue';

// Define your routes
const routes = [
  { path: "/", component: Home },
  {
    path: "/quiz/:id", 
    name: "Quiz",
    component: Quiz,
    props: true, 
  },
  { path: "/createquiz", component: CreateQuiz },
  { path: "/createquestion", component: CreateQuestion },
  {
    path: "/addquestions/:quizId",
    name: "addquestions",
    component: AddQuestions,
  },

  //   { path: '/create-quiz', component: CreateQuiz },
  //   { path: '/take-quiz/:id', component: TakeQuiz },
  //   { path: '/quiz-feedback/:id', component: QuizFeedback },
  //   { path: '/quiz-results/:id', component: QuizResults },
  // ... other routes
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
