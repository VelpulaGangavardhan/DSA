'''
Find the Intersection Point of Two Linked Lists 
o Example: 
Input: 
List A: 4 -> 1 -> 8 -> 4 -> 5,
List B: 5 -> 0 -> 1 -> 8 - > 4 -> 5 
Output: 8 
TC=O(n+m)
SC=O(1)
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single:
    def insert(self,head,data):
        if head is None:
            return Node(data)
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)
        return head
    def display(self,head):
        temp=head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
    def insertSectionPoint(self,h1,h2):
        t1=h1
        t2=h2
        while t1 != t2:
            if t1 is None:
                t1=h2
            else:
                t1=t1.next
            if t2 is None:
                t2=h1
            else:
                t2=t2.next
        if t1 :
            return t1.data
        else:
            return None
        

a=[4,1,8,4,5]
b=[5,0,9]
A=None
B=None
s=Single()
for i in a:
    A=s.insert(A,i)
for i in b:
    B=s.insert(B,i)
tempa=A
while tempa and tempa.data !=8:
    tempa=tempa.next
tempb=B
while tempb.next:
    tempb=tempb.next
tempb.next=tempa

s.display(A)
s.display(B)
print(s.insertSectionPoint(A,B))