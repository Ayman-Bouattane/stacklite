from dask import dataframe as dd
import pandas as pd
from .utils import get_data_paths
from dateutil import parser

def unique_tags(series):
    return list(series.unique())

def run_pipeline():
    # Chargement des données avec assume_missing pour éviter les erreurs de type
    questions = dd.read_csv('data/questions.csv', assume_missing=True)
    tags = dd.read_csv('data/question_tags.csv', assume_missing=True)

    # Sélection des colonnes nécessaires
    firsts = questions[['Id', 'CreationDate', 'Score']].drop_duplicates(subset='Id')

    # Forçons le type float64 pour éviter les conflits de merge
    firsts['Id'] = firsts['Id'].astype('float64')
    tags['Id'] = tags['Id'].astype('float64')

    # Définition du meta pour éviter les erreurs Dask
    meta = pd.DataFrame({'Id': pd.Series(dtype='float64'), 'TagList': pd.Series(dtype='object')})

    # Agrégation des tags
    tags_grouped = (
        tags.groupby('Id')['Tag']
        .apply(unique_tags, meta=meta)
        .reset_index()
        .rename(columns={'Tag': 'TagList'})
    )

    # Fusion des deux DataFrames sur la colonne Id
    grouped = firsts.merge(tags_grouped, on='Id', how='left')

    # Exécution réelle (Dask est paresseux)
    result = grouped.compute()

    return result
