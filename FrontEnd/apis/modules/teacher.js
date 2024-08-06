import Api from "../../apis";

export default {
  //Collection
  getCollection() {
    return Api().get("teacher/collection/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  addCollection(name) {
    return Api().post("teacher/collection/", name, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  addTest(test) {
    return Api().post("teacher/collection/test/", test, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getTests(collection_id) {
    return Api().get(
      `teacher/collection/test/?collection_id=${collection_id}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },
  //question
  addQuestionBank(bank) {
    return Api().post("teacher/collection/question_bank/", bank, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  addQuestion(questionBankId, question) {
    return Api().post(
      `teacher/collection/question_bank/question/?question_bank_id=${questionBankId}`,
      question,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },
  uploadFile(formData, questionId) {
    return Api().post(
      `teacher/collection/question_bank/question/attachment?question_id=${questionId}`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  getQuestionBank(collectionId) {
    return Api().get(
      `teacher/collection/question_bank/?collection_id=${collectionId}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },
  getQuestions(questionBankId) {
    return Api().get(
      `teacher/collection/question_bank/question/?question_bank_id=${questionBankId}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  //groups

  getStudents(groupId) {
    return Api().get(`teacher/group/student?group_id=${groupId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getGroups() {
    return Api().get(`teacher/group/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getHiddenGroups() {
    return Api().get(`teacher/group/?is_show=0`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  addGroup(groupName) {
    return Api().post(`teacher/group/`, groupName, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getRequests(group_id) {
    return Api().get(
      `teacher/group/student?group_id=${group_id}&is_join=false`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  addStudent(studentId, groupId) {
    return Api().post(`teacher/group/student?group_id=${groupId}`, studentId, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  refuseStudent(studentId, groupId) {
    return Api().delete(
      `teacher/group/student?group_id=${groupId}`,
      studentId,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },
  getImageGroups() {
    return Api().get(`teacher/group/static_images`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  updateGroup(group) {
    return Api().patch(`teacher/group/update`, group, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  //test
  getGroupTests(group_id) {
    return Api().get(`teacher/grouptest/?group_id=${group_id}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  addTestInGroup(data) {
    return Api().post(`teacher/grouptest/`, data, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getStudentPoints(group_test_id) {
    return Api().get(
      `teacher/grouptest/studentpoint?group_test_id=${group_test_id}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  updateGroupTest(group_tests) {
    return Api().put(`teacher/grouptest/`, group_tests, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getStudentTest(group_test_id) {
    return Api().get(
      `teacher/grouptest/student_test?group_test_id=${group_test_id}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  getSumary(question_bank_id) {
    return Api().get(
      `teacher/collection/question_bank/question/summary?question_bank_id=${question_bank_id}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  //profile
  getInfor() {
    return Api().get(`teacher/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  updateAvatar(formData) {
    return Api().put(`teacher/avatar`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  updateProfile(data) {
    return Api().put(`teacher/information`, data, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
};
