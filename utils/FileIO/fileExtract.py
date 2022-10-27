"""
platform: any
env: any
name: fileExtract.py
key file extractor
"""
import os
from math import ceil
from shutil import copyfile
from configs.config import aug_dir


def augExtract(out_dir):
    dst_dir = os.path.join(out_dir, "docking_set_extracted")
    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)
    for lig in os.listdir(aug_dir["ligands"]):
        new_lig_dir = os.path.join(dst_dir, lig)
        if not os.path.isdir(new_lig_dir):
            os.mkdir(new_lig_dir)
        lig_dir = os.path.join(aug_dir["ligands"], lig)
        n = ceil(len(os.listdir(lig_dir))/5)
        for i in range(n):
            if not os.path.isfile(os.path.join(lig_dir, "{}_ledock001_babel.sdf".format(i+1))):
                continue
            if not os.path.isfile(os.path.join(new_lig_dir, "{}_ledock001_babel.sdf".format(i+1))):
                copyfile(os.path.join(lig_dir, "{}_ledock001_babel.sdf".format(i+1)),
                         os.path.join(new_lig_dir, "{}_ledock001_babel.sdf".format(i+1)))


if __name__ == '__main__':
    augExtract(aug_dir["base"])
