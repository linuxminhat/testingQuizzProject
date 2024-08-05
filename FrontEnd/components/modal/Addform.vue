<template>
    <div>
        <a-button type="primary" @click="showModal">Thêm mới</a-button>
        <a-modal v-model:open="open" title="Thêm bộ sưu tập" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2">Tên bộ sưu tập: </label>

                <input v-model="collectionName"
                    class="input rounded-md px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                    placeholder="Nhập tên..." required="" type="text" />



            </div>
        </a-modal>
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';

export default {
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const collectionName = ref('');
        const collection = computed(() => ({ name: collectionName.value }));


        const showModal = () => {
            open.value = true;
        };

        const handleOk = async () => {
            loading.value = true;
            addCollection(collection.value)

            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const addCollection = async (name) => {
            const result = await teacherStore.addCollection(name);
            collectionName.value = result;
            open.value = false;
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            open,
            loading,
            collectionName,
            collection,
            showModal,
            handleOk,
            handleCancel,
            addCollection
        };
    }
}
</script>