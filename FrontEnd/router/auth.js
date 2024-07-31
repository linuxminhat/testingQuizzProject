const auth = [
  {
    path: "/",
    component: () => import("../layouts/authLayout.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../pages/auth/LoginPage.vue"),
    meta: {
      title: "Login",
      requiresAuth: false,
    },
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../pages/auth/RegisterPage.vue"),
    meta: {
      title: "Login",
      requiresAuth: false,
    },
  },
];

export default auth;
