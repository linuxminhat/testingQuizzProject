<template>
    <div>
        <a-button type="primary" @click="showModal">Tạo bài kiểm tra</a-button>
        <a-modal v-model:open="open" title="Tạo bải kiểm tra" @ok="handleOk" width="1000px">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>

            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Tên bài kiểm tra: </label>
                <input type="text" v-model="name"
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    placeholder="Nhập tên bài kiểm tra" />
            </div>


            <div v-for="(struct, idx) in structure" :key="idx" class="p-4">
                <div class="flex items-center p-4">
                    <label class="w-1/5 mb-2">Bộ sưu tập: </label>
                    <select name="" id=""
                        class="w-2/3 px-2 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                        v-model="struct.selected_collection">
                        <option v-for="collection in collections" :key="collection.id" :value="collection.id">
                            {{ collection.name }}
                        </option>
                    </select>

                    <label class="w-1/3 block mb-2 ml-2">Ngân hàng câu hỏi: </label>
                    <select name="" id=""
                        class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                        v-model="struct.question_bank_id">
                        <option v-for="questionBank in struct.questionBanks" :key="questionBank.id"
                            :value="questionBank.id">
                            {{ questionBank.name }}
                        </option>
                    </select>
                    <button @click="removeStructureRow(idx)" class="bg-red-500 text-white px-4 py-2 rounded mt-0 ml-4">
                        Xóa
                    </button>

                </div>

                <div v-for="(num, numindex) in struct.number_of_question" :key="numindex" class="p-4">
                    <div class="flex justify-between mb-2 items-center">
                        <div class="w-1/3  flex items-center">
                            <label class="w-1/2 mb-2">Độ khó: </label>
                            <select name="" id=""
                                class="w-1/2 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                                v-model.number="num.difficulty">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                            </select>
                        </div>
                        <div class="w-2/3 pl-2 flex items-center">
                            <label class="w-2/3 mb-2">Số lượng câu hỏi: </label>
                            <input type="number" v-model="num.number_of_question" min='1'
                                class="w-1/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                                placeholder="Nhập số lượng câu hỏi" />
                        </div>
                        <button @click="removeSNumberQuestion(numindex)"
                            class="w-1/5 bg-red-500 text-white px-4 py-2 rounded ml-4">
                            Xóa
                        </button>
                    </div>
                </div>

                <button @click="addSNumberQuestion(struct)"
                    class="bg-blue-500 text-white px-4 py-2 rounded mt-4 justify-end items-end right-10">
                    Thêm Câu hỏi
                </button>

            </div>
            <button @click="addStructureRow" class="bg-blue-500 text-white px-4 py-2 rounded mt-4">
                Thêm ngân hàng câu hỏi
            </button>



        </a-modal>
    </div>
</template>

<script>
import { ref, watch, computed } from "vue";
import { useTeacherStore } from "../../stores/modules/teacher";
import { watchEffect } from "vue";
import { useRoute } from 'vue-router';


export default {

    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const collections = ref('');
        const collection_id = ref('')
        const selectedCollection = ref(null);
        const name = ref('');
        const questionBanks = ref([])
        const route = useRoute();
        const structure = ref([

            {
                selected_collection: null,
                questionBanks: [],
                question_bank_id: null,
                number_of_question: [
                    {
                        difficulty: null,
                        number_of_question: null
                    }
                ]
            }
        ]);

        const test = computed(() => ({
            collection_id: collection_id.value,
            name: name.value,
            structure: structure.value.map(item => {
                const { selected_collection, questionBanks, ...rest } = item;
                return rest;
            })
        }));




        watchEffect(() => {
            structure.value.forEach(async (struct, idx) => {
                if (struct.selected_collection) {
                    struct.questionBanks = await teacherStore.getQuestionBank(struct.selected_collection);


                } else {
                    struct.questionBanks = [];
                }
            });
        });



        watch(name, (newName) => {
            test.value.name = newName;
        });


        const addQuestionBankRow = () => {
            questionBankIds.value.push({});
        };
        const removeQuestionBankRow = (index) => {
            questionBankIds.value.splice(index, 1);
        };
        const addStructureRow = () => {
            structure.value.push({
                selected_collection: null,
                question_bank_id: null,
                number_of_question: [
                    {
                        difficulty: null,
                        number_of_question: null
                    }
                ]
            });
        }
        const removeStructureRow = (index) => {
            structure.value.splice(index, 1);
        }

        const addSNumberQuestion = (struct) => {
            struct.number_of_question.push({
                difficulty: null,
                number_of_question: null
            });
        }
        const removeSNumberQuestion = (struct, numindex) => {
            struct.number_of_question.splice(numindex, 1);
        }


        const showModal = async () => {
            open.value = true;
            collections.value = await teacherStore.getCollections();
            collection_id.value = route.params.id;

        };

        const handleOk = async () => {
            loading.value = true;
            console.log(test.value)

            teacherStore.addTest(test.value);
            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            open,
            loading,
            collections,
            selectedCollection,
            test,
            questionBanks,
            structure,
            name,
            collection_id,
            route,

            addStructureRow,
            removeStructureRow,
            addQuestionBankRow,
            removeQuestionBankRow,
            addSNumberQuestion,
            removeSNumberQuestion,
            showModal,
            handleOk,
            handleCancel,
        };
    },
};
</script>
