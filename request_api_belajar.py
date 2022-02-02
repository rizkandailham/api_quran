#import library yg diperlukan
import requests
import numpy as np
from numpy import array

#bagian request ke api
r= requests.get('https://equran.id/api/surat/1')

#cek response
r.status_code
r.headers['content-type']
r.encoding
r.text
#convert response ke json array
arr=r.text
arr=json.loads(arr)

#akses ke array
arr['status']
arr['nomor']
arr['surat']
