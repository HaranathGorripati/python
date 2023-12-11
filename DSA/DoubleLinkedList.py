class Node():
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class doublelinkedlist():
    def __init__(self):
        self.head=None
    def insertAtFirst(self,data):
        node=Node(data,None,self.head)
        self.head=node
    def deleteAtFirst(self):
        if(self.head):
            self.head=self.head.next
    def insertAtend(self,data):
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(data,itr,None)

    def insert(self, index, data):
        length = self.display()
        if (index > length - 1):
            raise Exception("invalid index positon")
        if (index == 0):
            self.insertAtFirst(data)
        itr = self.head
        count = 0
        while (itr):
            if (count == index - 1):
                node = Node(data, itr,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1
    def remove(self,index):
        length=self.display()
        if(index>length-1):
            raise Exception("invalid index positon")
        if(index==0):
            self.deleteAtFirst()
        itr=self.head
        count=0
        while(itr):
            if(count==index-1):
                itr.next=itr.next.next
                break
            itr=itr.next
            count=count+1
    def deleteAtEnd(self):
        itr = self.head
        count = 1
        length = self.display()
        while (itr):
            if (count == length - 1):
                itr.next = None
                break
            itr = itr.next
            count = count + 1
    def display(self):
        itr=self.head
        count=0
        while(itr):
            count=count+1
            #print(itr.data)
            itr=itr.next
        return count
    def seeElements(self):
        itr=self.head
        while(itr):
            print(itr.data)
            itr=itr.next
dl=doublelinkedlist()
dl.insertAtFirst(100)
dl.insertAtFirst(8)
dl.insertAtend(1)
dl.insertAtend(6)
dl.insert(2,500)
dl.remove(1)
dl.seeElements()