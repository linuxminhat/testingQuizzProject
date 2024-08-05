<template>
    <div>
        <a-button type="primary" @click="showModal">Tạo bài kiểm tra</a-button>
        <a-modal v-model:open="open" title="Tạo bài kiểm tra" @ok="handleOk" :width="800">
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
            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Chọn bộ sưu tập: </label>
                <select name="" id=""
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    v-model="selectedCollection">
                    <option v-for="collection in collections" :key="collection.id" :value="collection.id">
                        {{ collection.name }}
                    </option>
                </select>
            </div>
            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Chọn đề thi: </label>
                <select name="" id=""
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    v-model="testId">
                    <option v-for="test in tests" :key="test.id" :value="test.id">
                        {{ test.name }}
                    </option>
                </select>
            </div>
            <div class="grid grid-cols-2">
                <div class="flex items-center p-4">
                    <label class="w-1/3 mb-2">Bắt đầu: </label>
                    <input type="datetime-local" v-model="startTime"
                        class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
                </div>
                <div class="flex items-center p-4">
                    <label class="w-1/3 mb-2"> Kết thúc: </label>
                    <input type="datetime-local" v-model="endTime"
                        class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
                </div>
            </div>
            <div class="grid grid-cols-2">
                <div class="flex items-center p-4">
                    <label class="w-1/3 mb-2">Thời gian làm bài: </label>
                    <input type="number" v-model="duration" min="1"
                        class="w-1/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
                    <label class="w-1/4 mb-2 mx-2">Phút </label>

                </div>
                <div class="flex items-center p-4 ">
                    <label class="w-1/3 ">Trộn đề: </label>
                    <input type="checkbox" v-model="shuffle"
                        class="w-2/3 h-6 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded" />
                </div>
            </div>
            <div class="grid grid-cols-2">
                <div class="flex items-center p-4">
                    <label class="w-1/2 mb-2">Mật khẩu bài thi: </label>
                    <input :type="showPassword ? 'text' : 'password'" v-model="password" @blur="validatePassword"
                        autocomplete="current-password" :class="`w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500focus:outline-none ${
                                passwordError
                                    ? 'border-red-500'
                                    : 'border-gray-300 focus:border-blue-500'
                            }`" placeholder="Mật khẩu" />
                    <button type="button" v-if="!passwordError" class="absolute left-1/2 -ml-12"
                        @click="togglePasswordVisibility">
                        <img v-if="showPassword" src="/src/assets/icon/show.png" alt="" class="h-6 w-6">
                        <img v-else src="/src/assets/icon/hide.png" alt="" class="h-6 w-6">
                    </button>

                </div>
                <div class="flex items-center p-4 ">
                    <label class="w-1/3 ">Số lần vi phạm: </label>
                    <input type="number" v-model="tolerance" min="0"
                        class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
                </div>
            </div>
            <div class="grid grid-cols-2">

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
            </div>

        </a-modal>
    </div>
</template>

<script>
import { ref, watch } from "vue";
import { useTeacherStore } from "../../stores/modules/teacher";
import Vue3TagsInput from "vue3-tags-input";
import { useRouter } from 'vue-router';
export default {
    components: { Vue3TagsInput },
    setup() {
        function formatDate(date) {
            if (date instanceof Date) {
                let month = '' + (date.getMonth() + 1),
                    day = '' + date.getDate(),
                    year = date.getFullYear();

                if (month.length < 2)
                    month = '0' + month;
                if (day.length < 2)
                    day = '0' + day;

                return [year, month, day].join('-');
            } else {
                console.error('formatDate called with non-Date object:', date);
                return null;
            }
        }
        const startTime = ref(formatDate(new Date()));
        const endTime = ref(formatDate(new Date()));
        const router = useRouter()
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const name = ref('')
        const testId = ref('')
        const collections = ref([])
        const showPassword = ref(false);
        const n_page = ref(1);
        const allow_move = ref(true);

        const duration = ref('')
        const shuffle = ref(false)
        const selectedCollection = ref(null)
        const tests = ref([])
        const password = ref('');
        const tolerance = ref('');
        const data = ref({
            group_id: router.currentRoute.value.params.id,
            test_id: testId.value,
            name: name.value,
            start: startTime.value,
            end: endTime.value,
            duration: duration.value,
            shuffle: shuffle.value,
            password: password.value,
            tolerance: tolerance.value,
            n_page: n_page.value,
            allow_move: allow_move.value

        });
        const togglePasswordVisibility = () => {
            showPassword.value = !showPassword.value;
        };
        watch([name, testId, startTime, endTime, duration, shuffle, password, tolerance, n_page, allow_move], () => {
            data.value = {
                group_id: router.currentRoute.value.params.id,
                test_id: testId.value,
                name: name.value,
                start: startTime.value,
                end: endTime.value,
                duration: duration.value,
                shuffle: shuffle.value,
                password: password.value,
                tolerance: tolerance.value,
                n_page: n_page.value,
                allow_move: allow_move.value

            };
        }, { immediate: true, deep: true });
        watch(selectedCollection, async (newCollectionId) => {
            if (newCollectionId) {
                tests.value = await teacherStore.getTests(newCollectionId);


            }
        });

        const showModal = async () => {
            open.value = true;
            collections.value = await teacherStore.getCollections();
        };


        const handleOk = async () => {
            loading.value = true;
            console.log(data.value);

            const payload = {
                ...data.value,
                start: formatDate(new Date(startTime.value)),
                end: formatDate(new Date(endTime.value)),
            };
            await teacherStore.addTestInGroup(payload);

            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            router,
            open,
            loading,
            tests,
            name,
            testId,
            startTime,
            endTime,
            duration,
            shuffle,
            collections,
            selectedCollection,
            showPassword,
            password,
            tolerance,
            n_page,
            allow_move,
            togglePasswordVisibility,
            formatDate,
            showModal,
            handleOk,
            handleCancel,
        };
    },
};
</script>
