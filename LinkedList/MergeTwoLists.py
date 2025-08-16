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
        t1=h1
        t2=h2
        dup=Node(0)
        tail=dup
        while t1 and t2:
            if t1.data<t2.data:
                tail.next=Node(t1.data)
                t1=t1.next
            else:
                tail.next=Node(t2.data)
                t2=t2.next
            tail=tail.next
        if t1:
            tail.next=t1
        if t2:
            tail.next=t2
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
    
            