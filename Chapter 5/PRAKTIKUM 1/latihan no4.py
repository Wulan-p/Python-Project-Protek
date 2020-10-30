#MARI MENGHITUNG
kode=int(input("Masukkan kode karyawan: "))
nama=input("Masukkan nama karyawan: ")
gol =input("Masukkan golongan     : ")


print ("\n=======================================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("\n---------------------------------------")
print("Nama Karyawan        : ", nama)
print("Golongan             : ", gol)
print ("\n---------------------------------------")

if gol == "C":
    print("Gaji Pokok           :Rp. 7000000")
    print("Potongan ( 1.5 %)    :Rp. 105000")
    print ("\n--------------------------------------- -")
    print("Gaji Bersih          :Rp. 6895000")
if gol == "A":
    print("Gaji Pokok           :Rp. 10000000")
    print("Potongan ( 2.5 %)    :Rp. 250000")
    print ("\n--------------------------------------- -")
    print("Gaji Bersih          :Rp. 9750000")
if gol == "B":
    print("Gaji Pokok           :Rp. 8500000")
    print("Potongan ( 2.0 %)    :Rp 170000")
    print ("\n--------------------------------------- -")
    print("Gaji Bersih          :Rp. 8330000")
if gol == "D":
    print("Gaji Pokok           :Rp. 5500000")
    print("Potongan ( 1.0 %)    :Rp 55000")
    print ("\n--------------------------------------- -")
    print("Gaji Bersih          :Rp. 5445000")
