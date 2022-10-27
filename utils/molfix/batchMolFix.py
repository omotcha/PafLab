"""
platform: any
env: any with openbabel
name: batchMolFix.py
perform some basic mol-fix based on obabel
"""
import os
import warnings
from configs.config import platform_delimiter, aug_dir
from tqdm import tqdm
warnings.filterwarnings("ignore")


def mol2toSDF(f_in, d_out):
    """
    convert mol2 to sdf using obabel
    :param f_in: mol2 format file (abs path)
    :param d_out:
    :return:
    """
    f_split = f_in.split(platform_delimiter)[-1].split(".")
    if f_split[1] != "mol2":
        return
    f_out = "{}_babel.sdf".format(f_split[0])
    babel_cmd = "obabel -imol2 {} -osdf -O {}".format(f_in, os.path.join(d_out, f_out))
    os.system(babel_cmd)


def augMol2toSDF():
    lig_base = aug_dir["ligands"]
    for lig_name in tqdm(os.listdir(lig_base)):
        dwork = os.path.join(lig_base, lig_name)
        n = int(len(os.listdir(dwork))/4)
        for i in range(n):
            lig = os.path.join(dwork, "{}_ledock001.mol2".format(i+1))
            mol2toSDF(lig, dwork)


if __name__ == '__main__':
    augMol2toSDF()
