
import pandas as pd


class Repository:

    __data: pd.DataFrame
    __movies: pd.DataFrame
    __tv: pd.DataFrame

    def __init__(self):
        self.__data = pd.read_csv('./data/netflix_titles.csv')
        self.__data = self.__data.dropna(subset=['cast', 'country', 'rating'])

    def get_tv_data(self) -> pd.DataFrame:
        if self.__tv:
            return self.__tv

        self.__tv = self.__data[self.__data['type'] == 'TV Show'].reset_index()
        self.__tv = self.__tv.drop(['index', 'show_id', 'type', 'date_added',
                                   'release_year', 'duration', 'description'], axis=1)
        return self.__tv

    def get_movies_data(self) -> pd.DataFrame:
        if self.__movies:
            return self.__movies
        self.__movies = self.__data[self.__data['type']
                                    == 'Movie'].reset_index()
        self.__movies = self.__movies.drop(['index', 'show_id', 'type', 'date_added',
                                            'release_year', 'duration', 'description'], axis=1)
        return self.__movies
