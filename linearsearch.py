a=list(map(int,input().split()))
num=int(input())
count=0
n=len(a)
for i in range(n):
    if num==a[i]:
        count=i
        continue

if count!=0:
    print(count)
else:
    print('sorry')