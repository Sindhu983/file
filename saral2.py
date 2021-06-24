file=open("saral1.txt")
c=file.readlines()
new=[]
i=1
while i<len(c):
    new.append(c[i])
    i+=1
print(new)
file.close()