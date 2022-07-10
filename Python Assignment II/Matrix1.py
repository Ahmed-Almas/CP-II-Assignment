l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
l3=[[0,0,0],[0,0,0],[0,0,0]]
l4=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        l3[i][j]=l1[i][j]+l2[i][j]
        
for i in range(0,3):
    for j in range(0,3):
        l4[i][j]=l1[i][j]-l2[i][j]

for i in range(0,3):
    print(l3[i])
print('\n')
for i in range(0,3):
    print(l4[i])
