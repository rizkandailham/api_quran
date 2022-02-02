import requests
import numpy as np
import json

data=requests.get("https://equran.id/api/surat")
data=json.loads(data.text)
#konversi ke array
#data=np.array(data)
jumlah_surat=0
jumlah_ayat=0
for i in data:
    print(str(i["nomor"])+":"+i["nama_latin"])
