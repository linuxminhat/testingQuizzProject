<template>

    <div class="h-full grid grid-cols-2 gap-4">
        <div class="flex items-center">
            <!-- <form class="relative w-3/4 h-24">
                <button class="absolute left-2 transform -translate-y-1/2 top-1/3 mt-1 p-1">
                    <svg width="17" height="16" fill="none" xmlns="http://www.w3.org/2000/svg" role="img"
                        aria-labelledby="search" class="w-5 h-5 text-gray-700">
                        <path d="M7.667 12.667A5.333 5.333 0 107.667 2a5.333 5.333 0 000 10.667zM14.334 14l-2.9-2.9"
                            stroke="currentColor" stroke-width="1.333" stroke-linecap="round" stroke-linejoin="round">
                        </path>
                    </svg>
                </button>
                <input
                    class="rounded-full h-1/2 w-3/4 px-8 py-3 border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                    placeholder="Nhập mã lớp" required="" type="text" />
                <button type="reset" class="absolute transform -translate-y-1/2 top-1/3 left-2/3">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-700" fill="none"
                        viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                </button>
            </form> -->
        </div>


        <div class="flex     justify-end items-center hover:cursor-pointer">
            <router-link :to="currentProfileRoute">
                <img :src="img+'static/'+ profile"
                    class="rounded-full w-12 h-12 text-center absolute transform -translate-x-2/3  top-2">

            </router-link>
        </div>



    </div>


</template>

<script>
import { computed, onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useStudentStore } from '../../stores/modules/student';
import { useTeacherStore } from '../../stores/modules/teacher';

export default {
    setup() {
        const route = useRoute();
        const profile = ref(null);
        const studentStore = useStudentStore();
        const teacherStore = useTeacherStore();

        const img = import.meta.env.VITE_APP_API;
        const currentProfileRoute = computed(() => {
            console.log(route.path)
            return route.path.startsWith('/student') ? { name: 'student - profile' } : { name: 'teacher-profile' };
        });

        onMounted(async () => {
            if (route.path.startsWith('/student')) {
                const res = await studentStore.getInfor();
                profile.value = res.avatar_path.replace(/\\\\/g, '/');
            }
            else if (route.path.startsWith('/teacher')) {
                const res = await teacherStore.getInfor();
                profile.value = res.avatar_path.replace(/\\\\/g, '/');
            }
        })

        return {
            currentProfileRoute,
            profile,
            img

        };
    }
}
</script>

<style scoped>

</style>