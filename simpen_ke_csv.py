import requests
import numpy as np
import json
from numpy import array
import pandas as pd


#save ke csv
#teks=np.array(teks)
#print(teks['jumlah_ayat'])
#np.savetxt('surat al fatihah.csv',teks,delimiter=',')
class scrapper_api:
    def __init__():

    def konversi_dict(teks):
        teks=list(teks.items())
        teks=np.array(teks)
        return teks

    def ambil_isi(url):
        r=requests.get(url)
        teks=json.loads(r.text)
        tmp=[]
        for i in teks:
            tmp.append(teks[i])
        return tmp

    def lihat_index(url):
        r=requests.get(url)
        teks=json.loads(r.text)
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

#ambil_isi(teks)
