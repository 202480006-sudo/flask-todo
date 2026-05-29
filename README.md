Simple Flask Todo App using SQLAlchemy and SQLite database.

For styling [semantic-ui](https://semantic-ui.com/) is used.

### Setup
Create project with virtual environment

```console
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

Activate it
```console
$ . venv/bin/activate
```

or on Windows
```console
venv\Scripts\activate
```

Install Flask
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
```

Set environment variables in terminal
```console
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

or on Windows
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```


## Enhancing a Flask Web Application with REST API Functionality
-----------------------------------------------------
## REST API for Flask Todo App

This project extends an existing Flask Todo application by adding a REST API and CRUD functionality.

### Features Added
I added two features
- Edit task
- Delete task 

### API Endpoints:
These are the API endpoints I used:
- GET -Retrieve all tasks and one specific task only
- POST -Create a new task
- PUT -Update an existing task
- DELETE -Delete a task

### 3. Error Handling
The HTTP status codes error handling I use:

- 200 -Successful request
- 201 -created successfully
- 400 -Bad request
- 404 -not found

### Testing

### Postman Tests include:
- GET methid -all tasks
- POST method -create task
- PUT method-update task
- DELETE method- delete task
- Negative test like invalid input and missing data

### Run Tests:
python -m pytest
