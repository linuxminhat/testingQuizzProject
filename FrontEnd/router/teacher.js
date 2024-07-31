const teacher = [
  {
    path: "/teacher",
    name: "teacher",
    component: () => import("../layouts/teacherLayout.vue"),
    beforeEnter: (to, from, next) => {
      if (localStorage.getItem("role") == "teacher") {
        next();
      } else {
        next("/login");
      }
    },
    meta: {
      title: "WeightNPay-Admin",
    },
    children: [
      {
        path: "schedule",
        name: "teacher-schedule",
        component: () => import("../pages/teacher/schedule/index.vue"),
      },
      {
        path: "group",
        name: "teacher-group",
        component: () => import("../pages/teacher/group/index.vue"),
      },
      {
        path: "group/:id",
        name: "teacher-group-detail",
        component: () => import("../pages/teacher/group/GroupDetail.vue"),
      },
      {
        path: "group/:groupId/groupTestId/:testId",
        name: "teacher-group-test",
        component: () => import("../pages/teacher/group/GroupTest.vue"),
      },
      {
        path: "quizes",
        name: "teacher-quizes",
        component: () => import("../pages/teacher/quizzes/index.vue"),
      },
      {
        path: "question-bank/:id",
        name: "teacher-question-bank",
        component: () => import("../pages/teacher/quizzes/questionBank.vue"),
      },
      {
        path: "edit-bank/:id",
        name: "teacher-edit-bank",
        component: () => import("../pages/teacher/quizzes/editBank.vue"),
      },

      {
        path: "profile",
        name: "teacher-profile",
        component: () => import("../pages/teacher/profile/index.vue"),
      },
      {
        path: "testhistory",
        name: "testHistory",
        component: () => import("../pages/teacher/group/TestHistory.vue"),
      },
    ],
  },
];
export default teacher;
