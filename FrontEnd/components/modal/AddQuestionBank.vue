<template>
    <div>
        <a-button type="primary" @click="showModal">Thêm mới</a-button>
        <a-modal v-model:open="open" title="Thêm bộ câu hỏi" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2">Tên bộ câu hỏi: </label>

                <input v-model="name"
                    class="input rounded-md px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                    placeholder="Nhập tên..." required="" type="text" />



            </div>
        </a-modal>
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const name = ref('');
        const route = useRouter();
        const questionBank = computed(() => ({ collection_id: route.currentRoute.value.params.id, name: name.value }));
        teacherStore.tmpCollectionId = route.currentRoute.value.params.id;
        const showModal = () => {
            open.value = true;
        };

        const handleOk = async () => {
            loading.value = true;
            await addQuestionBank(questionBank.value);

            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const addQuestionBank = async (Bank) => {
            await teacherStore.addQuestionBank(Bank);
            open.value = false;
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            open,
            loading,
            name,
            questionBank,
            showModal,
            handleOk,
            handleCancel,
            addQuestionBank
        };
    }
}
</script>