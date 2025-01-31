import pandas as pd
from typing import Callable, Any


class DataHandler():

    def load_data(self, path: str, type: str = 'csv') -> pd.DataFrame:
        if type == 'json':
            return pd.read_json(path)
        elif type == 'csv':
            return pd.read_csv(path)

    def save_data(self, data: pd.DataFrame, path: str) -> None:
        data.to_csv(path, index=False, encoding='utf-8', date_format='%Y-%m-%d')
