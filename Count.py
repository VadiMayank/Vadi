f=open("abcc.py","r")
a=[]
a=f.read()
#print(a)
word=a.split(" ")
#rint(word)
for i in range(len(word)):
    if len(word[i])>=20:
        print(word[i])
    else:
        print("Words only less than 20")


