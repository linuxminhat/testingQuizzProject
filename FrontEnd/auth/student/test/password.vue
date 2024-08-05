<template>
    <div class="flex items-center justify-center h-screen bg-slate-200 rounded-lg ">
        <form class="w-1/3 p-4 bg-white shadow-lg rounded-lg" @submit.prevent="check">
            <label class="w-1/2 m-4">Mật khẩu bài thi: </label>
            <input :type="showPassword ? 'text' : 'password'" v-model="password" @blur="validatePassword"
                autocomplete="current-password" :class="`w-1/2 px-3 py-2 mt-3 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500focus:outline-none ${
                                    passwordError
                                        ? 'border-red-500'
                                        : 'border-gray-300 focus:border-blue-500'
                                }`" placeholder="Mật khẩu" />
            <button type="button" v-if="!passwordError" class="absolute left-1/5 -ml-10 mt-5    "
                @click="togglePasswordVisibility">
                <img v-if="showPassword" src="/src/assets/icon/show.png" alt="" class="h-6 w-6">
                <img v-else src="/src/assets/icon/hide.png" alt="" class="h-6 w-6">
            </button>
            <button type="submit"
                class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mx-5">
                Xác nhận
            </button>
        </form>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import Websocket from '../../../components/questionBank/websocket.vue';
import { useWebSocketStore } from '../../../stores/modules/webSocket';
import { useToast } from 'vue-toastification';
import router from '../../../router';
export default {
    setup() {
        const showPassword = ref(false);
        const password = ref('');
        const passwordError = ref(false);





        const togglePasswordVisibility = () => {
            showPassword.value = !showPassword.value;
        }

        let url = import.meta.env.VITE_APP_WS;
        const WS = ref(new WebSocket(url + 'student'));



        WS.value.onopen = (event) => {
            console.log("Connection opened", event);
        };
        onMounted(() => {
            console.log(`${import.meta.env.WS}student`);
        });
        const check = () => {
            let token = localStorage.getItem("token");

            let auth = {
                command: "AUTHENTICATE",
                detail: {
                    token: token,
                },
            };
            WS.value.send(JSON.stringify(auth));

            WS.value.onmessage = (event) => {
                let data = JSON.parse(event.data);
                if (data.message == "Authenticated") {
                    let join = {
                        command: "JOIN GROUP TEST",
                        detail: {
                            group_test_id: localStorage.getItem("group_test_id"),
                            password: password.value
                        }
                    }
                    WS.value.send(JSON.stringify(join));
                    WS.value.onmessage = (event) => {
                        let data = JSON.parse(event.data)
                        // console.log(localStorage.getItem("group_test_id"))
                        // console.log(data)
                        if (data.status == 403) {
                            useToast().error("Sai mật khẩu");
                        }

                        else if (data.status == 200) {
                            localStorage.setItem('pass', password.value)
                            let get_test = {
                                command: "GET TEST"
                            }

                            WS.value.send(JSON.stringify(get_test));
                            WS.value.onmessage = (event) => {
                                let data = JSON.parse(event.data);
                                console.log(data)
                                if (data.status == 200) {

                                    localStorage.setItem("test", JSON.stringify(data.message.student_test));
                                    let npage = localStorage.getItem('n_page');
                                    if (npage == data.message.student_test.length) {
                                        router.push('/test');
                                    }
                                    else {
                                        router.push('/nPageTest');
                                    }
                                }
                            }

                        }

                    }
                }
            };
        };

        return {
            showPassword,
            password,
            passwordError,
            WS,
            check,
            togglePasswordVisibility
        }
    }
}
</script>

<style>

</style>