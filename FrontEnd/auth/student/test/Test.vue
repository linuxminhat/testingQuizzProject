<template>
    <div class="p-10 ">

        <timer :minutes="duration" class="fixed" @time-up="submitTest" />


        <div class="flex items-center justify-center min-h-screen">
            <div class="w-full max-w-4xl bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div v-for="(question, index) in questions.student_work" :key="index" class="mb-6"
                    :id="`question-${index+1}`">
                    <question-box :question="question" :questionIndex="index" @answer-selected="addAnswer" />
                </div>
                <a-button @click="showConfirm" class=" bg-blue-500 text-white rounded-md">Nộp bài</a-button>
            </div>


            <div class="fixed right-0 top-10">
                <Menu :totalQuestions="length" :answeredQuestions="answeredQuestions"
                    :selectedQuestion="selectedQuestion" @go-to-question="goToQuestion"
                    class="fixed right-0 top-1/2 mr-20" />
            </div>
        </div>
    </div>

</template>
<script>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue';
import { useStudentStore } from '../../../stores/modules/student';
import QuestionBox from '../../../components/test/QuestionBox.vue';
import Timer from '../../../components/test/Timer.vue';
import Menu from '../../../components/test/Menu.vue';

import { Modal } from 'ant-design-vue';
import { h } from 'vue';
import { ExclamationCircleOutlined } from '@ant-design/icons-vue';
import { useRouter } from 'vue-router';
import { useWebSocketStore } from '../../../stores/modules/webSocket';
import { eventType } from 'ant-design-vue/es/_util/type';
import { useToast } from 'vue-toastification';
export default {
    components: {
        QuestionBox,
        Timer,
        Menu
    },
    setup() {
        const studentStore = useStudentStore()
        const cheatingDetected = ref(false);
        const group_test_id = ref(null);
        const questions = ref([]);
        const userAnswers = reactive({});
        let student_answer = ref([]);
        const duration = ref(null);
        const length = ref(null)


        const tabSwitchCount = ref(0);

        duration.value = localStorage.getItem("duration");
        const selectedQuestion = ref(null);


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



        //  chặn chuột phải
        const contextMenuHandler = (event) => {
            event.preventDefault();

        };

        onMounted(() => {
            window.addEventListener('contextmenu', contextMenuHandler);
        });

        onUnmounted(() => {
            window.removeEventListener('contextmenu', contextMenuHandler);
        });


        //chặn phím
        window.addEventListener('keydown', function (e) {
            if (e.key === 'F5' || e.key === 'Ctrl' || e.key === 'Tab') {
                e.preventDefault();
            }
        });




        const WS = ref(new WebSocket(`${import.meta.env.WS}/student`));


        WS.value.onopen = (event) => {
            console.log("Connection opened", event);
        };


        const answeredQuestions = ref([]); // Mảng để theo dõi các câu hỏi đã được trả lời

        const addAnswer = (payload) => {
            const { questionId, answer } = payload;
            student_answer.value[questionId] = answer;
            selectedQuestion.value = questionId;
            answeredQuestions.value.push(questionId); // Thêm câu hỏi vào mảng câu hỏi đã trả lời
        }




        const submitTest = async () => {
            const submitData = computed(() => ({
                command: "SUBMIT TEST",
                detail: {
                    student_answer: student_answer.value
                }
            }));

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
                                } else if (data.status == 200) {
                                    WS.value.send(JSON.stringify(submitData.value))
                                    WS.value.onmessage = (event) => {
                                        let data = JSON.parse(event.data);
                                        console.log(data);
                                        if (data.status == 200) {

                                            localStorage.setItem("score", data.message.score);
                                            localStorage.setItem("violations", tabSwitchCount.value);
                                            router.push('/point');

                                        }
                                    }
                                }
                            }
                        }
                    }


                } else {
                    console.error('Authentication failed:', data.message);
                }
            };


            //console.log(submitData.value)

            // let res = null;
            // //res = await studentStore.testSubmit(data.value);
            // localStorage.setItem("score", res);
            // localStorage.setItem("violations", tabSwitchCount.value);
        };
        onMounted(async () => {
            let test = await localStorage.getItem('test');
            questions.value = JSON.parse(test);
            console.log(questions.value)
            group_test_id.value = localStorage.getItem("group_test_id");
            duration.value = localStorage.getItem("duration");
            if (questions.value && questions.value.student_work) {
                length.value = questions.value.student_work.length;
                student_answer = ref(Array(length).fill().map(() => []));
            }
            console.log(duration.value);
            document.addEventListener('visibilitychange', handleVisibilityChange);
        });

        // đếm số lần chuyển tab
        const handleVisibilityChange = () => {
            let tabSwitchLim = localStorage.getItem('tolerance')
            if (tabSwitchLim > 0) {
                if (document.hidden) {
                    tabSwitchCount.value++;
                    if (tabSwitchCount.value >= tabSwitchLim) {
                        submitTest();
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



        onUnmounted(() => {
            document.removeEventListener('visibilitychange', handleVisibilityChange);
        });


        const goToQuestion = (index) => {
            const questionElement = document.getElementById(`question-${index}`);
            if (questionElement) {
                questionElement.scrollIntoView({ behavior: 'smooth' });
            }
        };

        const router = useRouter();
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
                    //  router.push('/point');
                },
                onCancel() {
                    console.log('Hủy');
                },
                class: 'test',
            });
        };

        return {
            cheatingDetected,
            questions,
            userAnswers,
            student_answer,
            group_test_id,
            duration,
            length,
            selectedQuestion,
            answeredQuestions,
            WS,
            goToQuestion,
            showConfirm,
            addAnswer,
            submitTest,
            handleVisibilityChange
        };
    },
};
</script>
<style>
body {
  user-select: none;
}
</style>