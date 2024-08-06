<template>
    <div class="ml-8">
        <div class="flex items-center ">
            <button @click="$router.go(-1)" class="ml-10 mt-5">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                </svg>
            </button>
            <h1 class="text-2xl ml-10 mt-5"> {{ teacherStore.groupName }} </h1>
        </div>

        <div>
            <div class="flex items-center hover:cursor-pointer hover:text-blue-500" @click="toggleStudents">
                <DownOutlined v-if="showStudents" class="ml-4 mt-4" />
                <RightOutlined v-else class="ml-4 mt-4" />
                <h1 class="text-xl ml-8 mt-6">Danh sách sinh viên</h1>
            </div>
            <div class="student" v-for="student in students" :key="student.id" v-show="showStudents">
                <Card :student="student" />
            </div>

        </div>
        <div>
            <div class="flex items-center hover:cursor-pointer hover:text-blue-500">
                <DownOutlined v-if="showTests" @click="toggleTests" class="ml-4 mt-4" />
                <RightOutlined v-else @click="toggleTests" class="ml-4 mt-4" />
                <h1 class="text-xl ml-8 mt-6" @click="toggleTests">Bài kiểm tra</h1>

            </div>
            <div class="flex flex-wrap justify-between" v-show="showTests">
                <TestCard class="m-2 max-w-xs" :history="history" :test="test" v-for="test in tests" :key="test.id"
                    @click="getGroupTestId(test.id, test.duration, test.n_page,test.allow_move)" />
            </div>

        </div>


        <div>
            <div class="flex items-center hover:cursor-pointer hover:text-blue-500" @click="toggleHistory">
                <DownOutlined v-if="showHistory" class="ml-4 mt-4" />
                <RightOutlined v-else class="ml-4 mt-4" />
                <h1 class="text-xl ml-8 mt-6">Lịch sử làm bài</h1>

            </div>
            <div class="flex items-center mx-16 mb-5" v-show="showHistory">
                <table class="table-auto w-full m-2 bg-white shadow-md rounded-md">
                    <thead>
                        <tr>
                            <th class="px-4 py-2 text-center">Bài kiểm tra</th>
                            <th class="px-4 py-2 text-center">Ngày thi</th>
                            <th class="px-4 py-2 text-center">Điểm</th>
                            <th class="px-4 py-2 text-center">Số lần vi phạm</th>

                        </tr>
                    </thead>
                    <tbody class="items-center">
                        <tr v-for="record in history" :key="record.id">
                            <td class="border px-4 py-2 text-center">{{ record.group_test.name }}</td>
                            <td class="border px-4 py-2 text-center">{{ formatDate(record.start) }}</td>
                            <td class="border px-4 py-2 text-center">{{ record.score*10}}</td>
                            <td class="border px-4 py-2 text-center">{{ record.violate}}</td>

                        </tr>
                    </tbody>
                </table>
            </div>

        </div>
    </div>

</template>

<script>
import { format } from 'date-fns';
import { useTeacherStore } from '../../../stores/modules/teacher'
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import Card from '../../../components/profile/Card.vue';
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";
import TestCard from '../../../components/questionBank/TestCard.vue';
import { useStudentStore } from '../../../stores/modules/student';

export default {
    components: { Card, DownOutlined, RightOutlined, TestCard },
    setup() {
        const teacherStore = useTeacherStore();
        const studentStore = useStudentStore();
        const students = ref([]);
        const route = useRoute();
        const groupId = route.params.id;
        const showStudents = ref(false);
        const showRequests = ref(true);
        const showTests = ref(true);
        const tests = ref([]);
        const showHistory = ref(true);
        const history = ref([]);
        const formatDate = (date) => {
            return format(new Date(date), 'dd/MM/yyyy');
        }

        const toggleHistory = () => {
            showHistory.value = !showHistory.value;
        }


        const getGroupTestId = (group_test_id, duration, n_page, allow_move) => {
            studentStore.group_test_id = group_test_id;
            localStorage.setItem("duration", duration);
            localStorage.setItem("group_test_id", group_test_id);
            localStorage.setItem("n_page", n_page);
            localStorage.setItem("allow_move", allow_move);

        }
        const toggleTests = () => {
            showTests.value = !showTests.value;
        }
        const toggleRequests = () => {
            showRequests.value = !showRequests.value;
        }
        const toggleStudents = () => {
            showStudents.value = !showStudents.value;
        }

        onMounted(async () => {
            students.value = await studentStore.getStudentsInGroup(groupId);
            tests.value = await studentStore.getGroupTests(groupId);
            history.value = await studentStore.getHistory(groupId)
        });

        return {
            teacherStore,
            students,
            groupId,
            showStudents,
            showRequests,
            showTests,
            tests,
            showHistory,
            history,
            formatDate,
            toggleHistory,
            getGroupTestId,
            toggleTests,
            toggleRequests,
            toggleStudents
        };
    }
}
</script>

<style>

</style>