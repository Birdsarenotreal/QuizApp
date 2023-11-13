import { useHttp } from "@/composables/useHttp";

export default class QuizApi {
  // Health endpoint
  async getPublicHealth() {
    return usePublicHttp(`/v1/monitoring/health/`, "GET");
  }

  // Answer endpoints
  async getAllAnswers() {
    return useHttp("/v1/answer/", "GET");
  }

  async createAnswer(data) {
    return useHttp(`/v1/answer/`, "POST", data);
  }

  async getAnswer(id) {
    return useHttp(`/v1/answer/${id}`, "GET");
  }

  async updateAnswer(id, data) {
    return useHttp(`/v1/answer/${id}`, "PUT", data);
  }

  async deleteAnswer(id) {
    return useHttp(`/v1/answer/${id}`, "DELETE");
  }

  // Category endpoints
  async getAllCategories() {
    return useHttp("/v1/category/", "GET");
  }

  async createCategory(data) {
    return useHttp(`/v1/category/`, "POST", data);
  }

  async getCategory(id) {
    return useHttp(`/v1/category/${id}`, "GET");
  }

  async updateCategory(id, data) {
    return useHttp(`/v1/category/${id}`, "PUT", data);
  }

  async deleteCategory(id) {
    return useHttp(`/v1/category/${id}`, "DELETE");
  }

  // Feedback endpoints
  async getAllFeedbacks() {
    return useHttp("/v1/feedback/", "GET");
  }

  async createFeedback(data) {
    return useHttp(`/v1/feedback/`, "POST", data);
  }

  async getFeedback(id) {
    return useHttp(`/v1/feedback/${id}`, "GET");
  }

  async updateFeedback(id, data) {
    return useHttp(`/v1/feedback/${id}`, "PUT", data);
  }

  async deleteFeedback(id) {
    return useHttp(`/v1/feedback/${id}`, "DELETE");
  }

  // Question endpoints
  async getAllQuestions() {
    return useHttp("/v1/question/", "GET");
  }

  async createQuestion(data) {
    return useHttp(`/v1/question/`, "POST", data);
  }

  async getQuestion(id) {
    return useHttp(`/v1/question/${id}`, "GET");
  }

  async updateQuestion(id, data) {
    return useHttp(`/v1/question/${id}`, "PUT", data);
  }

  async deleteQuestion(id) {
    return useHttp(`/v1/question/${id}`, "DELETE");
  }

  // Quiz endpoints
  async getAllQuizzes() {
    return useHttp("/v1/quiz/", "GET");
  }

  async createQuiz(data) {
    return useHttp(`/v1/quiz/`, "POST", data);
  }

  async getQuiz(id) {
    return useHttp(`/v1/quiz/${id}`, "GET");
  }

  async updateQuiz(id, data) {
    return useHttp(`/v1/quiz/${id}`, "PUT", data);
  }

  async deleteQuiz(id) {
    return useHttp(`/v1/quiz/${id}`, "DELETE");
  }

  // Result endpoints
  async getAllResults() {
    return useHttp("/v1/result/", "GET");
  }

  async createResult(data) {
    return useHttp(`/v1/result/`, "POST", data);
  }

  async getResult(id) {
    return useHttp(`/v1/result/${id}`, "GET");
  }

  async updateResult(id, data) {
    return useHttp(`/v1/result/${id}`, "PUT", data);
  }

  async deleteResult(id) {
    return useHttp(`/v1/result/${id}`, "DELETE");
  }

  // Session endpoints
  async getAllSessions() {
    return useHttp("/v1/session/", "GET");
  }

  async createSession(data) {
    return useHttp(`/v1/session/`, "POST", data);
  }

  async getSession(id) {
    return useHttp(`/v1/session/${id}`, "GET");
  }

  async updateSession(id, data) {
    return useHttp(`/v1/session/${id}`, "PUT", data);
  }

  async deleteSession(id) {
    return useHttp(`/v1/session/${id}`, "DELETE");
  }

  // User endpoints
  async getAllUsers() {
    return useHttp("/v1/user/", "GET");
  }

  async createUser(data) {
    return useHttp(`/v1/user/`, "POST", data);
  }

  async getUser(id) {
    return useHttp(`/v1/user/${id}`, "GET");
  }

  async updateUser(id, data) {
    return useHttp(`/v1/user/${id}`, "PUT", data);
  }

  async deleteUser(id) {
    return useHttp(`/v1/user/${id}`, "DELETE");
  }

  async getMostPopularCategory() {
    return useHttp("/v1/category/most-popular-category/", "GET");
  }

  async getMostPopularQuiz() {
    return useHttp("/v1/quiz/most-popular-quiz/", "GET");
  }

  async getTopPerformer() {
    return useHttp("/v1/result/top-performer/", "GET");
  }

  async getLeastCorrectResultsUser() {
    return useHttp("/v1/result/least-correct-results-user/", "GET");
  }
}
