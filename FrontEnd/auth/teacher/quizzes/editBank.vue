<template>
    <div class="flex items-center">
        <button @click="$router.go(-1) " class="ml-10 mt-5">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
        </button>
        <h1 class="text-2xl ml-10 mt-5">Bộ câu hỏi: {{ questionName }} </h1>
    </div>
    <add-question class="flex justify-end mx-8 " />

    <div class="editor relative h-1/2 w-3/4 items-center justify-center left-28">
        <div v-for="(question, index) in questions" :key="index" class=" mb-10 rounded-lg m-4 ml-8 shadow-md">
            <h1 class="text-2xl p-3 ml-4">Câu {{ index + 1 }}</h1>
            <p class="ml-4 font-bold">
                Câu hỏi: </p>
            <p class="ml-4 p-4">
                {{ question.content }}
            </p>
            <div v-if="question.attachment">
                <div v-for="(file, index) in question.attachment" :key="index">
                    <img v-if="file.endsWith('.jpg') || file.endsWith('.png')" :src="imgUrl+'static/'+ file"
                        class="p-10 w-1/2" />
                    <audio class="ml-4" v-else-if="file.endsWith('.mp3')" controls :src="imgUrl+'static/'+ file">
                        Your browser does not support the audio element.
                    </audio>
                </div>
            </div>
            <p class="ml-4 font-bold">
                Đáp án: </p>
            <answer :answers="question.answer" class="p-4" />
            <p class="ml-4 mb-4 font-bold">
                độ khó: {{ question.difficulty }}</p>

            <edit-question :question="question" />
        </div>
    </div>
</template>

<script>
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import QuillEditor from '../../../components/quill/QuillEditor.vue';
import { useTeacherStore } from '../../../stores/modules/teacher.js';
import AddQuestion from '../../../components/addquestion/Addquestion.vue';

import Answer from '../../../components/answer/Answer.vue';
import EditQuestion from '../../../components/addquestion/EditQuestion.vue';

export default {
    components: {
        QuillEditor,
        Answer,
        AddQuestion,
        EditQuestion,
    },
    setup() {
        const teacherStore = useTeacherStore();
        const questions = ref([]);
        const showAddQuestion = ref(false);
        const route = useRouter();
        const questionName = ref('');
        const imgUrl = import.meta.env.VITE_APP_API;
        const addQuestion = (newQuestion) => {
            questions.value.push(newQuestion);
            showAddQuestion.value = false;
        };

        onMounted(async () => {
            questionName.value = await teacherStore.questionName;

            const id = route.currentRoute.value.params.id;
            teacherStore.bankId = id;

            const rawQuestions = await teacherStore.getQuestions(id);
            questions.value = rawQuestions.map(question => ({
                ...question,
                answer: {
                    text: question.answer.text,
                    correct: question.answer.correct,
                },
                attachment: question.attachment ? question.attachment.map(img => img.replace(/\\\\/g, '/')) : [],
            }));
        });
        watch(() => teacherStore.questions, (newQuestion) => {
            questions.value = newQuestion;
        });

        return {
            questions,
            questionName,
            showAddQuestion,
            imgUrl,
            addQuestion,
        };
    },
};
</script>