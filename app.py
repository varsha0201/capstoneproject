import os
import json
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from auth import AuthError, requires_auth
from models import Movie, Actor, db_setup, db

## ROUTES
def create_app():
    app = Flask(__name__)
    db_setup(app)
    CORS(app)

#----------------------------------------------------------------------------#
# Endpoints
#----------------------------------------------------------------------------#

    @app.route('/') 
    def home(): return 'Welcome to capstone'


# TODO DONE implement endpoint GET /movies

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_all_movies(payload):
        movies = Movie.query.all()
        return jsonify({
            "success": True,
            "all_movies": [movies.format() for movies in movies]
        }),200

# TODO DONE implement endpoint GET /actors
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_all_actors(payload):
        actors = Actor.query.all()
        return jsonify({
            "success": True,
            "all_actors": [actors.format() for actors in actors]
        }),200
        
# TODO-DONE implement endpoint POST /movies    
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        body = request.get_json()
        title = body.get('title')
        release_date = body.get('release_date')
        movie = Movie(title=title, release_date=release_date)
        movie.insert()
        return jsonify({
            'success': True, 
            'movies': movie.format()
        })

# TODO-DONE implement endpoint POST /actors
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        actor = Actor(
            name=name, 
            age=age, 
            gender=gender
            )
        db.session.add(actor)
        db.session.commit()
        return jsonify({
            'success': True, 
            'actors': actor.format()
        }), 201
        
# TODO DONE implement endpoint PATCH /movies/<id>
    @app.route('/movies/<int:id>', methods =['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(payload, id):
        data = request.get_json()
        movies = Movie.query.filter(Movie.id ==id).one_or_none()
        if not movies:
            abort(404)
        movies.title = data.get('title', movies.title)
        movies.update()
        return jsonify ({
            "success":True,
            "movies": movies.format()
        }),  200

# TODO DONE implement endpoint PATCH /actors/<id>
    @app.route('/actors/<int:id>', methods =['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(payload, id):
        data = request.get_json()
        actor = Actor.query.filter(Actor.id ==id).one_or_none()
        if not actor:
            abort(404)
        actor.name = data.get('name', actor.name)
        actor.age = data.get('age', actor.age)
        actor.gender = data.get('gender', actor.gender)  
        db.session.commit()
        return jsonify ({
            "success":True,
            "actors": actor.format()
        }), 200

# TODO DONE implement endpoint DELETE /movies/<drink_id>    
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(payload, id):
        movie = Movie.query.filter(Movie.id ==id).one_or_none()
        if not movie:
            abort(404)
        movie.delete()
        return jsonify({
            "success": True,
            "delete": id
        }), 200

# TODO DONE implement endpoint DELETE /actors/<drink_id>    
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(payload, id):
        actor = Actor.query.filter(Actor.id ==id).one_or_none()
        if not actor:
            abort(404)
        actor.delete()
        # db.session.add(actor)
        # db.session.commit()
        return jsonify({
            "success": True,
            "delete": id
        }), 200
## Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
            }), 422

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
            }), 404

    @app.errorhandler(405)
    def permission_error(error):
        return jsonify({
            "success": False,
            "error":405,
            "message": "Authentication error"
        }), 405
        
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "resource not found"
            }), 400

    @app.errorhandler(401)
    def custom_401(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized user, please login and try again."
            }), 40

    return app

app = create_app()

if __name__ =='__main__':
    app.run()