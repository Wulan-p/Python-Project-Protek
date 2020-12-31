file=open('fileDataMhs.txt','r')
searchNIM=input("Masukkan NIM yang mau dicari : ")
line = file.readlines()

for i in range(len(line)):
    y=line[i].split('|')

    if(searchNIM in line[i]):
        status='ada'
        print("Data Mahasiswa ")
        print("NIM    : ",y[0])
        print("Nama   : ",y[1])
        print("Alamat : ",y[2])
        break
    else:
        status='tidak ada'
if (status=='tidak ada'):
    print("Data Mahasiswa Tidak Ditemukan")
file.close()
