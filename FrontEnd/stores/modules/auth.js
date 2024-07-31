import { defineStore } from "pinia";
import AuthService from "../../apis/modules/auth.js";
import router from "../../router";
import { useToast } from "vue-toastification";
export const useAuthStore = defineStore("auth", {
  state: () => ({
    role: null,
    isLoggedIn: false,
    token: null,
  }),

  actions: {
    async login(data) {
      try {
        if (data.role === "teacher") {
          const teacher = {
            username: data.username,
            password: data.password,
          };
          const response = await AuthService.loginTeacher(teacher);
          if (response && response.data.access_token) {
            this.token = response.data.access_token;
            localStorage.setItem("token", this.token);
            localStorage.setItem("role", data.role);

            this.isLoggedIn = true;
            useToast().success("Đăng nhập thành công");
            router.push({ name: "teacher-schedule" });
          }
        }
        if (data.role === "student") {
          const student = {
            username: data.username,
            password: data.password,
          };
          const response = await AuthService.loginStudent(student);
          if (response && response.data.access_token) {
            this.token = response.data.access_token;
            localStorage.setItem("token", this.token);
            localStorage.setItem("role", data.role);
            console.log(localStorage.getItem("role"));
            this.isLoggedIn = true;
            useToast().success("Đăng nhập thành công");
            router.push({ name: "student - schedule" });
          }
        }
      } catch (error) {
        if (error.response.data.detail == "Incorrect username or password") {
          useToast().error("Email hoặc mật khẩu không đúng!");
        }
      }
    },
    async logout() {
      this.isLoggedIn = false;
      this.token = null;
      localStorage.removeItem("token");
      localStorage.removeItem("role");
      //router.push({ name: "login" });
    },
    async signUp(data) {
      try {
        if (data.role === "teacher") {
          const teacher = {
            email: data.email,
            password: data.password,
            name: data.name,
          };
          const response = await AuthService.signUpTeacher(teacher);
          console.log(response);
          useToast().success("Đăng ký thành công");
          router.push({ name: "login" });
        }
        if (data.role === "student") {
          const student = {
            username: data.username,
            password: data.password,
            role: data.role,
          };
          const response = await AuthService.signUpStudent(student);
          console.log(response);
          useToast().success("Đăng ký thành công");
          router.push({ name: "login" });
        }
      } catch (error) {
        if (error.response.data.detail == "Username already exists") {
          useToast().error("Email đã tồn tại!");
        }
      }
    },
  },
});
