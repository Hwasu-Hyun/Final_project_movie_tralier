import webbrowser


class Movie():
	""" This docstring shoud explain what the Movie() class does """
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, 
				poster_image, trailer_youtube):
		""" This docstring should explain the constructor method """
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		""" This docstring should explain what the show_trailer() function does """ 
		webbrowser.open(self.trailer_youtube_url)
