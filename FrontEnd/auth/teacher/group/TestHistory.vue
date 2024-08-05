<template>
    <div>
        <button @click="$router.go(-1)" class=" relative ml-10 top-10">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
        </button>

        <div class="editor relative h-1/2 w-3/4 items-center justify-center left-28">
            <div v-for="(question, index) in test" :key="index" class=" mb-10 rounded-lg m-4 ml-8 shadow-md">
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
                <student-answer :answers="question.answer" :studentAnswer="question.student_answer" class="p-4" />



            </div>

        </div>
    </div>
</template>

<script>
import { useTeacherStore } from '../../../stores/modules/teacher';
import { ref, onMounted } from 'vue';


import StudentAnswer from '../../../components/answer/StudentAnswer.vue';
export default {

    components: { StudentAnswer },

    setup() {
        const test = ref(null);

        const teacherStore = useTeacherStore();
        const imgUrl = import.meta.env.VITE_APP_API;

        onMounted(async () => {
            test.value = await teacherStore.tmpTest;
            console.log(test.value.student_work)
        })

        return {
            test,
            imgUrl
        };

    }

}
</script>

<style>

</style>