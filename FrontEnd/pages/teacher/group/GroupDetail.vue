<template>
    <div class="ml-8 ">
        <div class="flex items-center mb-5">
            <button @click="$router.go(-1)" class="ml-10 ">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                </svg>
            </button>
            <h1 class="text-2xl ml-5 my-5"> {{ teacherStore.groupName }}</h1>
        </div>
        <div class="mb-4">
            <div class="flex items-center hover:cursor-pointer hover:text-blue-500">
                <DownOutlined v-if="showRequests" @click="toggleRequests" class="ml-4" />
                <RightOutlined v-else @click="toggleRequests" class="ml-4" />
                <h1 class="text-xl ml-8 my-0" @click="toggleRequests">Yêu cầu tham gia</h1>
            </div>
            <div class="student" v-for="request in requests" :key="request.id" v-show="showRequests">
                <request :student="request" />

            </div>

        </div>
        <div class="mb-4">
            <div class="flex items-center relative hover:cursor-pointer hover:text-blue-500">
                <DownOutlined v-if="showStudents" @click="toggleStudents" class="ml-4 hover:cursor-pointer" />
                <RightOutlined v-else @click="toggleStudents" class="ml-4 hover:cursor-pointer" />
                <h1 class="text-xl ml-8 my-0 hover:cursor-pointer" @click="toggleStudents">Danh sách sinh viên</h1>
                <div class="absolute right-10 top-1/2 transform -translate-y-1/2" v-show="showStudents">
                    <add-student />
                </div>
            </div>
            <div class="student" v-for="student in students" :key="student.id" v-show="showStudents">
                <Card :student="student" />
            </div>

        </div>
        <div>
            <div class="flex items-center hover:cursor-pointer hover:text-blue-500">
                <DownOutlined v-if="showTests" @click="toggleTests" class="ml-4" />
                <RightOutlined v-else @click="toggleTests" class="ml-4" />
                <h1 class="text-xl ml-8 my-0" @click="toggleTests">Bài kiểm tra</h1>
                <group-test class="ml-auto" v-show="showTests" />
            </div>
            <div class="flex flex-wrap justify-start hover:cursor-pointer" v-show="showTests">
                <TestCard class="m-2" v-for="groupTest in groupTests" :key="groupTest.id" :test="groupTest" />
            </div>
        </div>
    </div>

</template>

<script>
import { useTeacherStore } from '../../../stores/modules/teacher'
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import Card from '../../../components/profile/Card.vue';
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";
import AddStudent from '../../../components/modal/AddStudent.vue';
import TestCard from '../../../components/questionBank/TestCard.vue';
import AddTest from '../../../components/modal/AddTest.vue';
import Request from '../../../components/profile/Request.vue';
import GroupTest from '../../../components/modal/GroupTest.vue';
import router from '../../../router';

export default {
    components: { Card, DownOutlined, RightOutlined, TestCard, AddStudent, AddTest, Request, GroupTest },


    setup() {
        const teacherStore = useTeacherStore();
        const students = ref([]);
        const route = useRoute();
        const groupId = route.params.id;
        const showStudents = ref(false);
        const showRequests = ref(true);
        const showTests = ref(false);
        const tests = ref([]);
        const requests = ref([]);
        const groupTests = ref([])
        const toggleTests = async () => {

            showTests.value = !showTests.value;
            groupTests.value = await teacherStore.getGroupTests(groupId);

        }
        const toggleRequests = () => {
            showRequests.value = !showRequests.value;
        }
        const toggleStudents = async () => {

            showStudents.value = !showStudents.value;
            students.value = await teacherStore.getStudents(groupId);


        }

        onMounted(async () => {
            //  tests.value = await teacherStore.getTests(groupId);
            requests.value = await teacherStore.getRequests(groupId);
            console.log(groupTests.value)

        });

        return {
            teacherStore,
            students,
            groupId,
            showStudents,
            showRequests,
            showTests,
            tests,
            requests,
            groupTests,

            toggleTests,
            toggleRequests,
            toggleStudents
        };
    }
}
</script>

<style>

</style>