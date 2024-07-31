<template>
    <div class="p-10">
        <timer :minutes="duration" class="fixed" @time-up="submitTest" />

        <div class="flex items-center justify-center min-h-screen">
            <div class="w-full max-w-4xl bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div v-for="(question, index) in paginatedQuestions"
                    :key="(currentPage-1)*paginatedQuestions.length + index" class="mb-6" :id="`${currentPage}`">
                    <question-box :question="question"
                        :questionIndex="(currentPage-1)*paginatedQuestions.length + index "
                        @answer-selected="addAnswer($event, (currentPage-1)*paginatedQuestions.length + index)" />
                </div>
                <div class="text-right ">
                    <a-button @click="showConfirm" class="bg-blue-500 text-white rounded-md">Nộp bài</a-button>
                </div>
                <div class="pagination space-x-3">
                    <a-button @click="prevPage" :disabled="currentPage === 1 || allow_move">Trước</a-button>
                    <span class=" space-x-3">Trang {{ currentPage }} trên {{ totalPages }}</span>
                    <a-button @click="nextPage" :disabled="currentPage === totalPages">Tiếp theo</a-button>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue';
import { useStudentStore } from '../../../stores/modules/student';
import QuestionBox from '../../../components/test/QuestionBox.vue';
import Timer from '../../../components/test/Timer.vue';


