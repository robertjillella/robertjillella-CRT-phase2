class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def printing(head):
    a=head
    while a!=None:
        print(a.data,end='__')
        a=a.next
    print()

def linklist(head,ele):
    temp=node(ele)
    if temp==None:
        return temp
    tail=head
    while tail!=None:
        tail=tail.next
    tail.next=temp
    return head 

num=[2,7,8,8,5,4,11,444,35]
head=None
for i in num:
    head=linklist(head,i)
print(head)
    


