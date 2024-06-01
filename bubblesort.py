a=[25,41,2,98,18,35,29,11,22,100]
n=len(a)
k=n
for j in  range(k):
    for i in range(1,n):
        temp=a[i-1]
        if temp>a[i]:
            a[i-1]=a[i]
            a[i]=temp
    n-=1
print(a)        