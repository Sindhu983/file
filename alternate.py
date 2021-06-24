import random
def read_random_line():
    file=open("alternate.txt","r")
    c=file.readlines()
    length=len(c)
    r1=random.randint(0,length-1)
    print(c[r1])
    file.close()
read_random_line()