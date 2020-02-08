### Capstone :-

Capstone is a casting ungency

Token= "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1URkNSRGMyUWpsRVFqTTNRamhCTUVJNE9EQkJOVGN6UkRZMk5qVkZOVVE1UlRJNU56UkNSUSJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AwMS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWUxNzY4ZjE1MDgxNDUwZThkYTVmMDlmIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNTgxMTQ0NTk5LCJleHAiOjE1ODExODA5OTksImF6cCI6ImpJR1liYkJmOFlzREhZMFV2QXlQNHNaMkY3RTlBNkRUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOmRyaW5rcyIsImdldDphY3RvcnMiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDpkcmlua3MiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6ZHJpbmtzIl19.FeZxX_a2ZDHCxW-psY1t9_dxw-ZNYfcURT0Xq9Wzr_Wgul96Ezfl7fwQWHn9kcgxMMyEReB7_gXIG-5HnuNemfTwwzhsp-jFQplVki9BivFtq6PK1br6GljuzsGulqPOZ3QeXdUN9BBPrePaLBsUnNpf2r-fGNYyUyL7BkFpgOwPU5kSTDAWyAAtmfWQqRgHvgydf-0Cq9DDYodsJQDIGtpc6SBHPwqzDCGT7OiDFassbeDycfSMCbjGdCMTKQs_rdX29P60bVx-89L6Xn2YyiChLtDqygvhdaKwgfM_uX03fh5oZUNvUNMWVnWPo79M_8bTo20lLh9LAzzpioKz8A"

### Heroku

Follow the link above to access the deployed app on heroku https://capstone4.herokuapp.com/

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the python docs

### Virtual Enviornment :-

l would recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

python -m venv (name of your virtual evironment).Activate the virtual evirnoment.Its is time to activate your virtual environment run:

- source <name of virtual_environment>/bin/activate

### PIP Dependencies :-

Once you have your virtual environment setup and running, install dependencies and run:

- pip install -r requirements.txt

This will install all of the required packages we selected within the requirements.txt file.
Key Dependencies

    Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

    - SQLAlchemy

    - Flask-SQLAlchemy

### Running the server

First ensure you are working using your created virtual environment.
Each time you open a new terminal session, run:

  export FLASK_APP=app.py;

To run the server, execute:
   flask run --reload

The --reload flag will detect file changes and restart the server automatically.

### Setup Auth0

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

### API Endpoints :-

1 - GET Method :-

    i. GET- http://127.0.0.1:5000/movies
        - This endpoint method will return all the Movies data.
    ii. GET- http://127.0.0.1:5000/actors
        - This endpoint method will return all the actors data.

2- POST Methods :-

    i. POST- http://127.0.0.1:5000/movies
        - Using this endpoint method user can create new movies data.

        Parameters:
         - For movies this parameter should pass:
           i- title  ii- release_date


    ii. POST- http://127.0.0.1:5000/actors
        - Using this endpoint method user can create new actors data.

        Parameters:
        - For movies this parameter should pass:
        i- name  ii- age  iii- gender

3 - PATCH Methods :-

    i. PATCH- http://127.0.0.1:5000/movies/<int:id>
        - Using this endpoint method user can update the data for movies.
        - For update this method you should use to select the the data present in the database.

    ii. PATCH- http://127.0.0.1:5000/actors/<int:id>
        - Using this endpoint method user can update the data for actors.
        - For update this method you should use to select the the data present in the database.

4 - DELETE Methods :-

    i. DELETE- http://127.0.0.1:5000/movies/<int:id>
        - Using this end point user can the delete data.
        - For delete the you should pass the movies id which is present in the database.

    ii. DELETE- http://127.0.0.1:5000/actors/<int:id>
        - Using this end point user can the delete data.
        - For delete the you should pass the actors id which is present in the database.