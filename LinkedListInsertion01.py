#the DS Hand book Linked insertion

class Node:
    def __init__(self, data):
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

    def search(self, key):
        while self.head is not None:
            if self.head.data == key:
                print("\nThe Key Is Found in LinkedList.")
                print(self.head.data)
                return
            self.head = self.head.next
        print("The Key Is NOT Found in LinkedList!")

    def LinkedListLength(self):
        temp = self.head
        count = 0

        while temp:
            count +=1
            temp = temp.next
        print("Length of LinkedList is :{}".format(count))
    
    def prepend(self, newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return

        else:
            newNode.next = self.head
            self.head = newNode

    def insertPostition(self, newData, pos):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return

        else:
            temp = self.head
            
            for i in range(0,pos-1):
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

    while True:
            print("\nLINKED LIST OPERATIONS\n\n")
            print("1. Insert Prepend-At The Begning\n")
            print("2. Insert At Postition\n")
            print("3. Insert Append-At The End\n")
            print("4. Remove From First\n")
            print("5. Remove By Position\n")
            print("6. Remove From Last")
            print("7. Display LinkedList\n")
            print("8. Count LinkedList Length\n")
            print("9. Search List Element\n")

            choice = int(input("Enter Your Choice ::"))

            if choice == 1:
                newData = input("Prepend/Begning Input ::")
                ll.prepend(newData)

            elif choice == 2:
                newData = input("\nInsert At Postistion Input (Data)::")
                pos = int(input("\nPostion ::"))
                ll.insertPostition(newData,pos)

            elif choice == 3:
                newData = input("\nInsert At Last/Append Input (Data)::")
                ll.append(newData)
            
            elif choice == 4:
                ll.removePrepend()
                print("First Node Deleted")
                
            elif choice == 5:
                pos = int(input("\nPosition ::"))
                ll.removeByPosition(pos)
                
            elif choice == 6:
                ll.removeAppend()
                print("Last Node Deleted.")
            
            elif choice == 7:
                print("\nDisplay LinkedList\n")
                ll.printList()

            elif choice == 8:
                ll.LinkedListLength()

            elif choice == 9:
                key = input("Enter Key You Want To Found ::")
                ll.search(key)
            
            else:
                print("Wrong Option")
