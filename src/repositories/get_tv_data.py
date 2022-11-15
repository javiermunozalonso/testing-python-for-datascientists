
import pandas as pd


def get_tv_data() -> pd.DataFrame:
    data = pd.read_csv('./data/netflix_titles.csv')
    data = data.dropna(subset=['cast', 'country', 'rating'])
    data = data[data['type'] == 'TV Show'].reset_index()
    data = data.drop(['index', 'show_id', 'type', 'date_added',
                      'release_year', 'duration', 'description'], axis=1)
    return data
