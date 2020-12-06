#mengurutkan data dari yg terbesar-terkecil
#descending

while True:
    try:
        n=int(input("Banyak data yang akan di input : "))
        break
    except ValueError:
        print("Input invalid")
        continue
data=[]

a=0
while (a<n):
    try:
        bil=int(input("Masukkan bilangan bulat : "))
        data.append(bil)
        a+=1
    except ValueError:
        print("Input invalid")
        
data.sort(reverse = True)
print("Urutan dari yang terbesar ke terkecil adalah", data)
