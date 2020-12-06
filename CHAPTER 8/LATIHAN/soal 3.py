#menyusun data scr urut
#ascending

data=[]
n=True
while(n==True):
    nama=input("Masukkan Nama Mahasiswa : ")
    data.append(nama)
    datamhswa=input("Ingin menginput nama lagi (YA/TIDAK) : ")
    if(datamhswa=="YA"):
        n=True   
    elif(datamhswa=="TIDAK"):
        n=False
    else:
        print("Input invalid")
        break
print()
data.sort()

for x in range(len(data)):
    print(data[x], '(', len(data[x]), 'karakter )')
