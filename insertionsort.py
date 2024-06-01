
num=[22, 11, 35, 29, 1, 42]
n=len(num)
lele=0
for i in range(1,n):
    temp=num[i]
    pre=lele

    while pre>=0 and num[pre]>temp:
        num[pre+1]=num[pre]
        pre-=1
        num[pre+1]=temp
    lele+=1
    print(num)