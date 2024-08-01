<template>
    <div>
        <div v-if="multipleCorrectAnswers">
            <div v-for="(answer, index) in answers.text" :key="index" class="flex items-center">
                <input type="checkbox" :checked="answers.correct.includes(index)" :disabled="true" class="mr-2">
                <label>{{ answer }}</label>
            </div>
        </div>
        <div v-else>
            <div v-for="(answer, index) in answers.text" :key="index" class="flex items-center">
                <input type="radio" :checked="answers.correct.includes(index)" :disabled="true" class="mr-2">
                <label>{{ answer }}</label>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        answers: {
            type: Object,
            required: true
        },
        studentAnswer: {
            type: Object,
            required: true
        }
    },
    computed: {
        multipleCorrectAnswers() {
            return this.answers.correct.length > 1;
        }
    }
}
</script>

<style>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
</style>