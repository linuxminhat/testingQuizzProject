<template>
    <div class="flex h-screen">
        <div class="text-3xl font-bold text-center">
            Thời gian còn lại: {{ minutes }}:{{ seconds < 10 ? '0' + seconds : seconds }} </div>
        </div>
</template>
<script>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue';

export default {
    name: 'CountdownTimer',
    props: {
        minutes: {
            type: Number,
            required: true
        }
    },
    setup(props, { emit }) {
        let interval;
        const totalSeconds = ref(props.minutes * 60);
        const minutes = ref(Math.floor(totalSeconds.value / 60));
        const seconds = ref(totalSeconds.value % 60);

        const updateCountdown = () => {
            if (totalSeconds.value > 0) {
                totalSeconds.value--;
                minutes.value = Math.floor(totalSeconds.value / 60);
                seconds.value = totalSeconds.value % 60;
            } else {
                emit('time-up');
            }
        };

        onMounted(() => {
            interval = setInterval(updateCountdown, 1000);
        });

        onBeforeUnmount(() => {
            clearInterval(interval);
        });

        watch(() => props.minutes, (newVal) => {
            totalSeconds.value = newVal * 60;
            minutes.value = newVal;
            seconds.value = 0;
        });

        return {
            minutes,
            seconds
        };
    },
};
</script>