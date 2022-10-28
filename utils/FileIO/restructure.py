"""
platform: any
env: any
name: fileExtract.py
key file extractor
"""
import os
from math import ceil
from shutil import copyfile
from configs.config import aug_dir, pdbbind_base


def augKeyFileExtractor(out_dir):
    """
    for data aug, extract key files(1 pdb with 1 sdf) from original ligand folder
    :param out_dir:
    :return:
    """
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


def augMatchPockets():
    """
    for data aug, get pocket from pdb2020 with matched id with original protein folder
    :return:
    """
    dst_dir = os.path.join(aug_dir["base"], "docking_set_pocket")
    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)
    for lig in os.listdir(aug_dir["ligands"]):
        if os.path.isdir(os.path.join(pdbbind_base, "general-minus-refined", lig)):
            pocket_f = os.path.join(pdbbind_base, "general-minus-refined", lig, "{}_pocket.pdb".format(lig))
        elif os.path.isdir(os.path.join(pdbbind_base, "refined-set", lig)):
            pocket_f = os.path.join(pdbbind_base, "refined-set", lig, "{}_pocket.pdb".format(lig))
        else:
            continue
        copyfile(pocket_f, os.path.join(dst_dir, "{}_pocket.pdb".format(lig)))


def toECIFModelTest(src_d, tar_d):
    """
    for ECIF model test, create a model test folder
    :param src_d:
    :param tar_d:
    :return:
    """
    targets = []
    for src_f in os.listdir(src_d):
        src_f_spl = src_f.split(".")
        if src_f_spl[-1] == "pdb":
            targets.append(src_f_spl[0].split("_")[0])
    for target in targets:
        prot_base = os.path.join(tar_d, target)
        if not os.path.isdir(prot_base):
            os.mkdir(prot_base)
            copyfile(os.path.join(src_d, "{}_p.pdb".format(target)), os.path.join(prot_base, "{}_protein.pdb".format(target)))
            os.mkdir(os.path.join(prot_base, "ligs"))
            if os.path.isfile(os.path.join(src_d, "{}.sdf".format(target))):
                copyfile(os.path.join(src_d, "{}.sdf".format(target)),
                         os.path.join(prot_base, "ligs", "{}.sdf".format(target)))
            if os.path.isfile(os.path.join(src_d, "{}_l.sdf".format(target))):
                copyfile(os.path.join(src_d, "{}_l.sdf".format(target)),
                         os.path.join(prot_base, "ligs", "{}_l.sdf".format(target)))
            if os.path.isfile(os.path.join(src_d, "{}_10.sdf".format(target))):
                copyfile(os.path.join(src_d, "{}_10.sdf".format(target)),
                         os.path.join(prot_base, "ligs", "{}_10.sdf".format(target)))


if __name__ == '__main__':
    toECIFModelTest("D:\\AlexYu\\MEIF\\model_test\\DEKOIS", "D:\\AlexYu\\MEIF\\model_test\\20221028")
