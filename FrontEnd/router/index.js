import { createRouter, createWebHistory } from "vue-router";
import auth from "./auth.js";
import student from "./student.js";
import teacher from "./teacher.js";

const routes = [...auth, ...student, ...teacher];

const router = createRouter({
  history: createWebHistory(),

  routes,
});

export default router;
