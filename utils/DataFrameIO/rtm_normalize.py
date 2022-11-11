"""
platform: any
env: any
name: rtm_normalize.py
normalize rtm results
"""
from configs.config import tmp_dir

import os
import pandas as pd


def rtm_normalize(f_in, out_loc):
    """

    :param f_in: a dataframe, or a standard csv file that could be read by pandas
    :param out_loc: the output location(folder) of normalized results
    :return:
    """
    if not isinstance(f_in, pd.DataFrame):
        try:
            f_in = pd.read_csv(f_in)
        except FileNotFoundError:
            print("Error: No such file or directory: {}".format(f_in))
            return None
    f_in["id"] = f_in["id"].apply(lambda x: x.split("-")[0])
    f_in.to_csv(os.path.join(out_loc, "result_rtm.csv"), index=False)


if __name__ == '__main__':
    rtm_normalize(os.path.join(tmp_dir, "out_core.csv"), tmp_dir)
