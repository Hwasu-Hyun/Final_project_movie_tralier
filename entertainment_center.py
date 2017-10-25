import webbrowser
import fresh_tomatoes
import media 

avengers = media.Movie("Avengers",
	"American superhero film ",
	"https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
	"https://www.youtube.com/watch?v=BSMEkYCk4Vo")
 
taitanic = media.Movie("Taitanic", 
	"American epic romance-disaster film", 
	"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg", 
	"https://www.youtube.com/watch?v=zCy5WQ9S4c0")

it = media.Movie("IT", 
	"Horro movie",
	"https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg",
	"https://www.youtube.com/watch?v=FnCdOQsX5kc")


saw = media.Movie("Saw", 
	"Horro movie", 
	"https://upload.wikimedia.org/wikipedia/en/5/56/Saw_official_poster.jpg", 
	"https://www.youtube.com/watch?v=Lq2AzZB6DUE")

jumanji = media.Movie("Jumanji", 
	"American fantasy adventure film", 
	"https://upload.wikimedia.org/wikipedia/en/b/b6/Jumanji_poster.jpg", 
	"https://www.youtube.com/watch?v=8WaAUE4MXs8")

grudge = media.Movie("Grudge", 
	"Horro movie", 
	"https://upload.wikimedia.org/wikipedia/en/9/91/The_Grudge_movie.jpg",
	"https://www.youtube.com/watch?v=9ZCIjKFCxdw")

hunger_games = media.Movie("Hunger Games", 
	"A really real reality show", 
	"https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg", 
	"https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [avengers, taitanic, it, saw, jumanji, grudge, hunger_games]
fresh_tomatoes.open_movies_page(movies)
