#2
i=0
while(i<10):
    print ('Hello World')
    i += 1

#4
i=0
while('n'):
    print ('Hello World')
    i += 1
    
#5
i=2
while(i<=20):
    print('Hello World')
    i += 2


#6
i=0
while True:
    print('Hello World')
    i+=1
    if (i>=10):
        break

#7
while True:
    print('Hello World')
    i+=1
    if (i>=n):
        break
#8
#kotak bintang ajaib
kolom=5
baris=5

i=0
while(i<baris):
    j=0
    while(j<kolom):
        print('*',end='')
        j+=1
    print('')
    i+=1

#10
kolom=5
baris=5

i=0
while i in range(5):
    j=0
    while (j<(i+1)):
        print('*', end='')
        j+=1
    print('')
    i+=1

#11
from random import randint
while True:
    bil=randint (0,10)
    print(bil)
    if bil == 5:
        break

#13
from random import randint
while True:
    bil=randint (0,10)
    print(bil)
    if bil == 5:
        break
