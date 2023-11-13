<template>
  <div class="dashboard">
    <div class="flex justify-content-center flex-wrap">
      <Button
        label="Top Performer"
        @click="showTopPerformer = true"
        class="m-2"
      />
      <Button
        label="Worst Performer"
        @click="showWorstPerformer = true"
        class="m-2"
      />
      <Button
        label="Most Popular Category"
        @click="showPopularCategory = true"
        class="m-2"
      />
      <Button class="m-2" label="Most Popular Quiz" @click="showPopularQuiz = true" />
      <Button
        label="Select Current User"
        @click="showSelectUserModal = true"
        class="m-2"
      />
      <Chip v-if="selectedUser" :label="`Current User: ${selectedUser.username}`" class="m-2" />
    </div>

    <!-- Modals -->
    <Dialog v-model:visible="showTopPerformer">
      <TopPerformerModal />
    </Dialog>

    <Dialog v-model:visible="showWorstPerformer">
      <WorstPerformerModal />
    </Dialog>

    <Dialog v-model:visible="showPopularCategory">
      <PopularCategoryModal
        @update:selectCategory="handleCategorySelection"
        @close="showPopularCategory = false"
      />
    </Dialog>

    <Dialog v-model:visible="showPopularQuiz">
      <PopularQuizModal />
    </Dialog>

    <Dialog v-model:visible="showSelectUserModal">
      <SelectUserModal @selectUser="handleUserSelection" />
    </Dialog>
  </div>
</template>

<script setup>
import { ref, reactive, watch } from "vue";
import TopPerformerModal from "@/components/TopPerformerModal.vue";
import WorstPerformerModal from "@/components/WorstPerformerModal.vue";
import PopularCategoryModal from "@/components/PopularCategoryModal.vue";
import PopularQuizModal from "@/components/PopularQuizModal.vue";
import SelectUserModal from "@/components/SelectUserModal.vue";
import { useQuiz } from "@/store/modules/quiz";

const quizStore = useQuiz();
const showTopPerformer = ref(false);
const showWorstPerformer = ref(false);
const showPopularCategory = ref(false);
const showPopularQuiz = ref(false);
const showSelectUserModal = ref(false);
const selectedUser = ref(null);
const state = reactive({
  selectCategory: null,
});

watch(() => quizStore.selectedUser, (newValue) => {
  selectedUser.value = newValue;
});

const handleCategorySelection = (categoryName) => {
  state.selectCategory = categoryName; 
};

</script>

<style scoped>
.dashboard {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding: 1rem 2rem; /* Adjusted for better spacing */
  background: #1a1a1a; /* Dark background for contrast */
  z-index: 1000; /* Ensure the dashboard is above other content */
}

/* Adjustments for buttons and dialog modals as needed */

@media (max-width: 768px) {
  .dashboard {
    padding: 0.5rem 1rem; /* Reduced padding on smaller screens */
  }}
</style>
