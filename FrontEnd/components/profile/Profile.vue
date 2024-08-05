<template>
    <div class="container mx-auto p-4">
        <div class="flex flex-cols-2 space-x-20">
            <div class="avt bg-white shadow-md rounded-md p-6 w-full text-center">
                <div class="flex-row">
                    <img :src="img + 'static/'+ user.avatar_path" class="rounded-full w-64 h-64 text-center">

                    <a-button class="flex relative left-20 mt-3" type="primary" @click="showModal">Chọn
                        ảnh</a-button>
                    <a-modal v-model:open="open" title="Cập nhật ảnh đại diện" @ok="handleOk">
                        <template #footer>
                            <a-button key="back" @click="handleCancel">Hủy</a-button>
                            <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Lưu</a-button>
                        </template>
                        <label for="file-upload"
                            class="flex rounded-md px-8 py-2 border-2 fixed left-1/2 -ml-10 border-transparent bg-blue-500 focus:outline-none text-white placeholder-gray-400 transition-all duration-300 shadow-md">
                            Tải ảnh lên
                        </label>
                        <input id="file-upload" type="file" @change="handleFileChange" class="hidden mb-4" multiple />
                        <!-- Add this line -->
                        <img :src="imagePreview" alt="Preview Image" class="mt-4 w-32 h-32 rounded-md bg-gray-200" />
                    </a-modal>

                </div>
                <h1 class="text-2xl font-bold text-center">{{ user.name }}</h1>
                <p class="text-gray-500 text-center">{{ user.email }}</p>
            </div>

        </div>
    </div>
</template>

<script>
import { useStudentStore } from '../../stores/modules/student';
import { useTeacherStore } from '../../stores/modules/teacher';
import { ref } from 'vue';
import { useRoute } from 'vue-router';

export default {
    props: {
        user: Object
    },
    setup() {
        const teacherStore = useTeacherStore();
        const studentStore = useStudentStore();
        const img = import.meta.env.VITE_APP_API;

        const loading = ref(false);
        const open = ref(false);
        const file = ref(null);
        const imagePreview = ref(null);
        const formData = ref(new FormData()); // Define formData here

        const handleFileChange = async (e) => {
            file.value = Array.from(e.target.files);
            formData.value = new FormData(); // Reset formData
            formData.value.append('image', file.value[0]); // Use formData.value to access it

            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.value = e.target.result;
            }
            reader.readAsDataURL(file.value[0]);
        }

        const showModal = () => {
            open.value = true;
        };
        const route = useRoute();
        const handleOk = async () => {


            if (route.path.startsWith('/student')) {
                await studentStore.updateAvatar(formData.value);
            }
            else if (route.path.startsWith('/teacher')) {
                await teacherStore.updateAvatar(formData.value);
            }
            loading.value = true;

            loading.value = false;
            open.value = false;
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            img,
            loading,
            open,
            showModal,
            handleOk,
            handleCancel,
            handleFileChange,
            imagePreview,
            formData // Return formData so it can be used in the template
        }
    }
}
</script>