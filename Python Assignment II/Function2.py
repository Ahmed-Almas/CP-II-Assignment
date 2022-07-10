#q48
def power(num,expo):
    if expo==0:
        return 1
    else:
        return num*power(num,expo-1)
    
n=int(input("Enter a number :"))
p=int(input("Enter its power :"))
print(power(n,p))