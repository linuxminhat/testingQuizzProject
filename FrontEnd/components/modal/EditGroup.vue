<template>
    <button type="primary" @click="showModal" class="flex items-end justify-end">
        <svg class="feather feather-edit" fill="none" height="24" stroke="currentColor" stroke-linecap="round"
            stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" />
            <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" />
        </svg>
    </button>
    <a-modal v-model:open="open" title="Chỉnh sửa nhóm" @ok="handleOk">
        <template #footer>
            <a-button key="back" @click="handleCancel">Hủy</a-button>
            <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
        </template>
        <div class="flex items-center p-4">
            <label class="w-1/3 mb-2">Tên nhóm: </label>
            <input type="text" v-model="data.name"
                class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                placeholder="Nhập tên nhóm" />
        </div>
        <div class="flex items-center p-4">
            <label class="w-1/3 mb-2">Ẩn nhóm: </label>
            <input type="checkbox" v-model="data.is_show"
                class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                placeholder="Nhập tên nhóm" />
        </div>
        <label class="w-1/3  mx-4">Ảnh nhóm: </label>
        <div class="flex overflow-x-auto scrolling-touch scrollbar-thin scrollbar-hide">
            <!-- your images here -->
            <div v-for="(img,index) in images" :key="index" style="flex: 0 0 auto;">
                <img :src="'http://localhost:4444/static/'+ formattedImagePath(img)"
                    :class="`rounded-md w-32 h-32 text-center hover:cursor-pointer mx-2 ${selectedImages === img ? 'selected-image-border' : ''}`"
                    @click="selectImage(img)">
            </div>
        </div>

    </a-modal>
</template>
<script>
import { ref, computed } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
export default {
    props: {
        group: {
            type: Object,
            required: true
        }
    },
    setup(props) {
        const teacherStore = useTeacherStore();
        const images = ref([]);
        const open = ref(false);
        const selectedImages = ref('');
        const data = ref({
            id: null,
            name: '',
            is_show: false,
            image_path: ''
        });
        const showModal = async () => {
            console.log(props.group)
            images.value = await teacherStore.getImageGroups();
            open.value = true;
            data.value.id = props.group.id;
            data.value.name = props.group.name;
            data.value.is_show = props.group.is_show;
            data.value.image_path = selectedImages.value;
        };
        const handleOk = () => {
            console.log(data.value);
            teacherStore.updateGroup(data.value);
            open.value = false;
        };
        const selectImage = (img) => {
            selectedImages.value = img;
            data.value.image_path = img;

        };
        const handleCancel = () => {
            open.value = false;
        };
        const formattedImagePath = computed(() => {
            return img => img.replace(/\\/g, '/');
        });
        return {
            open,
            showModal,
            handleOk,
            handleCancel,
            selectImage,
            selectedImages,
            formattedImagePath,
            images,
            data
        }
    }
}
</script>
<style>
.selected-image-border {
  border: 4px solid blue; /* Đặt kích thước và màu sắc cho đường viền */
  border-radius: 6px; /* Đặt độ cong cho viền */
}

</style>
