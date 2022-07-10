string="tacocat"
new=''
for i in string.split():
    new+=i[::-1]+' '
    
print(new)
