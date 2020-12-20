#mengetahui data terbesar menggunakan dictionary

def buahMahal(dictionary):
    key=list(dictionary.keys())
    values=tuple(dictionary.values())
    harga_termahal=max(values)
    index=values.index(harga_termahal)
    print(key[index])

buah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}
buahMahal(buah)
