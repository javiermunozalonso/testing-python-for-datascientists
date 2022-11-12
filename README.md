# testing-python-for-datascientists

This project is for show different ways to test the python code

## Requirements

### 1. Conda

Downloading and install [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html#regular-installation) ([anaconda](https://docs.conda.io/projects/conda/en/stable/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html))

### 2. Install environment

```bash
conda env create -f .\environment.yml
```

## Dataset

If you don't have a API Token from kaggle you need to create one to follow [these steps](https://www.kaggle.com/docs/api#getting-started-installation-&-authentication) and use the next command or you can download manually the csv file and put it in the local location ```./data```.

```bash
conda activate testing && python download_data.py
```

## References

1. [Netflix dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)

2. [Notebook dataset overview](https://www.kaggle.com/code/shivamb/netflix-shows-and-movies-exploratory-analysis)

3. [Notebook train recommender](https://www.kaggle.com/code/eward96/netflix-recommendation-engine#4.-Developing-Recommendation-Engine-using-cast,-director,-country,-rating-and-genres)
