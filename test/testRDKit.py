"""
platform: any
env: any with rdkit
name: testRDKit.py
tester of RDKit functionality
"""
import os

from rdkit import Chem
from configs.config import aug_dir, platform_delimiter


def testReadMols():
    for lig in os.listdir(aug_dir["ligands"]):
        lig_base = os.path.join(aug_dir["ligands"], lig)
        n = int(len(os.listdir(lig_base))/5)
        for i in range(n):
            molpath = os.path.join(lig_base, "{}_ledock001.sdf".format(i+1))
            mol = Chem.MolFromMolFile(molpath, removeHs=True)
            Chem.AssignStereochemistryFrom3D(mol)


def testReadLigand(molpath):
    mol = Chem.MolFromMolFile(molpath, removeHs=True)
    print(mol is None)
    return mol


def testReadProtein(molpath):
    mol = Chem.MolFromPDBFile(molpath, removeHs=True)
    if mol is None:
        print(molpath.split(platform_delimiter)[-1].split(".")[0])
    return mol


def testReadLigandFromMol2(molpath):
    mol = Chem.MolFromMol2File(molpath, removeHs=True)
    print(mol is None)
    return mol


if __name__ == '__main__':
    # testReadLigand(os.path.join(aug_dir["ligands"], "1dis", "20_ledock001_babel.sdf"))
    # testReadLigandFromMol2(os.path.join(aug_dir["ligands"], "1dis", "20_ledock001.mol2"))
    # testReadProtein(os.path.join(aug_dir["proteins"], "1e3v.pdb"))
    for pocket in os.listdir(aug_dir["pockets"]):
        testReadProtein(os.path.join(aug_dir["pockets"], pocket))

