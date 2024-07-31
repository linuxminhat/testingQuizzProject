import { defineStore } from "pinia";
import studentService from "../../apis/modules/student.js";

export const useStudentStore = defineStore("student", {
  state: () => ({
    group_test_id: "",
    duration: 0,
    score: 0,
    violations: 0,
  }),

  actions: {
    //group
    async getGroups() {
      try {
        const response = await studentService.getGroups();
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async joinGroup(group_id) {
      try {
        const response = await studentService.joinGroup(group_id);
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getStudentsInGroup(group_id) {
      try {
        const response = await studentService.getStudentsInGroup(group_id);
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getGroupTests(group_id) {
      try {
        const response = await studentService.getGroupTests(group_id);
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getHistory(group_id) {
      try {
        const response = await studentService.getHistory(group_id);
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    //profile
    async getInfor() {
      try {
        const response = await studentService.getInfor();
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async updateAvatar(formData) {
      try {
        const response = await studentService.updateAvatar(formData);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },

    //Test
    async getTest(group_test_id) {
      try {
        const response = await studentService.getTest(group_test_id);
        // console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async testSubmit(data) {
      try {
        const response = await studentService.testSubmit(data);
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },

    //Schedule

    async getSchedule() {
      try {
        const response = await studentService.getSchedule();
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
