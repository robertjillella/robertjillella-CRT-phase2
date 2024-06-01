#coding blocks IDE
#class student:
 #   def __init__(self,name,rollnumber,javamarks,pythonmarks,mathsmarks):
  #      self.name=name
   #     self.rollnumber=rollnumber
    #    self.javamarks=javamarks
    #    self.pythonmarks=pythonmarks
    #    self.mathsmarks=mathsmarks        

#obj1=student("robert",451,65,75,85)
#obj2=student("raghu",452,65,60,70)
#j3=student("sudheer",453,85,75,55)
#print(obj2.name)
#print(obj2.rollnumber)
#print(obj2.javamarks)
#print(obj2.pythonmarks)
#print(obj2.mathsmarks)

#def printalldetails(self):
    #print(self.name)
    #print(self.rollnumber)
    #print(self.javamarks)
    #print(self.pythonmarks)
    #print(self.mathsmarks)
    
#obj=student("raghu",520,55,65,75)
#obj.printalldetails()

#obj=student("raghu lvr",521,75,85,65)   
#
# obj.printalldetails()      


#https://pastebin.com/qK8im4Kx
    
#class Node:
    #def __init__(self, data):
        #self.data = data 
        #self.next = None 
 
# Object creation is happening      
#obj1 = Node(10)
#Obj2 = Node(20)
#obj3 = Node(30)
#obj4 = Node(40)
#obj5 = Node(50) 
 
# Links establishing in below lines 
#obj1.next = obj2 
#obj2.next = obj3
#obj3.next = obj4 
#obj4.next = obj5 
 
# print linked list 
#10 --> 20 --> 30 --> 40 --> None
 
#currentNode = obj1 
#while currentNode != None:
 #   print(currentNode.data, end = " --> ")
  #  currentNode = currentNode.next 
 
#class Node:
    #def __init__(self, data):
       # self.data = data 
        #self.next = None 
 
#def printLinkedList(head):
    #currentNode = head 
    #while currentNode != None:
        #print(currentNode.data, end = " --> ")
        #currentNode = currentNode.next
    #print()
 
#def insertAtTail(head, ele):
    #temp = Node(ele)
    #if head == None:
        #return temp
 
    #tail = head 
    #while tail.next != None:
        #tail = tail.next '..............
        
    #tail.next = temp 
    #return head

 
 
#nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#head = None 
#for ele in nums:
  #  head = insertAtTail(head, ele)
   # printLinkedList(head)
#print("Final linked list is:")
#printLinkedList(head)

#def push(stack,ele):
 #   stack.append(ele)
   # print(ele,"inserted into stack successfully")
#def pop(stack):
   # if len(stack)==0:
    #    print("stack is empty")
    #    return
   # print(stack[-1],"deleted succcessfully")
    #stack.pop()
    
#stack=[]
#push(stack,10)
#push(stack,20)
#push(stack,30)
#push(stack,40)
#push(stack,50)

#pop(stack)
#pop(stack)

# def enQueue(Q,ele):
#     Q.append(ele)
#     print(ele,"inserted into Queue")

# def deQueue(Q):
#     if len(Q)==0:
#         print("Queue is empty")
#         return
#     print(Q[0],"is getting deleted")
#     Q.pop(0)
    
# Q=[]
# enQueue(Q,10)
# enQueue(Q,20)
# enQueue(Q,30)
# enQueue(Q,40)
# enQueue(Q,50)
# deQueue(Q)
# deQueue(Q)        
        
# def isBalanced(word):
#     stack = []
#     for ele in word:
#         if ele == '(':
#             stack.append(ele)
#         else:
#             if len(stack) == 0:
#                 return False 
#             else:
#                 stack.pop()
#     if len(stack) == 0:
#         return True 
#     return False
 
 
# word = "()("
# word = input()
# result = isBalanced(word)
# print(result)
        
