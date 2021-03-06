import webbrowser
import fresh_tomatoes
import media

# Avengers movie: movie title, storyline, poster image and movie trailer.
avengers = media.Movie(
    "Avengers",
    "American superhero film",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=BSMEkYCk4Vo")

# Taitanic movie: movie title, storyline, poster image and movie trailer.
taitanic = media.Movie(
    "Taitanic",
    "American epic romance-disaster film",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

# IT movie: movie title, storyline, poster image and movie trailer.
it = media.Movie(
    "IT",
    "Horro movie",
    "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg",
    "https://www.youtube.com/watch?v=FnCdOQsX5kc")

# Saw movie: movie title, storyline, poster image and movie trailer.
saw = media.Movie(
    "Saw",
    "Horro movie",
    "https://upload.wikimedia.org/wikipedia/en/5/56/Saw_official_poster.jpg",
    "https://www.youtube.com/watch?v=Lq2AzZB6DUE")

# Jumanji movie: movie title, storyline, poster image and movie trailer.
jumanji = media.Movie(
    "Jumanji",
    "American fantasy adventure film",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/Jumanji_poster.jpg",
    "https://www.youtube.com/watch?v=8WaAUE4MXs8")

# Grudge movie: movie title, storyline, poster image and movie trailer.
grudge = media.Movie(
    "Grudge",
    "Horro movie",
    "https://upload.wikimedia.org/wikipedia/en/9/91/The_Grudge_movie.jpg",
    "https://www.youtube.com/watch?v=9ZCIjKFCxdw")

# Hunger games movie: movie title, storyline, poster image and movie trailer.
hunger_games = media.Movie(
    "Hunger Games",
    "A really real reality show",
    "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",  # noqa
    "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# Set the movies that will passed to the media file
movies = [avengers, taitanic, it, saw, jumanji, grudge, hunger_games]

# Open the HTML file in a webbrower via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
