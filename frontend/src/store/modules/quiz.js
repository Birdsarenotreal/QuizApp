/* eslint-disable no-console */
import { defineStore } from "pinia";
import { nanoid } from "nanoid";

export const useQuiz = defineStore("quiz", {
  state: () => {
    return {
      categories: [],
      selectedCategory: null,
      selectedQuiz: null,
      selectedUser: null,
      quizStatus: null,
      selectedDifficulty: null,
      quizzes: [],
      users: [],
      isQuizStarted: false,
      elapsedTime: 0,
      topPerformer: null,
      worstPerformer: null,
      popularQuiz: null,
      popularCategory: null,
      toastQueue: [],
    };
  },
  getters: {},
  actions: {
    setSelectedQuiz(quiz) {
      this.selectedQuiz = quiz;
    },
    setQuizzes(quizzes) {
      this.quizzes = quizzes;
    },
    setCategories(categories) {
      this.categories = categories;
    },
    setCategory(category) {
      this.selectedCategory = category;
    },
    setDifficulty(difficulty) {
      this.selectedDifficulty = difficulty;
    },
    setQuizStatus(status) {
      this.quizStatus = status;
    },
    setUsers(users) {
      this.users = users;
    },
    resetDifficulty() {
      this.selectedDifficulty = null;
    },
    resetCategory() {
      this.selectedCategory = null;
    },
    setTopPerformer(topPerformer) {
      this.topPerformer = topPerformer;
    },
    setWorstPerformer(worstPerformer) {
      this.worstPerformer = worstPerformer;
    },
    setPopularQuiz(popularQuiz) {
      this.popularQuiz = popularQuiz;
    },
    setPopularCategory(popularCategory) {
      this.popularCategory = popularCategory;
    },
    enqueueToast(toast) {
      this.toastQueue = [...this.toastQueue, { ...toast, id: nanoid() }];
    },
    dequeueToast() {
      this.toastQueue.shift();
    },
    removeToastById(toastId) {
      this.toastQueue = this.toastQueue.filter((toast) => toast.id !== toastId);
    },
    setSelectedUser(user){
      this.selectedUser = user;
    }
  },
});
