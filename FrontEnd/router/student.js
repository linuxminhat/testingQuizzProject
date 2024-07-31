const student = [
  {
    path: "/student",
    name: "student",
    component: () => import("../layouts/studentLayout.vue"),
    beforeEnter: (_to, _from, next) => {
      if (localStorage.getItem("role") == "student") {
        next();
      } else {
        next("/login");
      }
    },
    meta: {
      title: "StudentPage",
    },
    children: [
      {
        path: "schedule",
        name: "student - schedule",
        component: () => import("../pages/student/schedule/index.vue"),
        meta: {
          title: "Student - Schedule",
        },
      },
      {
        path: "group",
        name: "student - group",
        component: () => import("../pages/student/group/index.vue"),
      },
      {
        path: "group/:id",
        name: "student-group-detail",
        component: () => import("../pages/student/group/GroupDetail.vue"),
      },
      {
        path: "notif",
        name: "student - notif",
        component: () => import("../pages/student/notif/index.vue"),
      },
      {
        path: "profile",
        name: "student - profile",
        component: () => import("../pages/student/profile/index.vue"),
      },

      // {
      //   path: "profile/change-password",
      //   name: "student - profile - change-password",
      //   component: () => import("../pages/student/profile/ChangePassword.vue"),
      // },
    ],
  },
  {
    path: "/auth",
    name: "student-auth",
    component: () => import("../pages/student/test/password.vue"),
  },
  {
    path: "/test",
    name: "student-test",
    component: () => import("../pages/student/test/Test.vue"),
  },
  {
    path: "/nPagetest",
    name: "student-nPagetest",
    component: () => import("../pages/student/test/nPageTest.vue"),
  },

  {
    path: "/point",
    name: "student-point",
    component: () => import("../pages/student/test/Point.vue"),
  },
];

export default student;
