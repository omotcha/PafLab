"""
platform: any
env: any with spyrmsd
name: testLigRMSD.py
tester of lig rmsd
"""

import os

import pandas as pd

from utils.rmsd.ligrmsd import RMSDCalculator
from configs.config import *


def test():
    ref_base = os.path.join(tmp_dir, "CASF_ledock_redocking_pdb2sdf")
    rmsd = []
    rmsd_helper = RMSDCalculator()
    pids = os.listdir(ref_base)
    for pid in pids:
        ligand = os.path.join(ref_base, pid, "{}_dock.sdf".format(pid))
        ligand_ref = os.path.join(coreset_dir, pid, "{}_ligand.sdf".format(pid))
        rmsd.append(rmsd_helper.calc_rmsd(ligand, ligand_ref, "symmetric", minimize=False)[0])
    ret = pd.DataFrame({"id": pids, "rmsd": rmsd})
    ret.to_csv("./output/rmsd.csv", index=False)


if __name__ == '__main__':
    test()
