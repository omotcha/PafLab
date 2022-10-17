"""
platform: any
env: any with spyrmsd
name: testLigRMSD.py
tester of lig rmsd
"""

import os
from utils.rmsd.ligrmsd import RMSDCalculator
from configs.config import *


def test():
    ref_base = os.path.join(tmp_dir, "CASF_ledock_redocking_pdb2sdf")
    rmsd = []
    rmsd_helper = RMSDCalculator()
    err_list = []
    for pid in os.listdir(ref_base):
        ligand = os.path.join(ref_base, pid, "{}_dock.sdf".format(pid))
        ligand_ref = os.path.join(coreset_dir, pid, "{}_ligand.sdf".format(pid))
        item = None
        try:
            item = {pid: rmsd_helper.calc_rmsd(ligand, ligand_ref, "symmetric", minimize=False)}
        except Exception as e:
            # err_list.append(pid)
            try:
                ligand_ref = os.path.join(coreset_dir, pid, "{}_ligand.mol2".format(pid))
                item = {pid: rmsd_helper.calc_rmsd(ligand, ligand_ref, "symmetric", minimize=False)}
            except Exception:
                # err_list.append(pid)
                try:
                    ligand_ref = os.path.join("E:\\datasets\\casf2016\\CASF-2016\\coreset_moe", "{}_ligand_moe.sdf".format(pid))
                    item = {pid: rmsd_helper.calc_rmsd(ligand, ligand_ref, "symmetric", minimize=False)}
                except Exception:
                    err_list.append(pid)
        if item is not None:
            rmsd.append(item)
    print(rmsd)
    print(len(rmsd))
    print(err_list)


if __name__ == '__main__':
    test()
