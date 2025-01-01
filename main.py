from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import App
from database import Database

# Load environment variables
load_dotenv()

# Initialize Flask app
flask_app = Flask(__name__)

# Initialize Database and app
database = Database()
app = App(database)

@flask_app.route('/')
def default():
    watched, to_watch, watching = app.default()
    return render_template('movie.html', watched = watched, to_watch = to_watch, watching = watching)

@flask_app.route('/add_movie', methods=['POST'])
def add_movie_post():
    try:
        title = request.form['title'] if 'title' in request.form else ''
        year = int(request.form['year']) if 'year' in request.form else None
        description = request.form['description'] if 'description' in request.form else ''
        status = request.form['status'] if 'status' in request.form else ''
        progress = int(request.form['progress']) if 'progress' in request.form else 0    
        app.add_movie(title, year, description, status, progress)
        return jsonify({'message': 'Movie added successfully!', 'status': 'success'})
    except Exception as e:
        return jsonify({'message': e, 'status':'fail'})

@flask_app.route('/movie_recommendation', methods=['POST'])
def movie_recommendation():
    genre = request.form['genre']
    movies = app.movie_recommendation(genre)
    return jsonify(movies)

# Run the Flask app
if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=5000, debug=True)
