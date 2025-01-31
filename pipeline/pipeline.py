from pipeline.data_handler import DataHandler
import pandas as pd
from datetime import datetime as dt
 

class Pipeline:

    _LABELS = [
        'Nome do produto', 'Categoria', 'Preço (R$)', 
        'Quantidade', 'Filial', 'Data da venda'
    ]

    def __init__(self, handler: DataHandler = None) -> None:
        self.handler = handler

    def run(self) -> None:
        data_a = self.handler.load_data(
            './raw_data/dados_empresaA.json', type='json'
        )
        data_b = self.handler.load_data(
            './raw_data/dados_empresaB.csv', type='csv'
        )

        data_a.columns = self._LABELS[:5]
        data_b.columns = self._LABELS

        complete_df = pd.concat([data_a, data_b], ignore_index=True)

        #data fomatting
        complete_df['Data da venda'] = pd.to_datetime(
            complete_df['Data da venda'], 
            format='%Y-%m-%d %H:%M:%S.%f', 
            errors='coerce'
        )

        self.handler.save_data(
            complete_df, './processed_data/complete_data.csv'
        )
