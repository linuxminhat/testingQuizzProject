//fix registerPage
<template>
    <Header />


    <div class="regis p-20 pl-24 h-full">
        <div class="grid grid-cols-2">

            <div class="img w-2/3 bg-white m-28 shadow-md">
                <img src="/src/assets/img/register.png" alt="" />
            </div>
            <form class="form my-28 mx-12 bg-white shadow-md p-12 w-2/3" @submit.prevent="validateForm">
                <h2 class="text-3xl font-bold text-center mb-12">Đăng ký tài khoản</h2>

                <div class="mb-4">
                    <input type="text" v-model="name" @blur="validateName" :class="`w-full px-3 py-2 border rounded-md focus:outline-none ${
              nameError
                ? 'border-red-500'
                : 'border-gray-300 focus:border-blue-500'
            }`" placeholder="Họ và tên" />
                    <p v-if="nameError" class="text-red-500 text-sm p-1">
                        {{ nameError }}
                    </p>
                </div>
                <!-- <div class="mb-4">
                <input type="text" v-model="phone" @blur="validatePhone" :class="`w-full px-3 py-2 border rounded-md focus:outline-none ${
            phoneError
              ? 'border-red-500'
              : 'border-gray-300 focus:border-blue-500'
          }`" placeholder="Điện thoại" />
                <p v-if="phoneError" class="text-red-500 text-sm p-1">
                    {{ phoneError }}
                </p>
            </div> -->
                <div class="mb-4">
                    <input type="email" v-model="email" autocomplete="email" @blur="validateEmail" :class="`w-full px-3 py-2 border rounded-md focus:outline-none ${
              emailError
                ? 'border-red-500'
                : 'border-gray-300 focus:border-blue-500'
            }`" placeholder="Email" />
                    <p v-if="emailError" class="text-red-500 text-sm p-1">
                        {{ emailError }}
                    </p>
                </div>

                <div class="mb-4">
                    <div class="mt-2 flex flex-wrap space-x-6">
                        <div>
                            <label class="inline-flex items-center">
                                <input type="radio" class="form-radio text-blue-600 h-4 w-4" name="role" value="teacher"
                                    v-model="role" />
                                <span class="ml-2 text-gray-700">Giáo viên</span>
                            </label>
                        </div>
                        <div>
                            <label class="inline-flex items-center">
                                <input type="radio" class="form-radio text-blue-600 h-4 w-4" name="role" value="student"
                                    v-model="role" />
                                <span class="ml-2 text-gray-700">Học Sinh</span>
                            </label>
                        </div>
                    </div>
                </div>

                <div class="mb-4 relative">
                    <input :type="showPassword ? 'text' : 'password'" v-model="password" @blur="validatePassword"
                        autocomplete="current-password" :class="`w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500focus:outline-none ${
              passwordError
                ? 'border-red-500'
                : 'border-gray-300 focus:border-blue-500'
            }`" placeholder="Mật khẩu" />
                    <button v-if="!passwordError" class="absolute inset-y-0 right-0 pr-3 pb-1 flex items-center"
                        @click.prevent="togglePasswordVisibility">
                        <img v-if="showPassword" src="/src/assets/icon/show.png" alt="" class="h-6 w-6" />
                        <img v-else src="/src/assets/icon/hide.png" alt="" class="h-6 w-6" />
                    </button>

                    <p v-if="passwordError" class="text-red-500 text-sm p-1">
                        {{ passwordError }}
                    </p>
                </div>
                <button
                    class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-500 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                    Đăng ký
                </button>
                <p class="mt-4 text-center">
                    Đã có tài khoản?
                    <a href="/login" class="text-blue-500 hover:text-blue-700">Đăng Nhập</a>
                </p>
            </form>
        </div>
    </div>
    <router-view />
</template>

<script>
import { ref } from "vue";
import Header from "../../components/header/Header.vue";
import { useAuthStore } from '../../stores/modules/auth';
export default {
    components: { Header },
    setup() {
        const name = ref("");
        const phone = ref("");
        const email = ref("");
        const password = ref("");
        const nameError = ref("");
        const phoneError = ref("");
        const emailError = ref("");
        const role = ref("teacher");
        const passwordError = ref("");
        const showPassword = ref(false);

        const togglePasswordVisibility = () => {
            showPassword.value = !showPassword.value;
        }
        const validateForm = () => {
            validateEmail();
            validatePassword();
            validateName();
            validatePhone();
            if (
                emailError.value ||
                passwordError.value ||
                nameError.value ||
                phoneError.value
            ) {
                return;
            }
            submitForm();
        };

        const validateName = () => {
            nameError.value = name.value === "" ? "Vui lòng nhập họ và tên." : "";
        };

        const validatePhone = () => {
            phoneError.value =
                phone.value === ""
                    ? "Vui lòng nhập số điện thoại."
                    : !/((09|03|07|08|05)+([0-9]{8})\b)/g.test(phone.value)
                        ? "Số điện thoại không hợp lệ."
                        : "";
        };

        const validateEmail = () => {
            emailError.value =
                email.value === ""
                    ? "Vui lòng nhập email."
                    : !/\S+@\S+\.\S+/.test(email.value)
                        ? "Định dạng email không hợp lệ."
                        : "";
        };

        const validatePassword = () => {
            passwordError.value =
                password.value === ""
                    ? "Vui lòng nhập mật khẩu."
                    : password.value.length < 6
                        ? "Mật khẩu phải có ít nhất 6 ký tự."
                        : "";
        };

        const submitForm = () => {
            const data = {
                name: name.value,
                email: email.value,
                password: password.value,
                role: role.value,
            };
            console.log(data)
            useAuthStore().signUp(data)

        };
        return {
            name,
            phone,
            email,
            password,
            nameError,
            phoneError,
            emailError,
            passwordError,
            showPassword,
            togglePasswordVisibility,
            validateForm,
            validateName,
            validatePhone,
            validateEmail,
            validatePassword,
            submitForm,
        };
    },
};
</script>

<style>
.w-screen {
  overflow-x: hidden;
}
</style>
