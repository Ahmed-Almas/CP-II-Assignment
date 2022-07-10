#q43
import itertools as it
l=[1, 3, 5, 1, 3, 2, 5, 4, 2]
l2=[]
res=[list(val) for key, val in it.groupby(sorted(l))] 
print(res)
