import webbrowser

class Movie(object):
    """ Class the alaw user to crea movie object with basic actributes

        Attributes:
            title: the movie title
            box_art: the movie box cover art
            poster_image_url: the movie poster
            trailer_youtube_url: the movie trailer in youtube
    """

    def __init__(self,movie_title, movie_box_art, poster_image,trailer_youtube):
        """Construct an new instance of Movie.

           Arg:
              movie_title: the title of the movie
              movie_box_art: the url for the movie box art
              poster_image: the url for the movie poster
              trailer_youtube: the url for the movie trailer in youtube

           Return:
               A new instance of the class with the atribure initialaize
        """
        self.title = movie_title
        self.box_art = movie_box_art
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube