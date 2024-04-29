import unittest
from datetime import datetime


from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.json')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        Prgoram crashes: Line 63 fails in quizzes_controller.py because it could not cat int type with string type
        """
        self.ctrl.add_quiz(1,"Quiz for Requirments",None,None)
        self.assertEquals(len(self.ctrl.get_quizzes),1,"Number of quizzes should be one")
        
    def test_expose_failure_02(self):
        """
        Implement this function and two more that
        execute the code and make it fail. 
        Program crashes: quizzes_controller.py line 94, in add_answer date object cannot be saved
        """
        time_now = datetime.now()
        quiz_1 = self.ctrl.add_quiz("Quiz 1",None,None,None)
        question_1 = self.ctrl.add_question(quiz_1,"Q-1","This is Sample question?")
        answer_1 = self.ctrl.add_answer(question_1,"Sample answer format.",time_now)

        self.assertIsNone(answer_1, 'Dates cannot be saved in bool type or JSON.')

    def test_expose_failure_03(self):
        # Clearing previous data
        self.ctrl.clear_data()

        quiz_id = self.ctrl.add_quiz("A", "B", 1, 1)
        # Triggering exception in Line 21 of data_loader.py
        self.ctrl.add_question(quiz_id, b"some binary string", "D")

if __name__ == '__main__':
    unittest.main()
