import os
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile


def get_data_paths():
    base = Path(__file__).parent.parent.parent / 'data'
    return {
        'questions': base / 'questions.csv',
        'question_tags': base / 'question_tags.csv',
    }
