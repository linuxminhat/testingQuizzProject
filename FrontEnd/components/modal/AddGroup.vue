<template>
    <div>
        <a-button type="primary" @click="showModal">Tạo nhóm mới</a-button>
        <a-modal v-model:open="open" title="Tạo nhóm mới" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2">Tên nhóm: </label>

                <input v-model="groupName"
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
        const groupName = ref('');
        const group = computed(() => ({ name: groupName.value }));


        const showModal = () => {
            open.value = true;
        };

        const handleOk = async () => {
            loading.value = true;
            addGroup(group.value)

            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const addGroup = async (name) => {
            const result = await teacherStore.addGroup(name);
            groupName.value = result;
            open.value = false;
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            open,
            loading,
            groupName,
            showModal,
            handleOk,
            handleCancel
        };
    }
}
</script>