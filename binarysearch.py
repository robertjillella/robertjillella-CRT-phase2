a=list(map(int,input().split('')))
num=int(input())
l=0
r=len(a)-1
count=0
while l<=r:
    mid=(l+r)//2
    if a[mid]==num:
        count=num
        break
    elif a[mid]>num:
        r=mid-1
    else:
        l=mid+1
if count==0:
    print('sorry not found')
else:
    print('ur value at location',count)