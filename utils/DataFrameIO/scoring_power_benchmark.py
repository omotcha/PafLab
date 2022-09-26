"""
platform: win
env: any
name: scoring_power_benchmark.py
get sp benchmark
"""
import os

from configs.config import tmp_dir
import pandas as pd


def get_benchmark():
    bm = pd.read_csv(os.path.join(tmp_dir, "sp_benchmark.txt"), delimiter=" ")
    bm["left_ci"] = bm["left_ci"].apply(lambda x: x[1:])
    bm["right_ci"] = bm["right_ci"].apply(lambda x: x[:-1])
    bm = bm.drop(columns=["id", "num", "ch"])
    return bm


if __name__ == '__main__':
    pass
