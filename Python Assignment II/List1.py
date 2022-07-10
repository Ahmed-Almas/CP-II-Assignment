l=[]
length=int(input("Enter list size :"))
for i in range(0,length):
    e=int(input("Enter element :"))
    l.append(e)
l[0],l[length-1]=l[length-1],l[0]
print(l)
    