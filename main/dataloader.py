import pandas as pd
import os

data_df = None

def load_data():
    global data_df
    if data_df is not None:
        return data_df

    csv_file_path = os.path.join('main','data','metadata.csv')

    data_df = pd.read_csv(csv_file_path)
    data_df.fillna('', inplace=True)

    return data_df