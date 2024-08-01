<template>


    <div class="grid grid-cols-3 gap-2 shadow-md p-6 ">
        <div v-for="index in totalQuestions" :key="index" @click="goToQuestion(index)"
            class="cursor-pointer border rounded-full w-10 h-10 flex items-center justify-center hover:bg-gray-100"
            :class="{ 'bg-blue-200': answeredQuestions.includes(index-1) }">
            {{ index }}
        </div>
    </div>

</template>

<script>
export default {
    props: {
        totalQuestions: Number, // Số lượng câu hỏi
        answeredQuestions: Array // Mảng chứa các câu hỏi đã được trả lời
    },
    methods: {
        goToQuestion(index) {
            this.$emit('go-to-question', index);
        }
    }
};
</script>

<style scoped>
.bg-green-200 {
    background-color: #c6f6d5;
}
</style>