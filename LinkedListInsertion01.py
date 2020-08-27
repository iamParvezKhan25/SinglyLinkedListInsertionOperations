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

if __name__ == '__main__':
    ll = LinkedList()

    while True:
            print("\nLINKED LIST OPERATIONS\n\n")
            print("1. Insert Prepend-At The Begning\n")
            print("2. Insert At Postition\n")
            print("3. Insert Append-At The End\n")
            print("4. Display LinkedList\n")
            print("5. Count LinkedList Length\n")
            print("6. Search List Element\n")

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
                print("\nDisplay LinkedList\n")
                ll.printList()

            elif choice == 5:
                ll.LinkedListLength()

            elif choice == 6:
                key = input("Enter Key You Want To Found ::")
                ll.search(key)
            
            else:
                print("Wrong Option")
