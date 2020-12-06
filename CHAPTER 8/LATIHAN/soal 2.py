#datastatistika

def dataStat(x):
    a= sum(x)/len(x)
    b= max(x)
    c= min(x)
    dataStatistika=[a,b,c]
    return dataStatistika

while True:
    try:
        n=int(input("Banyak data yang akan di Input : "))
        break
    except ValueError:
        print("Input Invalid")
        continue
data=[]

j=0
while (j<n):
    try:
        bil=int(input("Masukkan bilangan bulat : "))
        data.append(bil)
        j+=1
    except ValueError:
        print("Input invalid")

data_akhir = dataStat(data)
print(data_akhir)
