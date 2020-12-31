file=open('fileDataMhs.txt','r')
line=file.readlines()
datamhs={}

for i in range(len(line)):
    a=line[i].split('|')
    a[2]=a[2].replace('\n','')
    
    datamhs[i]={'nim':a[0],'nama':a[1],'alamat':a[2]}

print(datamhs)
