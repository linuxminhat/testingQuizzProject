<template>
    <!-- <a-button type="primary" @click="showModal">Open Modal</a-button> -->
    <button type="primary" @click="showModal" class="flex items-end justify-end hover:text-blue-500">
        <svg class="feather feather-edit" fill="none" height="24" stroke="currentColor" stroke-linecap="round"
            stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" />
            <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" />
        </svg></button>
    <a-modal v-model:open="open" title="Chỉnh sửa nhóm thi" @ok="handleOk" :width="800">
        <template #footer>
            <a-button key="back" @click="handleCancel">Hủy</a-button>
            <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
        </template>

        <label class="font-bold">Tên bài kiểm tra:</label>
        <input v-model="name" type="text"
            class="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />

        <div class="grid grid-cols-2">
            <div class="flex items-center p-4">
                <label class="font-bold">Bắt đầu:</label>
                <input v-model="start" type="datetime-local"
                    class="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />

            </div>
            <div class="flex items-center p-4">
                <label class="font-bold">Kết thúc:</label>
                <input v-model="end" type="datetime-local"
                    class="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />

            </div>
        </div>
        <label class="font-bold">Thời gian làm bài:</label>
        <input v-model="duration" type="number" min="1"
            class="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
        <label class="font-bold">Số lần vi phạm cho phép:</label>
        <input v-model="tolerance" type="number" min="1"
            class="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />

        <label class="w-1/2 mb-2 font-bold">Mật khẩu bài thi: </label>
        <input :type="showPassword ? 'text' : 'password'" v-model="password" @blur="validatePassword"
            autocomplete="current-password" :class="`w-full  px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500focus:outline-none ${
                                passwordError
                                    ? 'border-red-500'
                                    : 'border-gray-300 focus:border-blue-500'
                            }`" placeholder="Mật khẩu" />


        <button type="button" v-if="!passwordError" class="absolute right-16 mt-2" @click="togglePasswordVisibility">
            <img v-if="showPassword" src="/src/assets/icon/show.png" alt="" class="h-6 w-6">
            <img v-else src="/src/assets/icon/hide.png" alt="" class="h-6 w-6">
        </button>
        <div class="flex items-center p-4 ">
            <label class="w-1/3 ">Số câu trong 1 trang: </label>
            <input type="number" v-model="n_page" min="0"
                class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
        </div>
        <div class="flex items-center p-4 ">
            <label class="w-1/3 ">Quay lại trang trước: </label>
            <input type="checkbox" v-model="allow_move"
                class="w-2/3 h-6 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded" />
        </div>
    </a-modal>
</template>
<script>
import { reactive, ref, watch } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
export default {

    props: {
        test: {
            type: Object,
            required: true
        }
    },
    setup(props) {

        const password = ref('');
        const name = ref(props.test.name);
        const start = ref(props.test.start);
        const end = ref(props.test.end);
        const duration = ref(props.test.duration);
        const tolerance = ref(props.test.tolerance);
        const n_page = ref(props.test.n_page);
        const allow_move = ref(props.test.allow_move);

        const teacherStore = useTeacherStore();
        const data = reactive({
            id: props.test.id,
            name: name.value,
            start: start.value,
            end: end.value,
            duration: duration.value,
            tolerance: tolerance.value,
            password: password.value,
            n_page: n_page.value,
            allow_move: allow_move.value
        });

        watch([name, start, end, duration, tolerance, password, n_page, allow_move], () => {
            data.name = name.value;
            data.start = start.value;
            data.end = end.value;
            data.duration = duration.value;
            data.tolerance = tolerance.value;
            data.password = password.value;
            data.n_page = n_page.value;
            data.allow_move = allow_move.value;


        }, { immediate: true });
        const showPassword = ref(false);

        const togglePasswordVisibility = () => {
            showPassword.value = !showPassword.value;
        };
        const open = ref(false);
        const showModal = () => {
            open.value = true;
        };
        const handleOk = async () => {
            const updatedData = {
                id: props.test.id
            };
            Object.keys(data).forEach((key) => {
                if (key === 'password' && password.value === '') return; // skip empty password
                if (data[key] !== props.test[key]) {
                    updatedData[key] = data[key];
                }
            });
            await teacherStore.updateGroupTest(updatedData)
            console.log(updatedData)
            open.value = false;
        };
        const handleCancel = () => {
            open.value = false;
        };

        return {
            showPassword,
            togglePasswordVisibility,
            open,
            name,
            start,
            end,
            duration,
            tolerance,
            password,
            n_page,
            allow_move,

            data,
            showModal,
            handleOk,
            handleCancel
        }
    }
}
</script>
<style>

</style>