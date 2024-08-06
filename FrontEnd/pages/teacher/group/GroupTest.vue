<template>
    <div>
        <button @click="$router.go(-1)" class=" relative ml-10 top-10">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
        </button>
        <h1 class="text-3xl flex justify-center items-center mt-10 font-semibold">
            Kết quả thi
        </h1>
        <div class="p-20 items-center justify-center w-full h-screen">
            <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            STT
                        </th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Họ và tên
                        </th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Trạng thái
                        </th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Điểm
                        </th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Số lần vi phạm
                        </th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    <tr v-for="(item, index) in data" :key="item.student" @click="getTestHistory(item.student_work)"
                        class=" cursor-pointer hover:text-blue-500">
                        <td class="px-6 py-4 whitespace-nowrap">{{ index + 1 }}</td>
                        <td class="px-6 py-4 whitespace-nowrap">{{ item.student.name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap" :class="{
              'text-green-500': item.start != null && item.end !=null,
              'text-yellow-500': item.start != null && item.end == null ,
            }">
                            {{
                            item.state !== undefined ? item.state :
                            (item.start === null ? "Chưa tham gia" : (item.end === null) ? "Đang làm" : "Đã hoàn thành")
                            }}
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap">{{ item.score*10 }}</td>
                        <td class="px-6 py-4 whitespace-nowrap">{{ item.violate }}</td>

                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
import { ref, onMounted, computed, watchEffect } from "vue";
import { useRoute } from "vue-router";
import { useTeacherStore } from "../../../stores/modules/teacher";
import router from "../../../router";

export default {
    setup() {
        const data = ref([]);
        const route = useRoute();
        const teacherStore = useTeacherStore();

        const webSocket = () => {
            const WS = new WebSocket(`${import.meta.env.VITE_APP_WS}teacher`);
            WS.onopen = (event) => {
                let token = localStorage.getItem("token");
                let auth = {
                    command: "AUTHENTICATE",
                    detail: {
                        token: token,
                    },
                };
                WS.send(JSON.stringify(auth));
                WS.onmessage = (event) => {
                    let receivedData = JSON.parse(event.data);
                    let joingr;
                    if (receivedData.status === 200) {
                        joingr = {
                            command: "JOIN GROUP TEST",
                            detail: {
                                group_test_id: route.params.testId,
                            }
                        }
                    }
                    WS.send(JSON.stringify(joingr));
                    WS.onmessage = (event) => {
                        let receivedData = JSON.parse(event.data);
                        if (receivedData.status === 200) {
                            WS.onmessage = (event) => {
                                let receivedData = JSON.parse(event.data);
                                //6console.log(receivedData);

                                data.value.forEach((stu) => {
                                    console.log(stu)
                                    if (stu.student.id == receivedData.student.id) {
                                        stu.violate = receivedData.violate;
                                        if (receivedData.score) {
                                            stu.score = receivedData.score;
                                        }
                                        if (receivedData.state === "WORKING") {
                                            stu.state = 'Đang làm'
                                        } else if (receivedData.state === "SUBMIT") {
                                            stu.state = "Đã nộp bài"
                                        }

                                    }
                                })

                            };
                        };
                    };
                };
            };

        };

        onMounted(async () => {
            data.value = await teacherStore.getStudentTest(route.params.testId);
            webSocket();
        });

        const getTestHistory = async (item) => {
            teacherStore.tmpTest = item;
            if (item) {
                router.push({ name: "testHistory" });
            }
        };

        return {
            data,
            getTestHistory,
        };
    },
};
</script>