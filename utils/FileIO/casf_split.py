"""
platform: any
env: any
name: casf_split.py
split casf(pdbbind) dataset
"""
import os
from configs.config import pdbbind_base, tmp_dir
import numpy as np


def get_train_valid_ids(dataset_base):
    """
    make sure in dataset_base, it contains 3 folders:
    casf(coreset), general-refined and refined(may include ids in coreset)
    :param dataset_base:
    :return:
    """
    core_ids = [i for i in os.listdir(os.path.join(dataset_base, "casf"))
                if len(i) == 4]
    refined_ids = [i for i in os.listdir(os.path.join(dataset_base, "refined-set"))
                   if len(i) == 4 and i not in core_ids]
    general_minus_refined_ids = [i for i in os.listdir(os.path.join(dataset_base, "general-minus-refined"))
                                 if len(i) == 4]
    return refined_ids + general_minus_refined_ids


def del_file(path):
    for i in os.listdir(path):
        f = os.path.join(path, i)
        if os.path.isfile(f):
            os.remove(f)
        else:
            del_file(f)
            os.rmdir(f)
    os.rmdir(path)


def rm_core(core_base, dataset_base):
    core_ids = [i for i in os.listdir(os.path.join(core_base, "casf"))
                if len(i) == 4]
    for core_id in core_ids:
        path = os.path.join(dataset_base, core_id)
        del_file(path)


def train_ids_check():
    train_ids = np.load(os.path.join(tmp_dir, "v2020_train_ids.npy"))
    cur_ids = os.listdir("E:\\datasets\\dataset\\pdbbind2020_rtm")
    for cur_id in cur_ids:
        if cur_id not in train_ids:
            print(cur_id)


if __name__ == '__main__':
    train_ids_check()
    # rm_core(pdbbind_base, "E:\\datasets\\dataset\\pdbbind2020_rtm")
