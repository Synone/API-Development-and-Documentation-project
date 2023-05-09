# Frontend - Trivia API

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend) so it will not load successfully if the backend is not working or not connected. We recommend that you **stand up the backend first**, test using Postman or curl, update the endpoints in the frontend, and then the frontend should integrate smoothly.

### Installing Dependencies

1. **Installing Node and NPM**
   This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

2. **Installing project dependencies**
   This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _tip_: `npm i`is shorthand for `npm install``

## Required Tasks

### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

### Running Backend server

In order to run the backend, change directory to 'backend' dir, run command: `.\myenv\Scripts\activate` to activate virtual environment.
In order to start the backend,in the command: `set FLASK_APP=flaskr` and `set FLASK_DEBUG=1`,THEN run command: `python -m flask run`
The backend will run on : [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Request Formatting

The frontend should be fairly straightforward and disgestible. You'll primarily work within the `components` folder in order to understand, and if you so choose edit, the endpoints utilized by the components. While working on your backend request handling and response formatting, you can reference the frontend to view how it parses the responses.

After you complete your endpoints, ensure you return to the frontend to confirm your API handles requests and responses appropriately:

- Endpoints defined as expected by the frontend
- Response body provided as expected by the frontend

### Optional: Updating Endpoints and API behavior

Would you rather the API had different behavior - different endpoints, return the response body in a different format? Go for it! Make the updates to your API and the corresponding updates to the frontend so it works with your API seamlessly.

### Optional: Styling

In addition, you may want to customize and style the frontend by editing the CSS in the `stylesheets` folder.

### Optional: Game Play Mechanics

Currently, when a user plays the game they play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category.

You can optionally update this game play to increase the number of questions or whatever other game mechanics you decide. Make sure to specify the new mechanics of the game in the README of the repo you submit so the reviewers are aware that the behavior is correct.

> **Spoiler Alert:** If needed, there are details below regarding the expected endpoints and behavior. But, ONLY look at them if necessary. Give yourself the opportunity to practice understanding code first!

---

---

## API Reference

### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

### Running Backend server

The backend uses techs in requirements.txt file, create virtual environment using `python -m venv path/your_env_name` and type in CMD `.\your_env\Scripts\activate` to activate the virtual environtment, install all packages running `pip install -r requirements.txt`

In order to run the backend, change directory to 'backend' dir, run command: `.\myenv\Scripts\activate` to activate virtual environment.
In order to start the backend,in the command: `set FLASK_APP=flaskr` and `set FLASK_DEBUG=1`,THEN run command: `python -m flask run`
The backend will run on : [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "Bad request"
}
```

The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 500: Internal Server Error

## DO NOT PROCEED: ENDPOINT SPOILERS

> Only read the below to confirm your notes regarding the expected API endpoint behavior based on reading the frontend codebase.

### Expected endpoints and behaviors

`GET '/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.

```json
{
  "categories": [
    { "id": 1, "type": "Science" },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "success": true
}
```

---

`GET '/questions?page=${integer}'`

- Fetches a paginated set of questions, a total number of questions, all categories and current category string.
- Request Arguments: `page` - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string

```json
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "currentCategory": 1,
  "questions": [
    {
      "answer": "Agra",
      "category": "2",
      "difficulty": 3,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "1",
      "difficulty": 2,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": "3",
      "difficulty": 2,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": "4",
      "difficulty": 2,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": "2",
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": "4",
      "difficulty": 1,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": "3",
      "difficulty": 1,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": "4",
      "difficulty": 1,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": "4",
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "8 bilions",
      "category": "3",
      "difficulty": 4,
      "id": 24,
      "question": "How many people are there on earth?"
    }
  ],
  "success": true,
  "total_questions": 22
}
```

---

`GET '/categories/${id}/questions'`

- Fetches questions for a cateogry specified by id request argument
- Request Arguments: `id` - integer
- Returns: An object with questions for the specified category, total questions, and current category string

```json
{
  "current_category": 2,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": "2",
      "difficulty": 4,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "George Washington Carver",
      "category": "2",
      "difficulty": 4,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": "2",
      "difficulty": 3,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": "2",
      "difficulty": 3,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Jackson Pollock",
      "category": "2",
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 5
}
```

---

`DELETE '/questions/${id}'`

- Deletes a specified question using the id of the question
- Request Arguments: `id` - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code. Optionally can return the id of the question. If you are able to modify the frontend, you can have it remove the question using the id instead of refetching the questions.

---

`POST '/quizzes'`

- Sends a post request in order to get the next question
- Request Body:

```json
{
    'previous_questions': [1, 4, 20, 15]
    quiz_category': 'current category'
 }
```

- Returns: a single new question object

```json
{
  "question": {
    "id": 1,
    "question": "This is a question",
    "answer": "This is an answer",
    "difficulty": 5,
    "category": 4
  }
}
```

---

`POST '/questions'`

- Sends a post request in order to add a new question
- Request Body:

```javascript
  {url: 'http://localhost:5000/questions', //TODO: update request URL
      type: 'POST',
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        question: new_question,
        answer: the_anwser,
        difficulty: the_difficulty,
        category: the_category,
      }),
      xhrFields: {
        withCredentials: false,
      },
      crossDomain: true}
```

```json
{
  "question": "Heres a new question string",
  "answer": "Heres a new answer string",
  "difficulty": 1,
  "category": 3
}
```

- Returns: Does not return any new data

```json
{
    "success":True,
    "created": ques.id,
    "questions":current_questions,
    "total_questions": len(selection)
}
```

---

`POST '/questions'`

- Sends a post request in order to search for a specific question by search term
- Request Body:

```json
{
  "searchTerm": "world cup"
}
```

- Returns: any array of questions, a number of totalQuestions that met the search term and the current category string

```json
{
  "currentCategory": 1,
  "questions": [
    {
      "answer": "Brazil",
      "category": "3",
      "difficulty": 6,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "4",
      "difficulty": 6,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ],
  "success": true,
  "totalQuestions": 2
}
```
