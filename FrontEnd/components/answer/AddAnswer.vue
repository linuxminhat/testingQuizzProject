<template>
    <div>
        <div v-for="(answer, index) in answers" :key="index" class="mb-2">
            <input v-model="answer.text" type="text" placeholder="Nhập đáp án tại đây" />
            <button @click="removeAnswer(index)">Xóa</button>
        </div>
        <button @click="addAnswer">Thêm đáp án</button>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: 'AddAnswer',
    setup() {
        const answers = ref([{ text: '' }]);

        const addAnswer = () => {
            answers.value.push({ text: '' });
        };

        const removeAnswer = (index) => {
            answers.value.splice(index, 1);
        };

        return {
            answers,
            addAnswer,
            removeAnswer,
        };
    },
};
</script>