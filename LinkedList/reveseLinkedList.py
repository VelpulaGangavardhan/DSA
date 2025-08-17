'''
Reverse a Linked List 
Example: 
Input: 1 -> 2 -> 3 -> 4 -> 5 
Output: 5 -> 4 -> 3 -> 2 -> 1
TC=O(N)
SC=O(1)
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=Node(data)
    def diplay(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("Null")
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
        
s=Single()
for i in [2,3,5,7,5]:
    s.insert(i)
s.diplay()
s.reverse()
s.diplay()
