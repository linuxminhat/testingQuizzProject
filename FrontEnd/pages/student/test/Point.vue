<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
        <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
            <h1 class="text-2xl font-bold mb-4">Kết quả bài kiểm tra</h1>
            <p class="mb-2">Điểm của bạn: <span class="font-bold">{{ score * 10 }}</span></p>
            <p>Số lần vi phạm: <span class="font-bold">{{ violations }}</span></p>
        </div>
    </div>
</template>
<script>
import { onMounted, onUnmounted, ref, watchEffect } from 'vue';
import { useStudentStore } from '../../../stores/modules/student';

export default {
    setup() {

        const studentStore = useStudentStore();
        const score = ref(null);
        const violations = ref(null);

        const clearLocalStorage = () => {
            localStorage.removeItem("score");
            localStorage.removeItem("violations");
        };

        onMounted(async () => {
            score.value = localStorage.getItem("score");
            violations.value = localStorage.getItem("violations");
            // console.log(score.value)
            location.reload();

        });

        onUnmounted(() => {
            window.removeEventListener('beforeunload', clearLocalStorage);
        });

        return {
            score,
            violations
        };
    }
}
</script>

<style scoped>
</style>