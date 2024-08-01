from datetime import datetime

from Backend.Business.BO_group_test import BO_group_test
from Backend.DataAccess.DAO_group_test import DAO_group_test
from Backend.Model.DB_model import StudentTest, StudentWork_Question
from Backend.DataAccess.DAO_student_test import DAO_student_test
from Backend.Model.request_model import Req_StudentWork
from Backend.Model.response_model import Res_StudentTest


class BO_student_test:
    def __init__(self):
        self._dao_student_test = None
        self._dao_group_test = None
        self._bo_group_test = None

    @property
    def dao_student_test(self):
        if not self._dao_student_test:
            self._dao_student_test = DAO_student_test()
        return self._dao_student_test

    @property
    def dao_group_test(self):
        if not self._dao_group_test:
            self._dao_group_test = DAO_group_test()
        return self._dao_group_test

    @property
    def bo_group_test(self):
        if not self._bo_group_test:
            self._bo_group_test = BO_group_test()
        return self._bo_group_test

    def get_student_test(self, group_test_id: str, student_id: str) -> StudentTest:
        return self.dao_student_test.get_student_test(group_test_id, student_id)

    # def get_group_test_in_time(self, student_id: str, start: datetime, end: datetime):
    #     return self.dao_group_test.get_group_test_for_student(student_id, start, end)

    def get_history(self, student_id: str, group_id: str) -> list[StudentTest]:
        return self.dao_student_test.get_student_test_history(student_id, group_id)

    # INSERT
    # def insert_student_test(self, student_id: str, group_test_id: str) -> StudentTest:
    #     student_work = self.bo_group_test.generate_student_work(group_test_id)
    #     student_test = StudentTest(student_id=student_id, group_test_id=group_test_id, student_work=student_work)
    #     self.dao_student_test.insert_student_test(student_test)
    #     return student_test

    def insert_student_test(self, student_test):
        return self.dao_student_test.insert_student_test(student_test)

    # def get_student_work(self, student_id: str, group_test_id: str):
    #     return self.dao_student_test.get_student_work(student_id, group_test_id)

    # UPDATE
    def update_violate(self, group_test_id, student_id, violate):
        self.dao_student_test.update_violate(group_test_id, student_id, violate)

    def submit(self, student_test: StudentTest):
        # student_test = self.dao_student_test.get_student_test(group_test_id, student_id)
        #
        # if student_test is None:
        #     raise Exception("Student test does not exist")
        # if student_test.end is not None:
        #     raise Exception("Student test has already been submitted")
        #
        # assert len(student_test.student_work) == len(student_answer)
        #
        # for index, answer in enumerate(student_answer):  # assign student answer to student work
        #     student_test.student_work[index].student_answer = answer

        student_test.end = datetime.now()
        student_test.score = self.calculate_point(student_test.student_work)
        self.dao_student_test.submit(student_test)

    def calculate_point(self, student_work: list[StudentWork_Question]) -> float:
        total_score = .0
        for sw_question in student_work:  # calculate score for each question
            if sw_question.student_answer is None:
                continue

            correct_student_ans = set(sw_question.student_answer) & sw_question.answer.correct  # set of correct student answers = set of student answers & set of correct answers
            question_score = len(correct_student_ans) / len(sw_question.answer.correct)  # question score = number of correct student answers / number of correct answers
            if len(sw_question.answer.correct) != 1 and question_score != 0:  # if question has multiple correct answers
                wrong_ans_count = len(sw_question.student_answer) - len(correct_student_ans)  # number of wrong answers = number of student answers - number of correct student answers
                question_score *= (1 - wrong_ans_count / (len(sw_question.answer.text) - len(sw_question.answer.correct)))  # question score *= 1 - number of wrong answers / number of wrong answers

            total_score += question_score

        return total_score / len(student_work)
