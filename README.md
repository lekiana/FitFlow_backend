## Creating .env file

To run server there needs to be a database connection.
You can achieve it by setting the .env file with parameters shown in .env.example
By default configured database is postgreSQL, it can be changed in the project settings file: settings.py.

## Setting up the project

### `python -m venv venv`

Creates virtual environment.

### `venv\Scripts\activate`

Activates virtual environment.

### `pip install -r requirements.txt`

Installs required dependencies.

### `python manage.py runserver`

Runs server on port localhost:8000.

