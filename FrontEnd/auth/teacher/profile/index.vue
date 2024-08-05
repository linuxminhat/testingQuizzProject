<template>
    <profile :user="teacher" />
    <update-profile class="flex justify-center items-center" />
</template>

<script>
import Profile from '../../../components/profile/Profile.vue'
import { useTeacherStore } from '../../../stores/modules/teacher';
import { ref, onMounted } from 'vue';
import UpdateProfile from '../../../components/modal/updateProfile.vue';
export default {
    components: {
        Profile,
        UpdateProfile
    },
    setup() {
        const teacher = ref({});
        const teacherStore = useTeacherStore();

        onMounted(async () => {
            const teacherInfo = await teacherStore.getInfor();
            console.log(teacherInfo); // In ra giá trị trả về từ getInfor()

            if (teacherInfo && teacherInfo.avatar_path) {
                teacher.value = teacherInfo;
                teacher.value.avatar_path = teacher.value.avatar_path.replace(/\\\\/g, '/');

                console.log(teacher.value)
            }
        });
        return {

            teacher
        }

    }

}
</script>

<style Profile>

</style>