"""
platform: any
env: any with spyrmsd
name: ligrmsd.py
RMSD calculation
"""
import os.path
from configs.config import tmp_dir
from spyrmsd import io, rmsd
from rdkit import Chem


class RMSDCalculator:
    _ref_lig = None

    def __init__(self):
        pass

    # callables
    def cache_reference(self, ref_lig):
        """
        cache reference ligand for efficiency
        :param ref_lig: reference ligand file
        :return:
        """
        self._ref_lig = io.loadmol(ref_lig)

    def calc_rmsd(self, ligands, ref_ligand, method, minimize):
        """
        rmsd calculation
        :param ligands: ligand file
        :param ref_ligand:
        :param method: {standard|symmetric}
        :param minimize: calculate minimized RMSD
        :return:
        """
        if method not in ["standard", "hungarian", "symmetric"]:
            raise(Exception("Method should be standard|hungarian|symmetric"))
        if ref_ligand is None:
            ref_lig = self._ref_lig
        else:
            ref_lig = io.loadmol(ref_ligand)
        if ref_lig is None:
            raise(Exception("Reference ligand missing"))

        ligs = io.loadallmols(ligands)

        # remove Hs
        ref_lig.strip()
        for lig in ligs:
            lig.strip()

        ref_coords = ref_lig.coordinates
        ref_atomic_num = ref_lig.atomicnums

        ligs_coords = [lig.coordinates for lig in ligs]
        lig0_atomic_num = ligs[0].atomicnums

        if method == "symmetric":
            ref_adj_mat = ref_lig.adjacency_matrix
            lig0_adj_mat = ligs[0].adjacency_matrix
            ret = rmsd.symmrmsd(ref_coords,
                                ligs_coords,
                                ref_atomic_num,
                                lig0_atomic_num,
                                ref_adj_mat,
                                lig0_adj_mat,
                                minimize=minimize)
        elif method == "hungarian":
            ret = []
            for lig_coords in ligs_coords:
                ret.append(rmsd.hrmsd(ref_coords,
                                      lig_coords,
                                      ref_atomic_num,
                                      lig0_atomic_num,
                                      center=False))
        else:
            ret = []
            for lig_coords in ligs_coords:
                ret.append(rmsd.rmsd(ref_coords,
                                     lig_coords,
                                     ref_atomic_num,
                                     lig0_atomic_num,
                                     center=False,
                                     minimize=minimize,
                                     atol=1e-9))
        return ret


if __name__ == '__main__':
    rmsd_calculator = RMSDCalculator()
    rmsd_calculator.cache_reference(os.path.join(tmp_dir, "dock", "1bcu_ligand.sdf"))
    rmsd = rmsd_calculator.calc_rmsd(os.path.join(tmp_dir, "dock", "1bcu.sdf"), None, "hungarian", False)
    print(rmsd)
