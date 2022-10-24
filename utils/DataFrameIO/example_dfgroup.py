"""
platform: any
env: any
name: example_dfgroup.py
basic dataframe grouping example
"""
from configs.config import tmp_dir
import os
import pandas as pd


def group(d):
    """

    :param d: 文件夹
    :return:
    """
    def gid2uni_id(gids):
        """
        根据gid查询uni_id
        :param gids:
        :return:
        """
        ret = df_all["uni_id"][gids.tolist()]
        ret = ret.tolist()
        return ret

    # smiles csv包含id, smiles串， 摩尔量
    df_all = pd.DataFrame(columns=["id", "smiles", "molwt", "uni_id"])
    for sf in os.listdir(d):
        df = pd.read_csv(os.path.join(tmp_dir, "smiles", sf))
        # uni_id = csv文件名 + id
        df["uni_id"] = df["id"].apply(lambda x: sf.split(".")[0] + "_" + str(x))
        df_all = pd.concat([df_all, df])
    # 扔掉id和摩尔量
    df_all = df_all.drop(columns=["id", "molwt"])
    # 重置index（gid），便于分组时定位原来位置
    df_all = df_all.reset_index()

    # 按smiles分组，grouping表包含smiles以及对应gid的列表
    df_groups = df_all.groupby("smiles").groups
    df_grouping = pd.DataFrame({"group": df_groups.keys(), "gid": df_groups.values()})
    # gid变成uni_id
    df_grouping["uni_id"] = df_grouping["gid"].apply(lambda x: gid2uni_id(x))
    df_grouping = df_grouping.drop(columns=["gid"])
    return df_grouping


if __name__ == '__main__':
    group(os.path.join(tmp_dir, "smiles"))