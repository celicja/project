import pandas as pd
from .database import get_engine

def load_csv():

    df = pd.read_csv("/app/data/data.csv")

    engine = get_engine()

    df.to_sql(
        "online_retail",
        engine,
        schema="raw",
        if_exists="append",
        index=False
    )