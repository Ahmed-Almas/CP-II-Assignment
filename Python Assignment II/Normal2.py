string=input("Enter the string :")
new=''
for i in string:
    if i not in ('!','@','#','$','%','&','*'):
        new+=i
print(new)