import { Modal } from 'ant-design-vue';
import { h } from 'vue';
import { ExclamationCircleOutlined } from '@ant-design/icons-vue';
import { useRouter } from 'vue-router';
import { useWebSocketStore } from '../../../stores/modules/webSocket';
import { eventType } from 'ant-design-vue/es/_util/type';
import { useToast } from 'vue-toastification';
import { all } from 'axios';
import Point from './Point.vue';
import teacher from '../../../apis/modules/teacher';
import student from '../../../apis/modules/student';
export default {
    components: {
        QuestionBox,
        Timer,
        Point
    },
    setup() {

        const questions = ref([]);
        const currentPage = ref(1);
        const questionsPerPage = ref(null);
        const duration = ref(null);
        const tabSwitchCount = ref(0);
        const totalPages = computed(() => (questions.value.length / questionsPerPage.value));
        const allow_move = ref(true);


        const paginatedQuestions = computed(() => {
            const startIndex = (currentPage.value - 1) * parseInt(questionsPerPage.value);
            const endIndex = startIndex + parseInt(questionsPerPage.value);
            // console.log(startIndex)
            // console.log(endIndex)
            // console.log(questions.value.slice(startIndex, endIndex))
            console.log('currentPage.value', currentPage.value);

            return questions.value.slice(startIndex, endIndex);


        });


        let url = import.meta.env.VITE_APP_WS;
        const WS = ref(new WebSocket(url + 'student'));

        const nextPage = () => {
            if (currentPage.value < totalPages.value) {
                currentPage.value++;

            }
        };

        const prevPage = () => {
            if (currentPage.value > 1) {
                currentPage.value--;
            }
        };


        onMounted(async () => {
            let test = await localStorage.getItem('test');
            duration.value = localStorage.getItem("duration");
            allow_move.value = localStorage.getItem("allow_move");
            questionsPerPage.value = localStorage.getItem("n_page");
            console.log(questionsPerPage.value)
            const parsedTest = JSON.parse(test);
            questions.value = parsedTest.student_work;

            WS.value.onopen = (event) => {
                console.log("Connection opened", event);

                let token = localStorage.getItem("token");

                let auth = {
                    command: "AUTHENTICATE",
                    detail: {
                        token: token,
                    },
                };
                WS.value.send(JSON.stringify(auth));

                WS.value.onmessage = (event) => {
                    let data = JSON.parse(event.data);
                    if (data.message == "Authenticated") {
                        let join = {
                            command: "JOIN GROUP TEST",
                            detail: {
                                group_test_id: localStorage.getItem("group_test_id"),
                                password: localStorage.getItem("pass")
                            }
                        }

                        WS.value.send(JSON.stringify(join));
                        WS.value.onmessage = (event) => {
                            let data = JSON.parse(event.data)
                            if (data.status == 403) {
                                useToast().error("Sai mật khẩu");
                            } else if (data.status == 200) {

                                let get_test = {
                                    command: "GET TEST"
                                }
                                WS.value.send(JSON.stringify(get_test));
                                WS.value.onmessage = (event) => {
                                    let data = JSON.parse(event.data);
                                    if (data.status == 400) {
                                        useToast().warning("Bạn đã làm bài kiểm tra này")
                                        // } else if (data.status == 200) {
                                        //     WS.value.send(JSON.stringify(submitData.value))
                                        //     WS.value.onmessage = (event) => {
                                        //         let data = JSON.parse(event.data);
                                        //         console.log(data);
                                        //         if (data.status == 200) {

                                        //             localStorage.setItem("score", data.message.score);
                                        //             localStorage.setItem("violations", tabSwitchCount.value);
                                        //             router.push('/point');

                                        //         }
                                        //     }
                                        // }
                                    }
                                }
                            }
                        }


                    } else {
                        console.error('Authentication failed:', data.message);
                    }
                };
            }



        });







        //  không nhấn chuột phải
        const contextMenuHandler = (event) => {
            event.preventDefault();

        };

        onMounted(() => {
            window.addEventListener('contextmenu', contextMenuHandler);
        });

        onUnmounted(() => {
            window.removeEventListener('contextmenu', contextMenuHandler);
        });

        // popup cảnh báo khi đóng cửa sổ
        onMounted(() => {
            window.addEventListener('beforeunload', handleBeforeUnload);
        });

        onUnmounted(() => {
            window.removeEventListener('beforeunload', handleBeforeUnload);
        });

        const handleBeforeUnload = (event) => {
            event.preventDefault();
            event.returnValue = '';
        };
        //chặn phím
        window.addEventListener('keydown', function (e) {
            if (e.key === 'F5' || e.key === 'Ctrl' || e.key === 'Tab' || e.key === 'Alt') {
                e.preventDefault();
            }
        });


        // đếm số lần chuyển tab
        const handleVisibilityChange = () => {
            let tabSwitchLim = localStorage.getItem('tolerance')
            if (tabSwitchLim > 1) {
                if (document.visibilityState === 'hidden') {
                    tabSwitchCount.value++;

                    WS.value.send(JSON.stringify({
                        command: "VIOLATE",
                    }));
                    WS.value.onmessage = (event) => {
                        let data = JSON.parse(event.data);
                        console.log(data);
                        const studentStore = useStudentStore();
                        if (data.message.score) {
                            console.log(data.message.score)
                            studentStore.score = data.message.score;
                            studentStore.violations = tabSwitchLim;
                            localStorage.setItem("score", data.message.score);
                            localStorage.setItem("violations", tabSwitchLim)

                        }
                    }

                    if (tabSwitchCount.value >= tabSwitchLim) {

                        router.push({
                            name: 'student-point',
                            // params: {
                            //     score: data.message.score,
                            //     violations: tabSwitchCount.value
                            // }
                        });

                    } else {
                        Modal.warning({
                            title: 'phát hiện hành vi gian lận!',
                            content: h('div', { style: 'color:red;' },
                                `Bạn đã chuyển tab ${tabSwitchCount.value} lần. Nếu chuyển tab quá ${tabSwitchLim} lần, bài kiểm tra sẽ tự động nộp.`,),
                        });

                    }
                }
            }
        };

        document.addEventListener('visibilitychange', handleVisibilityChange);
        onUnmounted(() => {
            document.removeEventListener('visibilitychange', handleVisibilityChange);
        });






        const addAnswer = (answer, index) => {
            // console.log({
            //     detail: {
            //         index: index,
            //         answer: [answer]
            //     }
            // });

            WS.value.send(JSON.stringify({
                command: "ANSWER",
                detail: {
                    index: index,
                    answer: answer.answer
                }
            }));
            // WS.value.onmessage = (event) => {
            //     let data = JSON.parse(event.data);
            //     console.log(data);

            // }




        }
        // const submitTest = () => {

        //     WS.value.send(JSON.stringify({
        //         command: "SUBMIT TEST",

        //     })); 

        //     WS.value.onmessage = (event) => {
        //         let data = JSON.parse(event.data);
        //         console.log(data);

        //     }


        // }
        const router = useRouter();
        const submitTest = () => {
            WS.value.send(JSON.stringify({
                command: "SUBMIT TEST",

            }));

            const studentStore = useStudentStore();
            WS.value.onmessage = (event) => {
                let data = JSON.parse(event.data);
                console.log(data.message)

                if (data.status == 200) {
                    studentStore.score = data.message.score;
                    localStorage.setItem("score", data.message.score);
                    studentStore.violations = tabSwitchCount.value;
                    localStorage.setItem("violations", tabSwitchCount.value)
                    router.push({
                        name: 'student-point',
                        // params: {
                        //     score: data.message.score,
                        //     violations: tabSwitchCount.value
                        // }
                    });

                }

            }

        }

        const showConfirm = () => {
            Modal.confirm({
                title: 'Bạn chắc chắn nộp bài?',
                icon: h(ExclamationCircleOutlined),
                content: h(
                    'div',
                    {
                        style: 'color:red;',
                    },
                    '',
                ),
                onOk() {

                    submitTest();

                },
                onCancel() {
                    console.log('Hủy');
                },
                class: 'test',
            });
        };

        return {
            questions,
            currentPage,
            totalPages,
            paginatedQuestions,
            duration,
            tabSwitchCount,
            handleVisibilityChange,
            showConfirm,
            allow_move,
            WS,
            submitTest,
            showConfirm,


            nextPage,
            prevPage,
            addAnswer
        };
    }
};
</script>