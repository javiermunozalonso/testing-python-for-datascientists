import numpy as np
import pandas as pd
import re

def my_first_test():
    data = pd.read_csv('./data/netflix_titles.csv')
    data = data.dropna(subset=['cast', 'country', 'rating'])
    movies = data[data['type'] == 'Movie'].reset_index()
    movies = movies.drop(['index', 'show_id', 'type', 'date_added', 'release_year', 'duration', 'description'], axis=1)

    actors = []

    for i in movies['cast']:
        actor = re.split(r', \s*', i)
        actors.append(actor)

    flat_list = []
    for sublist in actors:
        for item in sublist:
            flat_list.append(item)

    actors_list = sorted(set(flat_list))

    binary_actors = [[0] * 0 for i in range(len(set(flat_list)))]

    for i in movies['cast']:
        k = 0
        for j in actors_list:
            if j in i:
                binary_actors[k].append(1.0)
            else:
                binary_actors[k].append(0.0)
            k+=1

    binary_actors = pd.DataFrame(binary_actors).transpose()

    assert binary_actors.shape == (5280, 24814)