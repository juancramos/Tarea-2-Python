import sys, string, os, array

print "This program runs with the following arguments:", sys.argv
n_args = len(sys.argv)

for i in range(n_args):
    print sys.argv[i]
    print i

path = sys.argv[1]

# read the file
infile = open(path, 'r')

#load the full text by lines

text = infile.read(1)

ar = []
i = 0

while text!='':
    if ar.count(text)==0:
        ar.append(text)
    else:
        i = ar.index(text)
        ar.insert(i+1,text)
    text = infile.read(1)

contar = 0
letra = ar[0]
conteo = []
i=0
while i<len(ar):
    if letra == ar[i]:
        contar=contar+1
    else:
        conteo.append([contar,letra])
        letra=ar[i]
        contar=0
        i=i-1
    i=i+1

conteo.append([contar,letra])

for x in range(1,len(conteo)):
    for y in range(len(conteo) - x  ):
        if conteo[y][0]<conteo[y+1][0]:
            temp = conteo[y]
            conteo[y]=conteo[y+1]
            conteo[y+1]=temp

fileOut = open('frecuencias_'+path, 'w')
fileOut.write('[Cantidad , caracter] \n')

for pos in (range(len(conteo))):
    fileOut.write(str(conteo[pos])+'\n')

fileOut.close()
print conteo

infile.close()
