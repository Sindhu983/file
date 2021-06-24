file=open("question4.txt","r")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("others.txt","w")
c=(file.read())
d=c.split("\n")
i=0
while i<len(d):
    if "delhi" in d[i]:
        file1.write(d[i])
        file1.write("\n")

    elif "shimla" in d[i]:
        file2.write(d[i])
        file2.write("\n")
    else:
        file3.write(d[i])
        file3.write("\n")
    i+=1
file.close()






