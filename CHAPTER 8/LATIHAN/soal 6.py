#sortStringByChar

def sortStringByChar(data) :
    data.sort(reverse=True)
    return data

mydata = ['apel', 'rambutan', 'jeruk']
dataSort = sortStringByChar(mydata)

print("Data baru diurutkan dari jumlah karakter terbanyak ke terkecil: ",dataSort)
