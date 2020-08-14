from pandas import DataFrame
import pandas as pd

pd.set_option('mode.chained_assignment', None)


def one_to_many(df : DataFrame, column_name):
    columns = sorted(list(set(df[column_name].tolist())))
    for column in columns:
        df[column] = 0
        df[column] = df[column].astype(int)
    for i, row in df.iterrows():
        for column in columns:
            if column == row[column_name]:
                df.loc[i,column] = 1
    return df


def get_values(df: DataFrame, column_name):
    return sorted(list(set(df[column_name].tolist())))