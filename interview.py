class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


n1 = Node(1)
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5
n6 = Node(6)
n5.next = n6

n1.print_list()

def switch(n):
    p1 = n
    p2 = n.next
    l1 = n
    l2 = n.next

    while True:
        p1.next = p2.next
        
        if p2.next != None:
            p2.next = p2.next.next

        if p1.next == None:
            p1.next = l2
            break

        p1 = p1.next
        p2 = p2.next

    l1.print_list()

switch(n1)

