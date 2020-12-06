#CHAPTER 08
#LANGKAH LERJA

#NO 1
a=[1,5,6,3,6,9,11,20,12]
b=[7,4,5,6,7,1,12,5,9]
print(a)
print(b)
print( )

#NO 2
a.insert(3,10)
b.insert(2,15)
print(a)
print(b)
print( )

#NO 3
a.append(4)
b.append(8)
print(a)
print(b)
print( )

#NO 4
a.sort()
b.sort()
print(a)
print(b)
print( )

#NO 5
c=a[0:8]
d=b[2:10]
print(c)
print(d)
print( )

#NO 6
e=[]
for i in range(len(c)):
    element=c[i] + d[i]
    e.append(element)    
print(e)
print()

#NO 7
Tuple=tuple(e)

#NO 8
min_e=min(Tuple)
max_e=max(Tuple)
sum_e=sum(Tuple)
print(min_e)
print(max_e)
print(sum_e)
print( )

#NO 9
myString="python adalah bahasa pemrograman yang menyenangkan"

#NO 10
huruf=set(myString)
print(myString)
print( )

#NO 11
listHuruf=list(huruf)
listHuruf.sort()
print(listHuruf)
