"""
platform: any
env: any
name: df_compare.py
compare 2 dataframes
"""
import pandas as pd
import os


def strict_compare(df_1, df_2):
    """

    :param df_1:
    :param df_2:
    :return:
    """
    return df_1.compare(df_2)


if __name__ == '__main__':
    df = pd.read_csv("D:\\AlexYu\\more\\Ligand.csv")
    sdf = pd.read_csv("D:\\AlexYu\\more\\SLigand.csv")
    print(strict_compare(df, sdf))
