import requests
import numpy as np
import json
from numpy import array
import pandas as pd


#save ke csv
#teks=np.array(teks)
#print(teks['jumlah_ayat'])
#np.savetxt('surat al fatihah.csv',teks,delimiter=',')

def konversi_dict(teks):
    return array

def ambil_isi(teks):
    total_keterangan=[]
    for i in teks:
        print(teks[i])

def lihat_index(teks):
    bit_simpen=[]
    for i in teks:
        bit_simpen.append(i)
    print(*bit_simpen, sep="\n")

def simpan_ke_csv(url):
    r=requests.get(url)
    teks=r.text
    teks=json.loads(teks)
    data=list(teks.items())
    teks=np.array(data)
    df=pd.DataFrame(teks)
    df.to_csv("Daftar Surat.csv")
