<template>
    <div>
        <a-button type="primary" @click="showModal">Thêm câu hỏi</a-button>
        <a-modal v-model:open="open" title="Thêm câu hỏi" @ok="handleOk" :width="800">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2 font-bold">Câu hỏi: </label>
                <!-- <input v-model="content"
                    class="input rounded-md px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                    placeholder="Nhập câu hỏi..." required="" type="text" />
                
                -->
                <Editor @add-question="handleContentUpdate" :response="response" />

                <label class="block mb-2 mt-4 font-bold">Đính kèm: </label>
                <label for="file-upload"
                    class="input rounded-md px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md">
                    Chọn file...
                </label>
                <input id="file-upload" type="file" @change="handleFileChange" class="file-input hidden" multiple />

                <div class="mt-4">
                    <h2 class="font-bold">Files đã chọn:</h2>
                    <ul>
                        <li v-for="(f, index) in file" :key="index">{{ f.name }}</li>
                    </ul>
                </div>
                <label class="block mb-2 mt-4 font-bold">Độ khó: </label>
                <select v-model="difficulty"
                    class="input rounded-md px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>

                </select>
                <label class="block mb-2 mt-4 font-bold">Đáp án: </label>
                <div v-for="(answer, index) in answers" :key="index">
                    <input type="checkbox" v-model="answers[index].isCorrect" />
                    <input v-model="answers[index].text"
                        class="input rounded-md m-2 px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                        placeholder="Nhập đáp án..." required="" type="text" />

                    <a-button type="primary" class="bg-red-500" @click="removeAnswer(index)">Xóa</a-button>

                </div>
                <a-button type="primary" @click="addAnswer" class="mt-4">Thêm đáp án</a-button>
            </div>
        </a-modal>
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
import { useRoute } from 'vue-router';
import Editor from '../quill/Editor.vue';

export default {
    components: {
        Editor

    },
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const route = useRoute();
        const content = ref(null);
        const difficulty = ref(1);
        const answers = ref([{ text: '', isCorrect: false }]);
        const collection = computed(() => ({ question: question.value, answers: answers.value }));
        const file = ref([]);
        const resetForm = () => {
            content.value = null;
            difficulty.value = 1;
            answers.value = [{ text: '', isCorrect: false }];
            file.value = null;
        };



        const handleFileChange = (e) => {
            console.log('handleFileChange called', e.target.files);
            // file.value = e.target.files[0];
            file.value = Array.from(e.target.files);
        }

        const handleContentUpdate = (textFromEditor) => {
            content.value = textFromEditor.replace(/<\/?p>/g, '');

        }


        const showModal = () => {
            open.value = true;
        };
        const id = route.params.id;

        const handleOk = async () => {

            loading.value = true;
            const answerTexts = answers.value.map(answer => answer.text);
            const correctAnswers = answers.value
                .map((answer, index) => answer.isCorrect ? index : -1)
                .filter(index => index !== -1);

            const question = {
                content: content.value,
                answer: {
                    text: answerTexts,
                    correct: correctAnswers
                },
                difficulty: parseInt(difficulty.value)
            };

            const questions = [question];


            const response = await teacherStore.addQuestion(id, questions);

            const formData = new FormData();
            file.value.forEach((f, index) => {
                formData.append('attachment', f);
            });
            const res = response.toString();
            //console.log(res)
            console.log(formData.value);
            await teacherStore.uploadFile(formData, res);


            //console.log(response.toString());
            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 1000);
            resetForm();
        };



        const handleCancel = () => {
            open.value = false;
            resetForm();
        };

        const addAnswer = () => {
            answers.value.push({ text: '', isCorrect: false });
        };
        const removeAnswer = (index) => {
            answers.value.splice(index, 1);
        }

        return {
            open,
            loading,

            answers,
            content,
            difficulty,
            file,
            handleContentUpdate,
            handleFileChange,
            resetForm,
            addAnswer,
            removeAnswer,
            collection,
            showModal,
            handleOk,
            handleCancel,
            addAnswer
        };
    }
}
</script>
<style scoped>

</style>