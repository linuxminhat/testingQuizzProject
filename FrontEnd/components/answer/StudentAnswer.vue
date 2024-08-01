<template>
    <div>
        <div v-if="multipleCorrectAnswers">
            <div v-for="(answer, index) in answers.text" :key="index" class="flex items-center">
                <input type="checkbox" :checked="studentAnswer.includes(index)" :disabled="true" class="mr-2">
                <label :class="getAnswerClass(index)">{{ answer }}</label>
            </div>
        </div>
        <div v-else>
            <div v-for="(answer, index) in answers.text" :key="index" class="flex items-center">
                <input type="radio" :checked="studentAnswer.includes(index)" :disabled="true" class="mr-2">
                <label :class="getAnswerClass(index)">{{ answer }}</label>
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
            type: Array,
            required: true
        }
    },
    computed: {
        multipleCorrectAnswers() {
            return this.answers.correct.length > 1;
        }
    },
    methods: {
        getAnswerClass(index) {
            if (this.studentAnswer.includes(index)) {
                return this.answers.correct.includes(index) ? 'text-green-500' : 'text-red-500';
            } else if (this.answers.correct.includes(index)) {
                return 'text-green-500';
            }
            return '';
        }
    }
}
</script>