import webbrowser

"""Class that will store all the informations of the movies."""
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

    """Play the trailers in the web browser."""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
