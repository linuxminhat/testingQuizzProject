<template>
    <div>
        Bắt đầu làm bài
    </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';

export default {
    setup() {
        const WS = ref(null);

        const sendMessage = () => {
            if (WS.value) {
                WS.value.send('Hello, server!');
            }
        };

        onMounted(() => {
            WS.value = new WebSocket('ws://localhost:4444');

            WS.value.onopen = function (event) {
                console.log('Connection opened', event);
            };

        });

        // onUnmounted(() => {
        //     if (WS.value) {
        //         WS.value.close();
        //     }
        // });

        return {
            sendMessage
        };
    }
};
</script>