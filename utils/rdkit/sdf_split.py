"""
platform: any
env: any with rdkit
name: sdf_split.py
split sdf into smaller ones
"""
import os
from rdkit import Chem

from configs.config import extratest_dir


def split_sdf(src_f, n_mol):
    """

    :param src_f: source sdf file
    :param n_mol: #mol per target file
    :return:
    """
    contents = open(src_f, 'r').read()
    blocks = [c + "$$$$\n" for c in contents.split("$$$$\n")[:-1]]
    tasks = [blocks[i:i+n_mol] for i in range(0, len(blocks), n_mol)]
    for task in tasks:
        ligs = [Chem.MolFromMolBlock(block) for block in task]
        print(len(ligs))


def get_lig_blocks(src_f):
    """

    :param src_f: source sdf file
    :return:
    """
    contents = open(src_f, 'r').read()
    blocks = [c + "$$$$\n" for c in contents.split("$$$$\n")[:-1]]
    return blocks


def split_into_single_sdf(src_f, tgt_d):
    """

    :param tgt_d:
    :param src_f:
    :return:
    """
    blocks = get_lig_blocks(src_f)
    for block in blocks:
        lid = block.split("\n")[0]
        with open(os.path.join(tgt_d, "{}.sdf".format(lid)), 'w') as f:
            f.write(block)


if __name__ == '__main__':
    base_dir = os.path.join(extratest_dir, "20221109", "7ama")
    # split_sdf(os.path.join(base_dir, "all.sdf"), 1000)
    split_into_single_sdf(os.path.join(base_dir, "7ama_enamine_glide.sdf"), os.path.join(base_dir, "ligs"))
