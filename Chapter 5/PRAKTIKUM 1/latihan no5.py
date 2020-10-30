#MARI MENGHITUNG
kode=int(input("Masukkan kode karyawan: "))
nama=input("Masukkan nama karyawan: ")
gol =input("Masukkan golongan     : ")
stat=input("Masukkan status       :")
if stat=='1':
    anak=input("Masukkan jumlah anak  :")


#math.import
if gol== 'C':
    gajpok=7000000
    tuj_i=10/100*gajpok
    if stat=='1':
        tuj_a=5/100*gajpok
    persen=1.5
    pot=1.5/100*gajpok
    if stat=='1':
        gajkot=gajpok+tuj_i+tuj_a
    else:
        gajkot=gajpok
    gajber=gajkot-pot
   
elif gol == "A":
    gajpok=10000000
    tuj_i=10/100*gajpok
    if stat=='1':
        tuj_a=5/100*gajpok
    persen=2.5
    pot=2.5/100*gajpok
    if stat=='1':
        gajkot=gajpok+tuj_i+tuj_a
    else:
        gajkot=gajpok
    gajber=gajkot-pot

elif gol== 'B':
    gajpok=8500000
    tuj_i=10/100*gajpok
    if stat=='1':
        tuj_a=5/100*gajpok
    persen=2.0
    pot=2.0/100*gajpok
    if stat=='1':
        gajkot=gajpok+tuj_i+tuj_a
    else:
        gajkot=gajpok
    gajber=gajkot-pot
   
elif gol == "D":
    gajpok=5500000
    tuj_i=10/100*gajpok
    if stat=='1':
        tuj_a=5/100*gajpok
    persen=1.0
    pot=1.0/100*gajpok
    if stat=='1':
        gajkot=gajpok+tuj_i+tuj_a
    else:
        gajkot=gajpok
    gajber=gajkot-pot

print ("\n=======================================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("\n---------------------------------------")
print("Nama Karyawan        : ",nama)
print("Golongan             : ",gol)
print("Status Menikah       : ",stat)
if stat=='1':
    print("Jumlah anak          : ",anak)

print ("\n---------------------------------------")

print("Gaji Pokok           : ",gajpok)
if stat=='1':
    print("Tunjangan Istri/Suami: ",tuj_i)
    print("Tunjangan Anak       : ",tuj_a)

print ("\n--------------------------------------- +")

print("Gaji Kotor           : ",gajkot)
print("Potongan(",persen," %)    : ",pot)

print ("\n--------------------------------------- -")

print("Gaji Bersih          : ",gajber)
