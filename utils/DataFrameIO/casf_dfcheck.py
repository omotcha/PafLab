"""
platform: any
env: any
name: casf_dfcheck.py
check items need for casf benchmark
"""
import os

from configs.config import tmp_dir
import pandas as pd


def check_docking_df_integrity(fdr_be_checked, fdr_reference):
    """

    :return:
    """
    dir_be_checked = os.listdir(fdr_be_checked)
    dir_reference = os.listdir(fdr_reference)
    assert len(dir_be_checked) == len(dir_reference)
    err_fl = []
    for f in dir_reference:
        df_be_checked = pd.read_csv(os.path.join(fdr_be_checked, f))
        df_reference = pd.read_csv(os.path.join(fdr_reference, f))
        if len(df_be_checked) != len(df_reference):
            err_fl.append(f)
    print(err_fl)


if __name__ == '__main__':
    check_docking_df_integrity(os.path.join(tmp_dir, "dec_doc_new"), os.path.join(tmp_dir, "dec_doc_tmp"))
