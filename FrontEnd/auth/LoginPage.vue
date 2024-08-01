//comment
<template>
  <div class="w-screen">
    <Header class="fixed z-50 bg-white" />
    <h1 class="mt-24 mx-24 text-4xl font-bold">Đăng nhập để bắt đầu</h1>
    <div class="grid grid-cols-2 gap-4 m-10 mt-20 ml-24 h-full w-full">
      <div class="img w-2/3 ml-24 rounded-md shadow-lg">
        <img src="/src/assets/img/Exams-bro.png" alt="" />
      </div>

      <form
        class="p-6 bg-white rounded shadow-md w-1/2"
        @submit.prevent="validateForm"
      >
        <h2 class="text-3xl font-bold text-center my-16">Đăng nhập</h2>

        <div class="mb-4">
          <div class="mt-2 flex flex-wrap space-x-6">
            <div>
              <label class="inline-flex items-center">
                <input
                  type="radio"
                  class="form-radio text-blue-600 h-4 w-4"
                  name="role"
                  value="teacher"
                  v-model="role"
                />
                <span class="ml-2 text-gray-700">Giáo viên</span>
              </label>
            </div>
            <div>
              <label class="inline-flex items-center">
                <input
                  type="radio"
                  class="form-radio text-blue-600 h-4 w-4"
                  name="role"
                  value="student"
                  v-model="role"
                />
                <span class="ml-2 text-gray-700">Học Sinh</span>
              </label>
            </div>
          </div>
          <p class="text-red-500" v-if="roleError">{{ roleError }}</p>
        </div>

        <div class="mb-4">
          <input
            type="email"
            v-model="email"
            @blur="validateEmail"
            autocomplete="email"
            :class="`w-full px-3 py-2 border rounded-md focus:outline-none ${
              emailError
                ? 'border-red-500'
                : 'border-gray-300 focus:border-blue-500'
            }`"
            placeholder="Email"
          />
          <p v-if="emailError" class="text-red-500 text-sm p-1">
            {{ emailError }}
          </p>
        </div>
        <div class="mb-4 relative">
          <input
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            @blur="validatePassword"
            autocomplete="current-password"
            :class="`w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500focus:outline-none ${
              passwordError
                ? 'border-red-500'
                : 'border-gray-300 focus:border-blue-500'
            }`"
            placeholder="Mật khẩu"
          />
          <button
            type="button"
            v-if="!passwordError"
            class="absolute inset-y-0 right-0 pr-3 pb-1 flex items-center"
            @click="togglePasswordVisibility"
          >
            <img
              v-if="showPassword"
              src="/src/assets/icon/show.png"
              alt=""
              class="h-6 w-6"
            />
            <img
              v-else
              src="/src/assets/icon/hide.png"
              alt=""
              class="h-6 w-6"
            />
          </button>

          <p v-if="passwordError" class="text-red-500 text-sm p-1">
            {{ passwordError }}
          </p>
        </div>
        <p
          class="text-right text-blue-500 hover:text-blue-700 cursor-pointer pb-2"
        >
          Quên mật khẩu?
        </p>
        <button
          class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-500 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        >
          Đăng nhập
        </button>
        <p class="mt-4 text-center">
          Bạn chưa có tài khoản?
          <a href="/register" class="text-blue-500 hover:text-blue-700"
            >Đăng ký</a
          >
        </p>
      </form>
    </div>
  </div>
  <a-spin :spinning="loading"></a-spin>
  <router-view />
</template>

<script>
import { ref } from "vue";
import Header from "../../components/header/Header.vue";
import { useAuthStore } from "../../stores/modules/auth.js";
import { Spin } from "ant-design-vue";
export default {
  components: {
    Header,
    "a-spin": Spin,
  },
  setup() {
    const email = ref("");
    const password = ref("");
    const emailError = ref("");
    const passwordError = ref("");
    const role = ref("teacher");
    const showPassword = ref(false);

    const loading = ref(false);
    const roleError = ref("");

    const validateRole = () => {
      if (role.value === "") {
        roleError.value = "Vui lòng chọn vai trò.";
      } else {
        roleError.value = "";
      }
    };
    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value;
    };
    const validateEmail = () => {
      if (email.value === "") {
        emailError.value = "Vui lòng nhập email.";
      } else if (!/\S+@\S+\.\S+/.test(email.value)) {
        emailError.value = "Định dạng email không hợp lệ.";
      } else {
        emailError.value = "";
      }
    };

    const validatePassword = () => {
      if (password.value === "") {
        passwordError.value = "Vui lòng nhập mật khẩu.";
      } else if (password.value.length < 6) {
        passwordError.value = "Mật khẩu phải có ít nhất 6 ký tự.";
      } else {
        passwordError.value = "";
      }
    };

    const validateForm = () => {
      validateRole();
      validateEmail();
      validatePassword();
      if (emailError.value || passwordError.value) {
        return;
      }

      submitForm();
    };

    const submitForm = async () => {
      loading.value = true;

      const data = {
        username: email.value,
        password: password.value,
        role: role.value,
      };
      const authStore = useAuthStore();

      await authStore.login(data);

      loading.value = false;
    };
    return {
      role,
      email,
      password,
      emailError,
      passwordError,
      showPassword,
      roleError,
      validateRole,
      togglePasswordVisibility,
      validateEmail,
      validatePassword,
      validateForm,
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
