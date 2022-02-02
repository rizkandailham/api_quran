import requests
import numpy as np
import json
import csv

data=requests.get("https://equran.id/api/surat")
data=json.loads(data.text)
#konversi ke array
#data=np.array(data)
jumlah_surat=0
jumlah_ayat=0
header=["Nomor","Nama Surat"]
with open('surat.csv', 'w', encoding='UTF8') as f:
    tulis=csv.writer(f)
    tulis.writerow(header)
    for i in data:
            isi=[i['nomor'],i['nama_latin']]
            tulis.writerow(isi)

#for i in data:
#    print(str(i["nomor"])+":"+i["nama_latin"])
