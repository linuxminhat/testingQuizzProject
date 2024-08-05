<template>
    <div>
        <a-button type="primary" @click="showModal">Cập nhật</a-button>
        <a-modal v-model:open="open" title="Cập nhật thông tin cá nhân" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2 font-bold">Họ và tên mới: </label>
                <input v-model="name"
                    class="rounded-md mb-4 px-8 py-2 border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                    placeholder="Nhập họ và tên..." required="" type="text" />
                <label class="block mb-2 font-bold">Mật khẩu mới: </label>
                <input v-model="password"
                    class="rounded-md mb-4 px-8 py-2 border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                    placeholder="Nhập mật khẩu..." required="" type="password" />




            </div>
        </a-modal>
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useTeacherStore } from '../../stores/modules/teacher';
import { useStudentStore } from '../../stores/modules/student';

export default {
    setup() {

        const loading = ref(false);
        const open = ref(false);
        const imagePreview = ref(null);

        const name = ref('');
        const password = ref('');
        const route = useRoute();
        const data = ref({
            name: name.value,
            password: password.value
        })

        const teacherStore = useTeacherStore();
        const studentStore = useStudentStore();


        const store = computed(() => {

            if (route.path.startsWith('/student')) {
                return studentStore;
            } else {
                return teacherStore;
            }
        });

        const handleFileChange = (e) => {
            const file = e.target.files[0];
            if (file) {
                imagePreview.value = URL.createObjectURL(file);
                console.log(imagePreview.value);
            }
        };

        const showModal = () => {
            open.value = true;
        };

        const handleOk = async () => {
            console.log(route.params)



            loading.value = true;

            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 3000);
        };
        const handleCancel = () => {
            open.value = false;
        };

        return {
            loading,
            open,
            imagePreview,

            name,
            password,

            handleFileChange,
            showModal,
            handleOk,
            handleCancel
        };
    }
};
</script>