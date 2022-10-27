"""
platform: any
env: any with rdkit
name: testRDKit.py
tester of RDKit functionality
"""
import os

from rdkit import Chem
from configs.config import aug_dir


def testReadMol():
    for lig in os.listdir(aug_dir["ligands"]):
        lig_base = os.path.join(aug_dir["ligands"], lig)
        n = int(len(os.listdir(lig_base))/4)
        for i in range(n):
            molpath = os.path.join(lig_base, "{}_ledock001.sdf".format(i+1))
            mol = Chem.MolFromMolFile(molpath, removeHs=True)
            Chem.AssignStereochemistryFrom3D(mol)


if __name__ == '__main__':
    testReadMol()
