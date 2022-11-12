from zipfile import ZipFile
from pathlib import Path
import shutil
import logging

from kaggle.api.kaggle_api_extended import KaggleApi

DATA_FOLDER_LOCATION='./data'
DATASET_NAME = 'shivamb/netflix-shows'
DOWNLOADED_FILE_NAME='netflix_titles.csv.zip'
DOWNLOADED_FILE_LOCATION=f'{DATA_FOLDER_LOCATION}/{DOWNLOADED_FILE_NAME}'
FILE_NAME='netflix_titles.csv'

def __remove_data_folder():
    if Path(DATA_FOLDER_LOCATION).exists():
        shutil.rmtree(DATA_FOLDER_LOCATION)
    logging.info('The path is clear to start')
    return

def __create_data_folder():
    Path(DATA_FOLDER_LOCATION).mkdir(exist_ok=True)
    logging.info('Created the folder for the data')
    return

def __download_data_file():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file(dataset=DATASET_NAME, file_name=FILE_NAME,
                                path=DATA_FOLDER_LOCATION)
    logging.info('Downloaded the data from kaggle')
    return

def __decompress_data_file():
    with ZipFile(DOWNLOADED_FILE_LOCATION,'r') as zip:
        zip.extractall(path=DATA_FOLDER_LOCATION)
    logging.info('The file has been decompressed')
    return

def __remove_downloaded_file():
    if Path(DOWNLOADED_FILE_LOCATION).exists():
        Path(DOWNLOADED_FILE_LOCATION).unlink()
    logging.info('The file downloaded has been deleted')
    return

def run():
    __remove_data_folder()
    __create_data_folder()
    __download_data_file()
    __decompress_data_file()
    __remove_downloaded_file()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()