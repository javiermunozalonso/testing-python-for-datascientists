import numpy as np
import pandas as pd
import pytest

from src.logic import preprocessed_movies_actors

from src.repositories import Repository


# def test_preprocessed_movies_actors_test1(mocker, short_data: pd.DataFrame):
#     repository = Repository()
#     with mocker.patch.object(repository, 'get_movies_data', return_value=short_data) as mock_get_movies_data:
#         preprocessed_movies_actors(repository=repository)
#         mock_get_movies_data.assert_called_once()
#         repository.get_movies_data.assert_called_with

def test_preprocessed_movies_actors_test1(mocker, short_data: pd.DataFrame):
    # repository = Repository()
    repository = mocker.Mock()
    repository.get_movies_data.return_value = short_data
    preprocessed_movies_actors(repository=repository)
    repository.get_movies_data.assert_called_with()


def test_preprocessed_movies_actors2(mocker, short_data: pd.DataFrame):

    mock_get_movies_data = mocker.patch(
        "src.repositories.Repository.get_movies_data", return_value=short_data
    )

    preprocessed_movies_actors()
    mock_get_movies_data.assert_called_with()
