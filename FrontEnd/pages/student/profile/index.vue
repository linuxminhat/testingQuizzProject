<template>
    <profile :user="student" />
</template>

<script>
import Profile from '../../../components/profile/Profile.vue'
import { useStudentStore } from '../../../stores/modules/student';
import { ref, onMounted } from 'vue';
export default {
    components: {
        Profile
    },
    setup() {
        const student = ref({});
        const studentStore = useStudentStore();

        onMounted(async () => {
            const studentInfor = await studentStore.getInfor();


            if (studentInfor && studentInfor.avatar_path) {
                student.value = studentInfor;
                student.value.avatar_path = student.value.avatar_path.replace(/\\\\/g, '/');


            }
        });
        return {

            student
        }

    }

}
</script>

<style Profile>

</style>