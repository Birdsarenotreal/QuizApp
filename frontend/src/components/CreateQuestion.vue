<template>
    <div class="container mx-auto p-4">
      <!-- Question Text Field -->
      <div class="mb-6">
        <label for="questionText" class="block text-base font-medium mb-2">Question Text:</label>
        <InputText id="questionText" v-model="question.question_text" class="w-full" />
      </div>
  
      <!-- Options Fields -->
      <div v-for="(option, index) in question.options" :key="index" class="mb-6">
        <label :for="'option' + index" class="block text-base font-medium mb-2">Option {{ index + 1 }}:</label>
        <InputText :id="'option' + index" v-model="option.text" class="w-full" />
      </div>
  
      <!-- Correct Answer Field -->
      <div class="mb-6">
        <label class="block text-base font-medium mb-2">Correct Answer:</label>
        <div v-for="(option, index) in question.options" :key="'correct' + index" class="flex items-center mb-2">
          <RadioButton v-model="question.correct_answer" :value="(index + 1).toString()" />
          <label :for="option.text" class="ml-2">{{ option.text }}</label>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps, defineEmits } from "vue";
  
  const props = defineProps({
    question: Object,
  });
  
  const emit = defineEmits(['update-question']);
  const question = ref(props.question);
  </script>
  
<style scoped>
.container {
    max-width: 600px;
    margin: auto;
}
</style>