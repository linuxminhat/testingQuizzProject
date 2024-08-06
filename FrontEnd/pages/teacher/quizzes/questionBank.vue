<template>
    <div class="flex items-center">
        <button @click="$router.go(-1)" class="ml-10 mt-5">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
        </button>
        <h1 class="text-2xl ml-10 mt-5">Bộ sưu tập: {{ collectionName }}</h1>

    </div>


    <div class="flex justify-end m-4 -mt-4 mr-8">
        <add-question-bank />
    </div>

    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleQuestionBanks">
        <DownOutlined v-if="showQuestionBanks" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4">Ngân hàng câu hỏi</h1>
    </div>

    <div class="flex flex-wrap" v-show="showQuestionBanks">
        <Bank v-for="(item, index) in banks" :key="index" :collection="item" @click="getName(item.name)" />
    </div>


    <div class="flex items-center group cursor-pointer text-blue-500 hover:text-blue-700">
        <DownOutlined v-if="showTests" class="ml-4  transform transition-transform duration-200" @click="toggleTests" />
        <RightOutlined v-else class="ml-4  transform transition-transform duration-200" @click="toggleTests" />
        <h1 class="text-xl p-4 transition-colors duration-200" @click="toggleTests">Đề thi</h1>
        <add-test v-show="showTests" class="ml-auto mr-12 transition-opacity duration-200" />
    </div>

    <div class="flex flex-wrap" v-show="showTests">
        <Test v-for="(item, index) in tests" :key="index" :test="item" />
    </div>


</template>

<script>
import { defineComponent, ref, onMounted, watch } from 'vue';
import { useTeacherStore } from '../../../stores/modules/teacher.js';
import { useRoute } from 'vue-router';
import Bank from '../../../components/questionBank/Bank.vue';
import Addform from '../../../components/modal/Addform.vue';
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";
import AddTest from '../../../components/modal/AddTest.vue';

import AddQuestionBank from '../../../components/modal/AddQuestionBank.vue';
import Test from '../../../components/questionBank/Test.vue';
export default defineComponent({
    components: {
        Bank,
        Addform,
        AddQuestionBank,
        DownOutlined,
        RightOutlined, AddTest,
        Test
    },

    setup() {
        const banks = ref([]);
        const teacherStore = useTeacherStore();
        const route = useRoute();
        const collectionName = ref('');
        const showQuestionBanks = ref(true);
        const tests = ref([]);



        const toggleQuestionBanks = () => {
            showQuestionBanks.value = !showQuestionBanks.value;
        };

        const showTests = ref(true);
        const toggleTests = () => {
            showTests.value = !showTests.value;
        };


        onMounted(async () => {
            const id = route.params.id;

            collectionName.value = await teacherStore.collectionName;
            banks.value = await teacherStore.getQuestionBank(id);
            tests.value = await teacherStore.getTests(id);

        });
        const getName = (name) => {
            teacherStore.questionName = name;
        };
        watch(() => teacherStore.questionBank, (newQuestionBank) => {
            banks.value = newQuestionBank;
        });
        watch(() => teacherStore.testInCollection, (newTests) => {
            tests.value = newTests;
        });

        return {
            banks,
            collectionName,
            showQuestionBanks,
            showTests,
            tests,
            toggleTests,
            toggleQuestionBanks,
            getName,
        };
    }
})
</script>

<style>

</style>