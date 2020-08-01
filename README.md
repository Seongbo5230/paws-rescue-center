A website for fictional animal rescue org named "Paws Rescue Center"

Created using Flask

# Set Up
1. Create environment if 'venv' dir hasn't been created
`python3 -m venv venv`
2. Activate the environment
`. venv/bin/activate`
3. Install Flask
`pip3 install Flask`

# Turn off Venv
1. Deactivate the environment
`deactivate`

# Run Flask App
```
export FLASK_APP=<app_name>.py
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
```

# Jinja Delimiters
```
{% ... %} is used for statements.
{{ ... }} is used for variables.
{# ... #} is used for comments.
# ... ## is used for line statements.
```

# Things to implement later:
Flask Cache: For cache management in a Flask application.

Flask Migrate: Handles the SQLAlchemy database migrations for Flask applications using Alembic.

pyscopg: To integrate PostgreSQL with your application.

Flask-RESTful: Used for building REST APIs with Flask.

Flask-mail: Provides support to set up SMTP with your Flask application.

Flask-Login: Provides an extension to efficiently manage user sessions, login, and logout.

Gunicorn: A WSGI (HTTP) web server that can be used to deploy Flask applications.

Nginx: Handles requests from the client in the deployment environment.
