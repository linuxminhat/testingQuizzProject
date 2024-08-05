<template>
    <div>
        <a-button type="primary" @click="showModal">Tham gia nhóm</a-button>
        <a-modal v-model:open="open" title="Tham gia nhóm" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2">Mã lớp: </label>

                <input v-model="groupId"
                    class="input rounded-md px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                    placeholder="Nhập mã nhóm..." required="" type="text" />

            </div>
        </a-modal>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';

export default {
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const groupId = ref('')



        const showModal = () => {
            open.value = true;
        };

        const handleOk = async () => {
            loading.value = true;


            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };


        const handleCancel = () => {
            open.value = false;
        };

        return {
            open,
            loading,
            groupId,


            showModal,
            handleOk,
            handleCancel

        };
    }
}
</script>