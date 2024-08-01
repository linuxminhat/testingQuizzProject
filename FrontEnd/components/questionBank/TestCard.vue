<template>
    <div class="bg-white shadow-xl rounded-xl p-6 w-64 h-auto m-4 flex flex-col">
        <edit-group-test :test="test" class=" justify-end items-end flex" v-if="!isStudentRoute" />
        <div @click="getGroupTestId(test.id)">
            <h2 class="text-2xl font-semibold mb-4">{{ test.name }}</h2>
            <p class="font-bold">Bắt đầu: </p>
            <p class="text-gray-700">{{formatDate( test.start) }}</p>
            <p class="font-bold">Kết thúc: </p>
            <p class="text-gray-700">{{ formatDate(test.end) }}</p>
            <p class="font-bold">Thời gian làm bài: </p>
            <p class="text-gray-700">{{ test.duration }} phút</p>
            <p class="font-bold">Số lần vi phạm tối đa: </p>
            <p class="text-gray-700">{{ test.tolerance }} lần</p>
        </div>

        <a-button :disabled="isTestEnded" type="primary" @click="showModal" v-if="isStudentRoute">
            Bắt đầu làm bài
        </a-button>
        <a-modal v-model:open="open" title="Xác nhận vào thi" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Vào thi</a-button>
            </template>
            <div class="p-4">
                <p class="text-red-500 ">Trong quá trình làm bài, nếu chuyển tab quá {{ test.tolerance }} lần thì hệ
                    thống sẽ tự
                    động nộp bài</p>
            </div>
        </a-modal>
    </div>
</template>

<script>
import { format } from 'date-fns';
import { useRouter } from 'vue-router';
import { Modal } from 'ant-design-vue';
import { h, watchEffect, ref } from 'vue';
import { ExclamationCircleOutlined } from '@ant-design/icons-vue';
import { useStudentStore } from '../../stores/modules/student';
import EditGroupTest from '../modal/EditGroupTest.vue';
import websocket from './websocket.vue';
import { useWebSocketStore } from '../../stores/modules/webSocket'
import { useTeacherStore } from '../../stores/modules/teacher';
import { useToast } from 'vue-toastification';
export default {

    props: {
        test: {
            type: Object,
            required: true
        },
        history: {
            type: Number,
            required: false
        }

    },
    components: { EditGroupTest, websocket },
    setup(props) {
        const studentStore = useStudentStore();
        const teacherStore = useTeacherStore();
        const router = useRouter();
        const isTestEnded = ref(false);

        const open = ref(false);
        const WS = ref(null);
        const webSocketStore = useWebSocketStore();
        const showModal = () => {



            open.value = true;
        };
        const loading = ref(true)
        const handleOk = async () => {

            const width = window.screen.width;
            const height = window.screen.height;
            studentStore.group_test_id = props.test.id;
            localStorage.setItem('group_test_id', props.test.id);
            window.open('/auth', '_blank', `width=${width},height=${height}`);
            localStorage.setItem('tolerance', props.test.tolerance)
            localStorage.setItem('n_page', props.test.n_page)

            loading.value = true;
            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };
        const handleCancel = () => {
            open.value = false;
        };
        const isStudentRoute = router.currentRoute.value.path.startsWith('/student');
        const formatDate = (date) => {
            return format(new Date(date), 'dd/MM/yyyy - HH:mm');
        }



        const getGroupTestId = (testId) => {
            teacherStore.groupTestId = testId;

            router.push({
                name: "teacher-group-test",
                params: { groupId: teacherStore.groupId, testId: testId }
            });
        }

        if (isStudentRoute) {
            watchEffect(() => {
                let testEnded = (new Date(props.test.end) < new Date());
                let tested = props.history.some(his => props.test.id == his.group_test.id);

                console.log(tested)
                isTestEnded.value = testEnded || tested;
                console.log(isTestEnded.value)
            });
        }

        return {
            router,
            isStudentRoute,
            isTestEnded,
            open,
            getGroupTestId,
            showModal,
            handleOk,
            handleCancel,
            webSocketStore,


            WS,

            formatDate
        }
    }
}
</script>

<style>

</style>