# class Solution(object):
#     def isValid(self, s):
#         stack = []
#         openBrackets = ["(", "{", "["]
#         for ele in s:
#             if ele in openBrackets:
#                 stack.append(ele)
#             else:
#                 if len(stack) == 0:
#                     return False 
#                 elif ele == ')':
#                     if stack[-1] == '(':
#                         stack.pop()
#                     else:
#                         return False
#                 elif ele == ']':
#                     if stack[-1] == '[':
#                         stack.pop()
#                     else:
#                         return False
#                 elif ele == '}':
#                     if stack[-1] == '{':
#                         stack.pop()
#                     else:
#                         return False
#         if len(stack) == 0:
#             return True 
#         return False
#LINEAR SEARCH
# nums=[12,10,6,23,123]
# target=6
# flag=-1
# n=len(nums)
# for index in range(n):
#     if nums[index]==target:
#         flag=index
#         break
# if flag =="-1":
##     print("not found")
# else:
#     print("target found at:",flag)
#BINARY SEARCH
# nums=[12,10,6,23,123]
# target=6
# numberszzzææææææ
# flag=-1
# n=len(nums)
# for index in range(n):
#     if nums[index]==target:
#         flag=index
#         break
# if flag =="-1":
#     print("not found")
# else:
#     print("target found at:",flag)

# def performBubbleSort(nums):
#     n=len(nums)
#     fixThisIndex=n-1
    
#     while fixThisIndex>0:
#         for index in range (fixThisIndex):
#             if nums[index]>nums[index+1]:
#                 temp=nums[index]
#                 nums[index]=nums[index+1]
#                 nums[index+1]=temp
#         print(nums)
#         fixThisIndex-=1
        
# nums=[10,8,2,14,12,7]
# print("Before sorting:",nums)
# performBubbleSort(nums)
# print("print sorting:",nums)

# def performSelectionSort(nums):
#     n=len(nums)
#     fixThisIndex=n-1
    
#     while fixThisIndex>0:
#         maxEleIndex=fixThisIndex
        
#         for index in range (fixThisIndex):
#             if nums[index]>nums[maxEleIndex+1]:
#                 maxEleIndex=index
#         if maxEleIndex!=fixThisIndex:
#             temp=nums[fixThisIndex]
#             nums[fixThisIndex]=nums[fixThisIndex+1]
#             nums[fixThisIndex+1]=temp
#         print(nums)
#         fixThisIndex-=1
        
# nums=[10,8,2,14,12,7]
# print("Before sorting:",nums)
# performSelectionSort(nums)
# print("print sorting:",nums)0

# def mergetwoSubarrays(nums,left,mid,right):
#     temp=[]
#     index1=left
#     index2=mid+1
#     while index1<=mid and index2<=right:
#         if nums[index1]<nums[index2]:           
#             temp.append(nums[index1])
#             index1+=1
#         else:
#             temp.append(nums[index2])
#             index2+=1
#     while index1<=mid:
#         temp.append(nums[index1])
#         index1+=1
#     while index2<=mid:
#         temp.append(nums[index2])
#         index2+=1

# class Node:
#     def __init__(self, data):
#         self.data = data 
#         self.left = None 
#         self.right = None
 
 
# def printPreorder(root):
#     if root == None:
#         return 
#     # 1 
#     print(root.data, end = ", ")
#     # 2 
#     printPreorder(root.left)
#     # 3
#     printPreorder(root.right)
 
 
# def printInorder(root):
#     if root == None:
#         return 
#     # 1 
#     printInorder(root.left)
#     # 2 
#     print(root.data, end = ", ")
#     # 3
#     printInorder(root.right)
 
# def printPostorder(root):
#     if root == None:
#         return 
#     # 1 
#     printPostorder(root.left)
#     # 2 
#     printPostorder(root.right)
#     # 3
#     print(root.data, end = ", ")
 
 
 
 
#https://pastebin.com/ugJvxcbL  
 
 
 
# class Solution(object):
#     def maxLevelSum(self, root):
#         if root == None:
#             return 0
#         Q = [root]
#         resultLevel = 0 
#         resultSum = -100000000
#         currLevel = 1
#         while len(Q) > 0:
#             n = len(Q)
#             currSum = 0
#             for i in range(n):
#                 # step-1 (Deleting)
#                 currNode = Q.pop(0)
 
