
import pandas as pd
import pytest


@pytest.fixture
def short_data() -> pd.DataFrame:
    data = pd.read_csv('./test/dummy_data/short_netflix_titles.csv')
    return data.dropna(subset=['cast', 'country', 'rating'])
