from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

movies = {
    1: {"title": "Inception", "description": "A thief enters dreams to steal secrets."},
    2: {"title": "Interstellar", "description": "A journey through space and time."},
    3: {"title": "The Matrix", "description": "Reality is not what it seems."}
}

@app.route('/')
def home():
    return render_template('home.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    movie = movies.get(movie_id)
    return render_template('movie.html', movie=movie, movie_id=movie_id)

@app.route('/random')
def random_movie():
    movie_id = random.choice(list(movies.keys()))
    return redirect(url_for('movie', movie_id=movie_id))

if __name__ == '__main__':
    app.run(debug=True)