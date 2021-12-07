with open('Lista.txt','rt') as f:
    l=list(f)

n=media=0
for i in l:
    x=i.split()
    nota=int(x[2])
    n, media= n+1, media+nota
    if x[3]=='1':
        f=open("Gr1.txt","a")
        f.write(i)
        f.close()
    else:
        f=open("Gr2.txt","a")
        f.write(i)
        f.close()
med=round((media/float(n)),2)

f=open("Media.txt","w")
f.write('Media clasei: ')
f.write(str(med))
f.close()

