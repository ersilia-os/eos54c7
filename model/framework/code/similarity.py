from bs4 import BeautifulSoup
import requests
import json
import sys

fp        = 'ECFP4'
maxCount  = '100'
maxDist   = '20'


def zinc_100_closest(smiles_list):
    data = []
    for input_smiles in smiles_list:
        input_smiles = input_smiles.strip() 
        url = 'https://multi-fpb.gdb.tools/MCSS/search.jsp?maxCount=' + maxCount + '&type=numOfMols&maxDist=' + maxDist + '&group1=Princeton&group1=Enamine&group1=Otava&group1=Vitas-M&group1=Specs&group1=Urosy&group1=ChemDiv&group1=ChemBridge&group1=Others&pdbID=&mask=0&smi=' + input_smiles + '&fp=' + fp + '&searchMethod=searchByNum&searchLimit=100&retBooleans=false%3Bfalse%3Bfalse%3Bfalse%3Bfalse%3Bfalse&retVals=0%3B0%3B0%3B0%3B0%3B0&formulaCheck=null&PDB_LIGANDS=&PDB_LIGANDS_smi='
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features = 'html.parser')
        results = soup.find_all('textarea')
        
        T = str(results[0]).splitlines() if results else []
        T = [i for i in T if not ('ZINC' not in i)]
        smiles_list = []
        for i in T:
            x = i.split(" ZINC")[0]
            smiles_list.append(x) 
        data+= [smiles_list]
    return data



