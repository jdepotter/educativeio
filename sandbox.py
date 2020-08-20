class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, val):
        n = Node(val)
        if self.head == None:
            self.head = n
            self.tail = self.head
            return

        self.tail.next = n
        n.prev = self.tail       
        self.tail = self.tail.next


    def prepend(self, val):
        n = Node(val)
        if self.head == None:
            self.head = n
            self.tail = self.head
            return

        n.next = self.head
        self.head.prev = n
        self.head = n

    
    def __find(self, index):
        tList = self.head
        c = 0

        while c != index:
            if tList == None:
                raise Exception('Index out of bounds')
            tList = tList.next
            c += 1

        return tList


    def insert(self, val, index):
        if index == 0:
            self.prepend(val)
            return

        tList = None
        try:
            t_List = self.__find(index):
        except e:
            raise e

        if tList == None:
            self.append(val)
            return
        
        n = Node(val)
        n.next = tList
        tList.prev.next = n
        n.prev = tList.prev
        tList.prev = n


    def remove(self, val, index):
        if index == 0:
            self.head = self.head.next

        


    def length(self):
        tList = self.head
        l = 0

        while tList != None:
            tList = tList.next
            l += 1

        return l

    
    def print(self):
        tList = self.head
        s = ''
        while tList != None:
            s += f'{tList.val}, '
            tList = tList.next

        print(s)


    def indexOf(self, val):
        tList = self.head
        index = 0
        while tList != None:
            if tList.val == val:
                return index, val
            tList = tList.next
            index += 1

        return None

    
    def indexesOf(self, val):
        tList = self.head
        indexes = []
        index = 0
        while tList != None:
            if tList.val == val:
                indexes.append(index)
            tList = tList.next
            index += 1

        return val, indexes


class Stack(List):
    def push(self, val)
        self.prepend(val)

    def pop(self)




list = List()
list.append(2)
list.append(4)
list.prepend(1)
list.append(2)
list.insert(3, 0)
list.print()
print(list.indexesOf(2))