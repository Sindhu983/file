file=open("alternate.txt","r")
c=file.readlines()
countlines=0
i=0
while i<len(c):
    countlines+=1
    i+=1
print(countlines)
file.close()




