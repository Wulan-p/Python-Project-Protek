#function kuadrat

def kuadrat(bil):
    bilangan = []
    for i in range(len(bil)):
        n = bil[i]**2
        bilangan.append(n)
    return bilangan

#cth
bil = [2, 4, 5, 6]
hasil = kuadrat(bil)
print(hasil)
