l=[]
length=int(input("Enter list size :"))
for i in range(0,length):
    e=int(input("Enter element :"))
    l.append(e)
for i in l:
    if i%5==0:
        print(i)
    
