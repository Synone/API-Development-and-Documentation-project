import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
database_test_name = os.getenv('DATABASE_TEST_NAME','trivia_test')
db_user = os.getenv('DATABASE_USER','postgres')
db_password = os.getenv('DATABASE_PASSWORD','0000')
db_host =os.getenv('DATABASE_HOST','localhost:5432')
class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = database_test_name
        self.database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(db_user,db_password,db_host, self.database_name)
        setup_db(self.app, self.database_path)
        self.new_question = {"question":"How are you today?", "answer":"I am okay", "category":"1","difficulty":1}
        self.fail_question = {"question":"How are you today?", "answer":"I am okay", "category":2,"difficulty":"kjkj"}
        self.search_string_404 = {'searchTerm':'somethingnotexist'}
        self.search_string = {'searchTerm':'how'}
        self.quiz = {"previous_questions":[],"quiz_category":{"type":"Science","id":'1'}}
        self.quiz_fail = {"previous_questions":[],"quiz_category":{"type":"Science","id":1}}
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_retrieve_all_question(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['categories'])
        

    def test_create_new_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data["success"],True)
        self.assertTrue(data["created"])
        self.assertTrue(len(data["questions"]))

    def test_404_create_can_not_process(self):
        res = self.client().post("/questions", json=self.fail_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"],False)
        self.assertEqual(data["message"],"One of the entity is not appropriate")

    def test_play_quiz(self):
        res = self.client().post('/quizzes',json=self.quiz)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_play_quiz_fail(self):
        res = self.client().post('/quizzes',json=self.quiz_fail)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],"Something went wrong in the server")

    def test_search_questions(self):
        res = self.client().post('/questions/search', json=self.search_string)
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        
    def test_retrieve_questions_based_on_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data["success"],True)
        self.assertTrue(len(data['questions']))

    def test_delete_question(self):
        res = self.client().delete("/questions/3")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["message"], "Delete successfully")

    def test_retrieve_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"]) 

    def test_422_delete_question(self):
        res = self.client().delete("/questions/313")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()