from Show import Show
from BookMyShowEnums import Genre


class Movie(Show):
    def __init__(self, movie_id: str, genre: Genre, movie_name: str,
                 movie_duration: int, movie_rating: float, total_views: int):
        super().__init__(movie_id, genre, movie_name, movie_duration, movie_rating, total_views)

