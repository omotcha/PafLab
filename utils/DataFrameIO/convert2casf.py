"""
platform: any
env: any
name: convert2casf.py
convert dataframe based predictions to casf-needed format
"""
import os

from configs.config import tmp_dir
import pandas as pd


def rtm2casf(f_df, mode, oth):
    """

    :param f_df:
    :param mode:
    :param oth:
    :return:
    """
    if not isinstance(f_df, pd.DataFrame):
        try:
            f_df = pd.read_csv(f_df)
        except FileNotFoundError:
            print("Error: No such file or directory: {}".format(f_df))
            return None
    if mode in ["oc"]:
        f_df.rename(columns={"id": "#code"}, inplace=True)

    if mode in ["oc"]:
        f_df["#code"] = f_df["#code"].apply(lambda x: x.split("_")[0])
    elif mode in ["od"]:
        f_df["#code"] = f_df["#code"].apply(lambda x: x.split("-")[0])

    if mode in ["oc"]:
        f_df.to_csv(os.path.join(tmp_dir, "rtm.dat"), index=False)
    elif mode in ["od"]:
        lig_df = pd.read_csv(os.path.join(tmp_dir, "rtm.dat"))
        lig_df = lig_df[lig_df["#code"] == oth[0]]
        lig_df["#code"] = "{}_ligand".format(oth[0])
        f_df = pd.concat([f_df, lig_df], ignore_index=True)
        f_df.to_csv(os.path.join(tmp_dir, "dec_doc_new", "{}_score.dat".format(oth[0])), index=False)


if __name__ == '__main__':
    dec_doc = os.path.join(tmp_dir, "dec_doc")
    for f in os.listdir(dec_doc):
        f = f.split("_")[0]
        rtm2casf(os.path.join(dec_doc, "{}_score.csv".format(f)), "od", [f])
