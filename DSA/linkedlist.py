class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist():
    def __init__(self):
        self.head=None
    def insertAtBegin(self,data):
        node=Node(data,self.head)
        self.head=node
    def insertAtEnd(self,data):
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(data,None)
    def insert(self,index,data):
        length=self.display()
        if(index>length-1):
            raise Exception("invalid index positon")
        if(index==0):
            self.insertAtBegin(data)
        itr=self.head
        count=0
        while(itr):
            if(count==index-1):
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count=count+1
    def deleteAtBegin(self):
        if(self.head):
            self.head=self.head.next
    def deleteAtEnd(self):
        itr=self.head
        count=1
        length=self.display()
        while(itr):
            if(count==length-1):
                itr.next=None
                break
            itr=itr.next
            count=count+1
    def remove(self,index):
        length=self.display()
        if(index>length-1):
            raise Exception("invalid index positon")
        if(index==0):
            self.deleteAtBegin()
        itr=self.head
        count=0
        while(itr):
            if(count==index-1):
                itr.next=itr.next.next
                break
            itr=itr.next
            count=count+1
    def display(self):
        itr=self.head
        count=0
        while(itr):
            count=count+1
            #print(itr.data)
            itr=itr.next
        return count
    def seeElemets(self):
        itr=self.head
        count=0
        while(itr):
            count=count+1
            print(itr.data)
            itr=itr.next
ll=linkedlist()
ll.insertAtBegin(20)
ll.insertAtBegin(7)
ll.insertAtBegin(30)
ll.insertAtEnd(100)
ll.insertAtEnd(200)
ll.deleteAtEnd()
ll.insert(3,1000)
ll.remove(3)
ll.seeElemets()





