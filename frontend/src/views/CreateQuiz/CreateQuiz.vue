<template>
    <div class="container mx-auto p-4 text-white">
        <h1 class="text-3xl font-bold mb-6">Create a New Quiz</h1>
        <form @submit.prevent="createNewQuiz">
            <!-- Title Field -->
            <div class="mb-6">
                <label for="title" class="block text-base font-medium mb-2">Title:</label>
                <InputText id="title" v-model="quizForm.title" class="w-full" />
                <small v-if="validationErrors.title" class="text-red-500 block mt-1">{{ validationErrors.title }}</small>
            </div>

            <!-- Description Field -->
            <div class="mb-6">
                <label for="description" class="block text-base font-medium mb-2">Description:</label>
                <Textarea id="description" v-model="quizForm.description" rows="5" autoResize class="w-full" />
                <small v-if="validationErrors.description" class="text-red-500 block mt-1">{{ validationErrors.description
                }}</small>
            </div>

            <!-- Category Field -->
            <div class="mb-6">
                <label for="category" class="block text-base font-medium mb-2">Category:</label>
                <Dropdown id="category" v-model="quizForm.category_id" :options="categories" optionLabel="name"
                    optionValue="id" placeholder="Select a Category" />
                <small v-if="validationErrors.category_id" class="text-red-500 block mt-1">{{ validationErrors.category_id
                }}</small>
            </div>

            <!-- Difficulty Field -->
            <div class="mb-6">
                <label for="difficulty" class="block text-base font-medium mb-2">Difficulty:</label>
                <Dropdown id="difficulty" v-model="quizForm.difficulty" :options="difficulties"
                    placeholder="Select Difficulty" />
                <small v-if="validationErrors.difficulty" class="text-red-500 block mt-1">{{ validationErrors.difficulty
                }}</small>
            </div>

            <!-- Owner Field -->
            <div class="mb-6">
                <label for="owner" class="block text-base font-medium mb-2">Owner:</label>
                <Dropdown id="owner" v-model="quizForm.owner_id" :options="simplifiedUsers" optionLabel="name"
                    optionValue="id" placeholder="Select Owner" />
                <small v-if="validationErrors.owner_id" class="text-red-500 block mt-1">{{ validationErrors.owner_id
                }}</small>
            </div>

            <!-- Submit Button -->
            <div class="flex justify-end mt-8">
                <Button label="Next Step" type="submit" class="p-button-rounded p-button-success p-button-lg" />
            </div>
        </form>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import QuizApi from '@/api/quiz';
import { useRouter } from 'vue-router';

const router = useRouter();
const quizApi = new QuizApi();
const validationErrors = ref({});
const categories = ref([]);
const difficulties = ref(['Easy', 'Medium', 'Hard']);
const simplifiedUsers = ref([]);

const quizForm = ref({
    title: '',
    description: '',
    category_id: null,
    difficulty: 'Easy',
    owner_id: null
});

const validateForm = () => {
    validationErrors.value = {};
    let isValid = true;

    if (!quizForm.value.title) {
        validationErrors.value.title = 'Title is required.';
        isValid = false;
    }
    if (!quizForm.value.description) {
        validationErrors.value.description = 'Description is required.';
        isValid = false;
    }
    if (!quizForm.value.category_id) {
        validationErrors.value.category_id = 'Category is required.';
        isValid = false;
    }
    if (!quizForm.value.difficulty) {
        validationErrors.value.difficulty = 'Difficulty is required.';
        isValid = false;
    }
    if (!quizForm.value.owner_id) {
        validationErrors.value.owner_id = 'Owner is required.';
        isValid = false;
    }

    return isValid;
};

onMounted(async () => {
    try {
        const categoriesResponse = await quizApi.getAllCategories();
        if (categoriesResponse.data) {
            categories.value = categoriesResponse.data.value;
        }

        const usersResponse = await quizApi.getAllUsers();
        if (usersResponse.data) {
            simplifiedUsers.value = usersResponse.data.value.map(user => ({
                id: user.id,
                name: user.username 
            }));
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});

const createNewQuiz = async () => {
    if (!validateForm()) {
        return;
    }
    const payload = {
        title: quizForm.value.title,
        description: quizForm.value.description,
        category_id: quizForm.value.category_id,
        difficulty: quizForm.value.difficulty,
        owner_id: quizForm.value.owner_id
    };

    try {
        const response = await quizApi.createQuiz(payload); 
        if (response.data) {
            router.push({ name: 'addquestions', params: { quizId: response.data.value.id } });
        }
    } catch (error) {
        console.error('Error creating quiz:', error);
    }
};
</script>
  