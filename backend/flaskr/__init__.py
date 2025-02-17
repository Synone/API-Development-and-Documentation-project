import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginate_questions(request, selection):    


    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    _questions = [ques.format() for ques in selection]
    current_questions = _questions[start:end]
    return current_questions
def create_app(test_config=None):


    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        
        return response
    """
@TODO: 
Create an endpoint to handle GET requests
for all available categories.
    """
    @app.route('/categories', methods=['GET'])
    def retrieve_categories():
        categos = Category.query.order_by(Category.id).all()
        if len(categos)==0:
            abort(404)
        return jsonify({
            "success":True,
            "categories":[catego.format() for catego in categos ],
        }),200
    """
    @TODO: 
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.
    
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """ 
    @app.route('/questions')
    def retrieve_questions():
        questions = Question.query.order_by(Question.id).all()
        categories  = Category.query.all() 
        current_questions = paginate_questions(request, questions)
        print(len(Question.query.all()))
        if len(questions)==0:
            abort(404)
        print([cate.format() for cate in categories ])
        return jsonify(
            {
                "success":True,
                "questions":current_questions,
                "total_questions": len(Question.query.all()),
                "categories": [cate.format() for cate in categories ]
            }
        )
    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.
    
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(422)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                    "questions": current_questions,
                    "total_books": len(Question.query.all()),
                    "message": 'Delete successfully'
                }
            ),200
        except:
            abort(422)
    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
    
    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=['POST'])
    @cross_origin()
    def create_question():
        body = request.get_json()
        new_question = body.get("question")
        new_category = body.get("category")
        new_difficulty = body.get('difficulty')
        new_answer = body.get('answer')
        try:
            ques = Question(question=new_question, answer=new_answer, category=new_category, difficulty=int(new_difficulty))
            ques.insert()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                "success":True,
                "created": ques.id,
                "questions":current_questions,
                "total_questions": len(selection)
            }),201
        except:
            return jsonify({
                "success":False,
                "message":"One of the entity is not appropriate"
            }),404
    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        body = request.get_json()
        search_term = body['searchTerm']
        try:
            questions = []
            if search_term != "":
                questions = Question.query.filter(Question.question.ilike(f"%{search_term}%")).all()
                if questions is None:
                    abort(404)
            return jsonify({
                "success":True,
                "questions": [ques.format() for ques in questions],
                "totalQuestions": len(questions)
                }),200
        except:
            abort(404)
    """
    @TODO:
    Create a GET endpoint to get questions based on category.
    
    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:category_id>/questions')
    def retrieve_questions_by_category(category_id):
        try:
            questions = Question.query.filter_by(category=str(category_id)).all()
            if len(questions) != 0:
                return jsonify({
                    "success":True,
                    "questions": [ques.format() for ques in questions],
                    "total_questions": len(questions),
                    "current_category": category_id
                })
            else:
                return jsonify({
                    "success":True,
                    "questions": [],
                    "total_questions": 0,
                    "current_category": category_id
                })
        except:
            abort(404)
    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def retrieve_quizzes():
        body = request.get_json()
        store_questions = body.get('previous_questions')
        category = body.get('quiz_category')
        try:
            if category['id'] !=0:
                questions = Question.query.filter_by(category=category['id']).all()
                questions_list = [ques.format() for ques in questions]
                fresh_questions = [item for item in questions_list if int(item['id']) not in store_questions]
                if len(fresh_questions)==0:
                    return jsonify({
                        "message":'End of quiz',
                        "success": True,
                        "question": None
                    }),200
                random_num = random.randint(0,len(fresh_questions)-1)
                random_question = fresh_questions[random_num]
                return jsonify({
                    "success":True,
                    "question":random_question
                }),200
            else:
                questions = Question.query.order_by(Question.id).all()
                questions_list = [ques.format() for ques in questions]
                fresh_questions = [item for item in questions_list if int(item['id']) not in store_questions]
                if len(fresh_questions)==0:
                    return jsonify({
                        "message":"No questions exists",
                        "success":True,
                        "question":None
                    }),200
                random_num = random.randint(0,len(fresh_questions)-1)
                random_question = fresh_questions[random_num]
                return jsonify({
                    "success":True,
                    "question":random_question
                }),200
        except:
            return jsonify({
                "success":False,
                "question": None,
                "message": "Something went wrong in the server"
            }),500
        
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({
                "success":False,
                "error":404,
                "message":"resource not found"
            }),
            404
        )
    @app.errorhandler(422)
    def unprocessable_request(error):
        return (
            jsonify({"success": False, "error": 422, "message": "Unprocessable"}),422
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "Bad request"}), 400

    @app.errorhandler(405)
    def not_alowwed_method(error):
        return (
            jsonify({"success": False, "error": 405, "message": "Method not allowed"}),
            405
        )
    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify({
                "success": False, "error":500, "message":"Internal server error"
            }),500
        )
    return app

