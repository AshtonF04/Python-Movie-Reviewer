class Movie:
    reviews = []

    def add_review(title, release_year, genre, rating):
        movie = Movie(title, release_year, genre, rating)
        Movie.reviews.append(movie)

        str_len = len(str(movie))
        print("-" * (str_len + 40))
        print(f"{movie} was successfully added to the database.")
        print("-" * (str_len + 40))

    def list_reviews():
        pass


    def __init__(self, title, release_year, genre, rating):
        self._title = title
        self._release_year = release_year
        self._genre = genre
        self._rating = rating

    @property
    def title(self):
        return self._title
    
    @property
    def release_year(self):
        return self._release_year

    @property
    def genre(self):
        return self._genre
    
    @property
    def rating(self):
        return self._rating
    
    @title.setter
    def title(self, new_title):
        self._title = new_title

    @release_year.setter
    def release_year(self, new_release_year):
        self._release_year = new_release_year

    @genre.setter
    def genre(self, new_genre):
        self._genre = new_genre

    @rating.setter
    def rating(self, new_rating):
        self._rating = new_rating

    def __str__(self):
        return f"'{self._title}' {self._release_year}, {self._genre}: {self._rating}/10⭐️"