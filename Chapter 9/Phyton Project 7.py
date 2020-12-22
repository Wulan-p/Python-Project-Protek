mhs=['K001:ROSIHAN ARI:1979-09-01:SOLO',
     'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
     'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

listupgrade=[]

for x in range(len(mhs)):
    i=mhs[x].split(':')
    listupgrade.append(i)

    j=listupgrade[x][2].split('-')
    j.reverse()
    
    jgab='/'.join(j)
    listupgrade[x][2] = jgab

print('=' * 65)
print('NIM'.ljust(11),'NAMA MAHASISWA'.ljust(22),'TGL LAHIR'.ljust(17),'TEMPAT LAHIR'.ljust(20))
print('-' * 65)

for i in range(len(listupgrade)):
    print(listupgrade[x][0].ljust(11),listupgrade[x][1].ljust(22),listupgrade[x][2].ljust(17),listupgrade[x][3].ljust(20))
print('-'*65)
