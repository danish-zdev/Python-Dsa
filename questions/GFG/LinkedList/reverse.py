class Node:
    def __init__(self, data, nextRef):
        self.data = data
        self.ref = nextRef

class LinkedList:
    def __init__(self):
        self.head = None   

    def Insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def printL(self):
        if self.head is None:
            print("Linked list Empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, "->", end=" ")
                n = n.ref

    def reverse(self):
        # prev = None
        # n = self.head
        # while n:
        #     nxt = n.ref
        #     n.ref = prev
        #     prev = n
        #     n = nxt     
        # self.head = prev  
        #    
  
        curr,pre,nxt = self.head,None,None
        while curr:
            nxt = curr.ref # hold the next address of curr
            curr.ref = pre # connect current to pre " <- " (reverse node)
            pre = curr # move previous
            curr = nxt # move curr 
        self.head = pre    


    def DeleteAtBegning(self):
        if self.head is None:
            print("Linked list Empty")
            return
        else:
            self.head = self.head.ref

    def DeleteAtLast(self):
        if self.head is None:
            print("Linked list Empty")
            return
        else:
            temp = self.head
            while temp.ref:
                temp = temp.ref
                if temp.ref.ref is None:
                    temp.ref = None

    def DeleteMiddle(self, pos):
        if self.head is None:
            print("Linked list Empty")
            return
        if pos == 0:
            self.DeleteAtBegning()
            return
        
        currentNode = self.head
        currentPos = 0
        while True:
            if currentPos == pos:
                previousNode.ref= currentNode.ref
                currentNode.ref = None
                break
            previousNode = currentNode
            currentNode = currentNode.ref
            currentPos +=1



            
   


ll = LinkedList()

ll.Insert(4)
ll.Insert(6)
ll.Insert(2)
ll.Insert(0)
ll.Insert(8)
ll.printL()
print()
ll.reverse()
ll.printL()


 

      