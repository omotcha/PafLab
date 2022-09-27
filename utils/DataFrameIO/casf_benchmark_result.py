"""
platform: win
env: any
name: scoring_power_benchmark.py
get sp benchmark
"""
import os

from configs.config import tmp_dir
import pandas as pd


def get_scoring_power_benchmark():
    bm = pd.read_csv(os.path.join(tmp_dir, "sp_benchmark.txt"), delimiter=" ")
    bm["left_ci"] = bm["left_ci"].apply(lambda x: x[1:])
    bm["right_ci"] = bm["right_ci"].apply(lambda x: x[:-1])
    bm = bm.drop(columns=["id", "num", "ch"])
    return bm


def get_ranking_power_benchmark():
    bm = pd.read_csv(os.path.join(tmp_dir, "rp_benchmark.txt"), delimiter=" ")
    bm["left_ci"] = bm["left_ci"].apply(lambda x: x[1:])
    bm["right_ci"] = bm["right_ci"].apply(lambda x: x[:-1])
    bm = bm.drop(columns=["id", "ch"])
    return bm


def get_docking_power_benchmark():
    bm = pd.read_csv(os.path.join(tmp_dir, "dp_benchmark.txt"), delimiter=" ")
    bm["top1"] = bm["top1"].apply(lambda x: float(x[:-1]) / 100)
    bm["left_ci"] = bm["left_ci"].apply(lambda x: float(x[1:-1]) / 100)
    bm["right_ci"] = bm["right_ci"].apply(lambda x: float(x[:-2]) / 100)
    bm = bm.drop(columns=["id", "ch", "top2", "top3"])
    return bm


if __name__ == '__main__':
    print(get_docking_power_benchmark())
