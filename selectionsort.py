a=[22,11,35,29,356,42,57,100,68,1]
n=len(a)-1
m=0

for j in  range(n):
    k=n
    for i in range(n):
        if a[i]>a[k]:
            k=i
    if k!=n:
        temp=a[k]
        a[k]=a[n]
        a[n]=temp
    n-=1
print(a) 
    
        

       



