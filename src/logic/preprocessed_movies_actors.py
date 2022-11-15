from src.utils import get_matrix_binary, get_unique_sorted_values_from_list
from src.repositories import Repository


def preprocessed_movies_actors(repository: Repository = Repository()):
    movies_data = repository.get_movies_data()
    cast_movies_data = movies_data['cast']
    cast_list = get_unique_sorted_values_from_list(
        values_list=cast_movies_data)
    return get_matrix_binary(data=cast_movies_data, list_flattened=cast_list)
