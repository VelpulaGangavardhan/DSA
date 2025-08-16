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
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
    def removeNthEndNode(self,n):
        if n<=0:
            return
        lenght=0
        temp=self.head
        while temp:
            lenght+=1
            temp=temp.next
        if n>lenght:
            return
        if n==lenght:
            temp=self.head
            self.head=temp.next
            return
        removeNode=lenght-n
        temp=self.head
        for i in range(removeNode-1):
            temp=temp.next
        temp.next=temp.next.next
        
s=Single()
for i in [1,2,3,4,5]:
    s.insert(i)
s.display()
s.removeNthEndNode(8)
s.display()
        