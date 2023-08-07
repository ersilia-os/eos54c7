from bs4 import BeautifulSoup
import requests
import json
import sys

# Input Parameters
input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()[1:]

fp        = 'ECFP4'
maxCount  = '100'
maxDist   = '20'

data = []
for input_smiles in Lines:
    input_smiles = input_smiles.strip() 
    url = 'http://130.92.106.217:8080/MCSS/search.jsp?maxCount=' + maxCount + '&type=numOfMols&maxDist=' + maxDist + '&group1=Princeton&group1=Enamine&group1=Otava&group1=Vitas-M&group1=Specs&group1=Urosy&group1=ChemDiv&group1=ChemBridge&group1=Others&pdbID=&mask=0&smi=' + input_smiles + '&fp=' + fp + '&searchMethod=searchByNum&searchLimit=100&retBooleans=false%3Bfalse%3Bfalse%3Bfalse%3Bfalse%3Bfalse&retVals=0%3B0%3B0%3B0%3B0%3B0&formulaCheck=null&PDB_LIGANDS=&PDB_LIGANDS_smi='

    r = requests.get(url)
    soup = BeautifulSoup(r.text, features = 'html.parser')
    results = soup.find_all('textarea')
    
    T = str(results[2]).splitlines()
    T = [i for i in T if not ('ZINC' not in i)]
    smiles_list = []
    similarity_indices = []
    for i in T:
        x = i.split(" ZINC")[0]
        x2 = i.split(" ")[2]
        smiles_list.append(x) 
        similarity_indices.append(x2)
        
    data+= [[smiles_list, similarity_indices]]

with open(sys.argv[2], 'w') as f:
    json.dump(data, f)
