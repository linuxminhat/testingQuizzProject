<template>
    <div class="bg-gray-100 p-4 rounded-lg shadow-md m-4 flex items-center justify-between">
        <div class="flex items-center">
            <img :src="imgUrl+'static/'+ user.avatar_path" class="rounded-full w-64 h-64 text-center">
            <div class="ml-4">
                <h2 class="text-xl font-bold">{{ student.name }}</h2>
                <p class="text-gray-600">{{ student.email }}</p>
            </div>
        </div>
        <div>
            <button @click="acceptStudent(student.id)" class="bg-blue-500 text-white px-4 py-2 rounded">Chấp
                nhận</button>
            <!-- <button @click="deleteStudent(student.id)" class="bg-red-500 text-white px-4 py-2 rounded ml-2">Xóa</button> -->
        </div>
    </div>

</template>

<script>

import { useTeacherStore } from '../../stores/modules/teacher';
import { ref } from 'vue';
export default {
    props: {
        student: {
            type: Object,
            required: true
        },

    },
    setup() {
        const teacherStore = useTeacherStore();
        const studentId = ref({
            student_id: []
        });
        const imgUrl = import.meta.env.VITE_APP_API;
        const acceptStudent = (id) => {
            studentId.value.student_id.push(id);
            teacherStore.addStudent(studentId.value, teacherStore.groupId);
        }
        const deleteStudent = (id) => {
            studentId.value.student_id.push(id);
            teacherStore.refuseStudent(studentId.value.student_id, teacherStore.groupId);
        }
        return {
            studentId,
            imgUrl,
            acceptStudent, deleteStudent
        }
    }
}
</script>

<style>

</style>