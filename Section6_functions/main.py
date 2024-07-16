# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1,l2):
        list=[]
        for i in range(len(l1),0,-1):
            node1=l1[i]
            for j in range(len(l2),0,-1):
                node2=l2[j]
            if i==j:
                list.append(node1+node2)
        





#answer=Solution.addTwoNumbers(l1=[2,4,3], l2=[5,6,4])#answer=[7,0,8]
#print(answer)

l1 = [2,4,3]
l2= [5,6,4]
for i in range(len(l1),0,-1):
    print (i)


#test1=[::-1] in [2,4,3]
#print([])
