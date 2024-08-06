import Api from "../../apis";

export default {
  //group
  getGroups() {
    return Api().get("student/group/?join=1&just_id=0", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  joinGroup(group_id) {
    return Api().post(
      `student/group?group_id=${group_id}`,

      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  getStudentsInGroup(group_id) {
    return Api().get(`student/group/students/?group_id=${group_id}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getGroupTests(group_id) {
    return Api().get(`student/grouptest/?group_id=${group_id}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getHistory(group_id) {
    return Api().get(`/student/grouptest/history?group_id=${group_id}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  //profile
  getInfor() {
    return Api().get("student/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  updateAvatar(formData) {
    return Api().put(`student/avatar`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  //Test
  getTest(group_test_id) {
    return Api().get(
      `student/grouptest/studentwork?group_test_id=${group_test_id}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },
  testSubmit(data) {
    return Api().post("student/grouptest/studentwork/submit", data, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  //Schedule

  getSchedule() {
    return Api().get(
      "student/grouptest/calendar?start=2024-05-20T09:00:00&end=2024-06-25T09:00:00",
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },
};
