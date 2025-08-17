'''
Merge Two Sorted Linked Lists 
Example: 
Input: 1 -> 2 -> 4, 1 -> 3 -> 4 
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 
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
        else:
            temp=head
            while temp.next:
                temp=temp.next
            temp.next=Node(data)
            return head
    def display(self,head):
        temp=head
        while temp:
            print(temp.data,end='-->')
            temp=temp.next
        print("None")
    def merge(self,h1,h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        dup=Node(0)
        tail=dup
        while h1 and h2:
            if h1.data<=h2.data:
                tail.next=h1
                h1=h1.next
            else:
                tail.next=h2
                h2=h2.next
            tail=tail.next
        if h1:
            tail.next=h1
        if h2:
            tail.next=h2
        return dup.next
                    
                    
            
s=Single()
h1=None
h2=None
for i in range(1,5):
    h1=s.insert(h1,i)
for i in range(1,6):
    h2=s.insert(h2,i)
s.display(h1)
s.display(h2)
m=s.merge(h1,h2)
s.display(m)
    
            
