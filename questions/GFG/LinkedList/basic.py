class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head == None:  
            print("LinkedList is Empty")
        else:
            n = self.head
            while n!= None:
                print(n.data, end='->') 
                n = n.next     

    def insertBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode   

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = newNode

       
ll = LinkedList()

ll.insertBegin(1)
ll.insertBegin(2)
ll.insertBegin(3)
ll.insertBegin(4)
ll.insertBegin(5)

ll.printLL()
print()

ll.insertEnd(1)
ll.insertEnd(2)
ll.insertEnd(3)
ll.insertEnd(4)

ll.printLL()
print()


