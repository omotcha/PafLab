"""
platform: any
env: any
name: df_concat.py
concatenate several dataframes
"""
import pandas as pd
import os


def ecif_model_test_concat(base_d):
    """
    concatenate ecif predictions
    :param base_d:
    :return:
    """
    df_total = pd.DataFrame(columns=["protein", "ligand", "prediction"])
    for target in os.listdir(base_d):
        pred_f = os.path.join(base_d, target, "{}_result.csv".format(target))
        if os.path.isfile(pred_f):
            df = pd.read_csv(pred_f)[df_total.columns]
            df_total = pd.concat([df_total, df])
    df_total.to_csv(os.path.join(base_d, "ecif_results.csv"), index=False)


if __name__ == '__main__':
    ecif_model_test_concat("D:\\AlexYu\\MEIF\\model_test\\20221028")
