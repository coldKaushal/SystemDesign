from BookMyShowEnums import Genre


class Show:
    def __init__(self, show_id: str, genre: Genre, show_name: str,
                 show_duration: int, show_rating: float, total_views: int):
        self.__show_id = show_id
        self.__genre = genre
        self.__show_name = show_name
        self.__show_duration = show_duration
        self.__show_rating = show_rating
        self.__total_view = total_views

    def get_show_id(self):
        return self.__show_id

    def get_genre(self):
        return self.__genre

    def get_show_name(self):
        return self.__show_name

    def get_show_duration(self):
        return self.__show_duration

    def get_show_rating(self):
        return self.__show_rating

    def get_total_view(self):
        return self.__total_view

    def update_show_rating(self, new_rating):
        self.__show_rating = new_rating