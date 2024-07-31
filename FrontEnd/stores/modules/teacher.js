import { defineStore } from "pinia";
import teacherService from "../../apis/modules/teacher.js";
import { useToast } from "vue-toastification";

export const useTeacherStore = defineStore("teacher", {
  state: () => ({
    tmpCollectionId: null,
    collections: [],
    collectionName: "",
    questionName: "",
    questionBank: [],
    questions: [],
    bankId: "",
    groupId: "",
    groupName: "",
    questionId: "",
    testInCollection: [],
    tmpTest: [],
    state: null,
  }),

  actions: {
    //collection

    async getCollections() {
      try {
        const response = await teacherService.getCollection();
        console.log(response.data);
        this.collections = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addCollection(name) {
      try {
        const response = await teacherService.addCollection(name);
        // console.log(response.data);
        this.collections = this.getCollections();
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addTest(test) {
      try {
        const response = await teacherService.addTest(test);
        useToast().success("Đã tạo đề thi");
        this.testInCollection = await this.getTests(this.tmpCollectionId);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getTests(collection_id) {
      try {
        const response = await teacherService.getTests(collection_id);
        // console.log(response.data);
        this.testInCollection = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },

    //question

    async getQuestionBank(collectionId) {
      try {
        const response = await teacherService.getQuestionBank(collectionId);
        // console.log(response.data);
        this.questionBank = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getQuestions(questionBankId) {
      try {
        const response = await teacherService.getQuestions(questionBankId);
        //console.log(response.data);
        this.questions = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addQuestionBank(bank) {
      try {
        const response = await teacherService.addQuestionBank(bank);
        this.questionBank = await this.getQuestionBank(this.tmpCollectionId);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addQuestion(questionBankId, question) {
      try {
        console.log(question);
        const response = await teacherService.addQuestion(
          questionBankId,
          question
        );
        useToast().success("Đã thêm câu hỏi");

        this.questions = await this.getQuestions(this.bankId);

        return response.data;
      } catch (error) {
        console.error(error);
        useToast().error("Thêm thất bại");
      }
    },
    async uploadFile(formData, questionId) {
      try {
        const response = await teacherService.uploadFile(formData, questionId);
        this.questions = await this.getQuestions(this.bankId);

        return response.data;
      } catch (error) {
        console.error(error);
        useToast().error("Tải ảnh lên thất bại!");
      }
    },

    //Groups

    async getStudents(groupId) {
      try {
        const response = await teacherService.getStudents(groupId);

        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getGroups() {
      try {
        const response = await teacherService.getGroups();
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getHiddenGroups() {
      try {
        const response = await teacherService.getHiddenGroups();
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addGroup(groupName) {
      try {
        const response = await teacherService.addGroup(groupName);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getRequests(group_id) {
      try {
        const response = await teacherService.getRequests(group_id);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addStudent(studentId, groupId) {
      try {
        const response = await teacherService.addStudent(studentId, groupId);
        this.getStudents(groupId);
        this.getRequests(groupId);
        useToast().success("Đã thêm học sinh");
        return response.data;
      } catch (error) {
        useToast().error("Thêm thất bại");
        console.error(error);
      }
    },
    async refuseStudent(studentId, groupId) {
      try {
        const response = await teacherService.refuseStudent(studentId, groupId);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getImageGroups() {
      try {
        const response = await teacherService.getImageGroups();
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async updateGroup(group) {
      try {
        const response = await teacherService.updateGroup(group);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getGroupTest(group_id) {
      try {
        const response = await teacherService.getHistory(group_id);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    //test
    async getTests(group_id) {
      try {
        const response = await teacherService.getTests(group_id);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addTestInGroup(data) {
      try {
        const response = await teacherService.addTestInGroup(data);

        useToast().success("Đã tạo bài kiểm tra");
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getGroupTests(group_id) {
      try {
        const response = await teacherService.getGroupTests(group_id);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getStudentPoints(group_test_id) {
      try {
        const response = await teacherService.getStudentPoints(group_test_id);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async updateGroupTest(group_tests) {
      try {
        const response = await teacherService.updateGroupTest(group_tests);

        useToast().success("Cập nhật thành công");
        console.log("cc", response);
        return response.data;
      } catch (error) {
        console.error(error);
        useToast().error("Cập nhật thất bại");
      }
    },

    async getStudentTest(group_test_id) {
      try {
        const response = await teacherService.getStudentTest(group_test_id);
        this.state = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },

    async getSumary(question_bank_id) {
      try {
        const response = await teacherService.getSumary(question_bank_id);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },

    //profile
    async getInfor() {
      try {
        const response = await teacherService.getInfor();

        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async updateAvatar(formData) {
      try {
        const response = await teacherService.updateAvatar(formData);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async updateInfor(data) {
      try {
        const response = await teacherService.updateInfor(data);
        useToast().success("Cập nhật thành công");
        return response.data;
      } catch (error) {
        console.error(error);
        useToast().error("Cập nhật thất bại");
      }
    },
  },
});
