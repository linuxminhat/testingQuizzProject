<template>
    <div class="bg-gray-100 shadow-lg rounded-lg p-6 w-64 h-64 m-4">
        <h2 class="text-2xl font-semibold mb-4">{{ question.text }}</h2>
        <div v-for="answer in question.answers" :key="answer.id">
            <input type="radio" :id="answer.id" :name="question.id" :value="answer.id"
                v-model="userAnswers[question.id]">
            <label :for="answer.id">{{ answer.text }}</label>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        question: {
            type: Object,
            required: true
        },
        userAnswers: {
            type: Object,
            required: true
        }

    }
}
</script>

<style>

</style>