a=0
b=100

jumlah=0
total=0

for bil in range(a,b):
    if bil % 2 == 1 :
        print (bil);
    jumlah = int((bil/2)+1)
    total = int(jumlah/2*(b))

print()
print("Banyak nya bilangan ganjil: ", jumlah)
print("Jumlah bilangan ganjil    : ", total)
