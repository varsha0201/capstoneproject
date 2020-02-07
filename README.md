---------Capstone---------------------

Capstone is a casting ungency

Heroku

Follow the link above to access the deployed app on heroku https://capstone4.herokuapp.com/
Getting Started
Installing Dependencies
Python 3.7

Follow instructions to install the latest version of python for your platform in the python docs
Virtual Enviornment

l would recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

python -m venv (name of your virtual evironment)

Activate the virtual evirnoment

Its is time to activate your virtual environment run:

source <name of virtual environment>/bin/activate

PIP Dependencies

Once you have your virtual environment setup and running, install dependencies and run:

pip install -r requirements.txt

This will install all of the required packages we selected within the requirements.txt file.
Key Dependencies

    Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

    SQLAlchemy

    Flask-SQLAlchemy

Running the server

First ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

export FLASK_APP=app.py;

To run the server, execute:

flask run --reload

The --reload flag will detect file changes and restart the server automatically.
Setup Auth0

    Create a new Auth0 Account
    Select a unique tenant domain
    Create a new, single page web application
    Create a new API
        in API Settings:
            Enable RBAC
            Enable Add Permissions in the Access Token
    Create new API permissions:
        get:movies
        post:movies
        patch:movies
        delete:movies
        get:actors
        post:actors
        patch:actors
        delete:actors
    Create new roles for:

        Casting Assistant
            can view:actors
            can view:movies

        Casting Director

            can perform all actions for the casting assistant
                get:movies
                post:movies
                patch:movies
                get:actors
                patch:actors
                delete:actors

        Executive Producer

            Can perform all actions for the casting director
                get:movies
                post:movies
                patch:movies
                delete:movies
                get:actors
                post:actors
                patch:actors
                delete:actors
