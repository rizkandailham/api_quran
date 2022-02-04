import pandas as pd

def cek_isi():
    data=pd.read_excel('TABEL7_2.xls', index_col=5)
    df=pd.DataFrame(data, columns=['LAPANGAN USAHA'])
    print(df)
cek_isi()
