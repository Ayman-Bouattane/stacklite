from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump, load
from .utils import get_data_paths
from dask import dataframe as dd


def train_model():
    # Load and preprocess
    qdf = dd.read_csv(get_data_paths()['questions'], dtype={'CreationDate': 'object'})
    qdf = qdf.dropna(subset=['CreationDate'])
    qdf['CreationDate'] = dd.to_datetime(qdf['CreationDate'])

    daily_counts = qdf.groupby(qdf['CreationDate'].dt.date).size().compute()
    df = pd.DataFrame({
        'date': pd.to_datetime(daily_counts.index),
        'count': daily_counts.values
    })
    df['day_num'] = (df['date'] - df['date'].min()).dt.days

    X = df[['day_num']]
    y = df['count']
    model = LinearRegression()
    model.fit(X, y)
    dump(model, Path(__file__).parent / 'linear_model.joblib')
    return model, df


def predict(n_days: int):
    model_path = Path(__file__).parent / 'linear_model.joblib'
    model = load(model_path)
    import datetime

    # Determine last day_num
    # Assuming df from train_model is persisted or retrained on startup
    # For simplicity, retrain here (could refine)
    _, df = train_model()
    last_day_num = df['day_num'].max()

    preds = []
    for i in range(1, n_days + 1):
        day_num = last_day_num + i
        pred = model.predict([[day_num]])[0]
        date = df['date'].max() + pd.Timedelta(days=i)
        preds.append({'date': date.strftime('%Y-%m-%d'), 'predicted': float(pred)})
    return preds