#                 # step-2 (Appending to subResult)
#                 currSum += currNode.val
 
#                 # step-3 (Enquing the left child)
#                 if currNode.left != None:
#                     Q.append(currNode.left)
 
#                 # step-4 (Enquing the right child)
#                 if currNode.right != None:
#                     Q.append(currNode.right)
 
#             if currSum > resultSum:
#                 resultSum = currSum 
#                 resultLevel = currLevel 
#             currLevel += 1
#         return resultLevel 
 
 
# def printLevelOrderTraversal(root):
#     if root == None:
#         return 
#     Q = [root]
#     result = []
#     while len(Q) > 0:
#         n = len(Q)
#         subResult = []
#         for i in range(n):
#             # step-1 (Deleting)
#             currNode = Q.pop(0)
 
#             # step-2 (Appending to subResult)
#             subResult.append(currNode.data)
 
#             # step-3 (Enquing the left child)
#             if currNode.left != None:
#                 Q.append(currNode.left)
 
#             # step-4 (Enquing the right child)
#             if currNode.right != None:
#                 Q.append(currNode.right)
 
#         result.append(subResult)    
 
#     print(result)
 
# def printLeftView(root):
#      if root == None:
#         return
#      Q = [root]
#      result = []
#      while len(Q) > 0:
#         n = len(Q)
#         for i in range(n):
#             # step-1 (Deleting)
#             currNode = Q.pop(0)
 
#             # step-2 (Appending to result)
#             if i == 0:
#                 result.append(currNode.data)
 
#             # step-3 (Enquing the left child)
#             if currNode.left != None:
#                 Q.append(currNode.left)
 
#             # step-4 (Enquing the right child)
#             if currNode.right != None:
#                 Q.append(currNode.right)
 
#      print("Left view is:", result)
 
# def printRightView(root):
#      if root == None:
#         return 
#      Q = [root]
#      result = []
#      while len(Q) > 0:
#         n = len(Q)
#         for i in range(n):
#             # step-1 (Deleting)
#             currNode = Q.pop(0)
 
#             # step-2 (Appending to result)
#             if i == n - 1:
#                 result.append(currNode.data)
 
#             # step-3 (Enquing the left child)
#             if currNode.left != None:
#                 Q.append(currNode.left)
 
#             # step-4 (Enquing the right child)
#             if currNode.right != None:
#                 Q.append(currNode.right)
 
#      print("Right view is:", result)
 
# #      12 
# #     5  8 
# #   -1 2   89
# obj1 = Node(12)
# obj2 = Node(5)
# obj3 = Node(8)
# obj4 = Node(-1)
# obj5 = Node(2)
# obj6 = Node(89)
# obj1.left = obj2
# obj1.right = obj3 
# obj2.left = obj4
# obj2.right = obj5
# obj3.right = obj6
 
# # printPreorder(obj1)
# # print()
# # printInorder(obj1)
# # print()
# # printPostorder(obj1)
# # print()
 
# printLeftView(obj1)
# class solution(object):
#     def insertIntoBST(self,root,val):
#         if root ==None:
#             return TreeNode(val)
#         elif root.val>val:
#             root.left=self.insertIntoBST(root.left,val)
#         else:
#             root.right=self.insertIntoBST(root.right,val)
#         return root
    
# class TreeNode:
#     def __init__(self, data):
#         self.val = data 
#         self.left = None 
#         self.right = None
 
# def printInorder(root):
#     if root == None:
#         return 
#     # 1 
#     printInorder(root.left)
#     # 2 
#     print(root.val, end = ", ")
#     # 3
#     printInorder(root.right)
 
 
# def insertIntoBST(root, val):
#     if root == None:
#         return TreeNode(val)
#     elif root.val > val:
#         root.left = insertIntoBST(root.left, val)
#     else:
#         root.right = insertIntoBST(root.right, val)
#     return root
 
# nums = [10, 8, 12, 5, 23, 20]
# root = None
# for ele in nums:
#     root = insertIntoBST(root, ele)
# printInorder(root)
           
                   