<template>
  <div class="popular-category-content">
    <h2>{{ popularCategory.name }}</h2>
    <Button label="Select this Category" @click="selectThisCategory" />
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useQuiz } from "@/store/modules/quiz";
import { defineEmits } from "vue";

const quizStore = useQuiz();
const popularCategory = ref(quizStore.popularCategory);
const emit = defineEmits(["update:selectCategory"]);

const clickCategoryButton = (categoryName) => {
  const categoriesContainer = document.querySelector(".categories-identifier");
  if (!categoriesContainer) {
    console.error("Categories container not found");
    return;
  }

  const categoryButtons = Array.from(categoriesContainer.children);
  const categoryButton = categoryButtons.find((button) =>
    button.textContent.includes(categoryName)
  );
  
  if (categoryButton && (popularCategory.value.name !== quizStore.selectedCategory) ) {
    categoryButton.click();
  } else {
    console.warn(`Button for category "${categoryName}" not found.`);
  }
};

const selectThisCategory = () => {
  clickCategoryButton(popularCategory.value.name);
  emit("update:selectCategory", popularCategory.value.name);
  emit("close");
};

watch(
  () => quizStore.selectedCategory,
  (newCategory) => {
    clickCategoryButton(newCategory);
  }
);
</script>

<style scoped>
.popular-category-content {
  text-align: center;
  padding: 1em;
}
</style>
