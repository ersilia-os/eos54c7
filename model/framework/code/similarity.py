from bs4 import BeautifulSoup
import requests
import urllib
import time

fp        = 'ECFP4'
maxCount  = '100'
maxDist   = '20'


def zinc_100_closest(smiles_list):
    data = []
    for input_smiles in smiles_list:
        input_smiles = input_smiles.strip() 
        url_encoded_smiles = urllib.parse.quote(input_smiles)
        url = "https://multi-fpb.gdb.tools/pfpZinc.NoJava/search.jsp?maxCount="+maxCount+ "&type=numOfMols&maxDist="+maxDist+ "&group2=None&inputMol=&mask=0&smi="+url_encoded_smiles+ "&searchMode=searchByNum&limit=100"
        print(url)
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
        time.sleep(6)
    return data



