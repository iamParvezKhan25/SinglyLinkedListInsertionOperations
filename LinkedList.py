# LinkedList Insertion Operation

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def LinkedListLength(self):
        count = 0

        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("LinkedList Length :: {}".format(count))

    def searchList(self,key):
        temp = self.head
        while temp:
            if temp.data == key:
                print("List Element {} Found".format(key))
                return
            
            temp = temp.next
        print("List Element {} NOT Found!".format(key))
        
    def prepend(self,newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtPosition(self,newData,pos):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return
        else:
            temp = self.head

            for i in range(0,pos-1): #Head is 0
                temp = temp.next

            newNode.next = temp.next
            temp.next = newNode

    def append(self,newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = newNode

    def removePrepend(self):
        if self.head is None:
            return None

        temp = self.head

        self.head = self.head.next
        temp = None
        return self.head

    def removeAppend(self):
        if self.head is None:
            return None

        temp = self.head

        if self.head.next is None:
            self.head = None
        else:
            while temp.next is not None:
                prev = temp
                temp = temp.next

            prev.next = None

    def removeByPosition(self, pos):
        if self.head is None:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(pos-1):
            temp = temp.next

            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None
        temp.next = next
    
if __name__ == '__main__':

    ll = LinkedList()

    ll.prepend(50)
    ll.prepend(40)
    ll.prepend(30)

    ll.append(60)
    ll.append(70)

    ll.insertAtPosition(99,1)
    
    
    #ll.removePrepend()
    ll.removeAppend()
    ll.removeAppend()
    #ll.removePrepend()
    
    #ll.removeByPosition(5)
    
    ll.printList()

    ll.LinkedListLength()

    ll.searchList(30)
