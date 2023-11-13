<template>
  <h2 class="text-center">{{ question.question_text }}</h2>
  <div
    v-for="(choice, index) in question.options.split(',')"
    :key="index"
    class="flex justify-content-center mt-3"
  >
    <RadioButton
      v-model="selectedChoice"
      :inputId="'choice-' + index"
      name="choice"
      :value="(index + 1)"
      @change="onChoiceChange(index + 1)"
    />
    <label :for="'choice-' + index" class="ml-2 text-xl text-center">{{ choice }}</label>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  question: {
    type: Object,
    required: true,
  },
  onAnswer: {
    type: Function,
    required: true,
  },
});

const selectedChoice = ref(null);

// Emit the selected choice when it changes
const onChoiceChange = (choice) => {
  props.onAnswer(choice, props.question.id);
};

// If you want to watch for the selected choice change inside the component
watch(selectedChoice, (newValue) => {
  if (newValue !== null) {
    props.onAnswer(newValue, props.question.id);
  }
});
</script>
