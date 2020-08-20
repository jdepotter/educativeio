from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head):
    cur = head
    prev = None
    nex = None
    while cur != None:
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex

    return prev


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

#print("Nodes of original LinkedList are: ", end='')
# head.print_list()
result = reverse(head)
#print("Nodes of reversed LinkedList are: ", end='')
# result.print_list()


def reverse_sub_list(head, p, q):
    subHead = None
    tail = None
    curHead = None

    cur = head
    i = 1
    while cur != None:
        if i == p - 1:
            curHead = cur
            subHead = cur.next
        if i == q:
            tail = cur.next
            cur.next = None
            break

        cur = cur.next
        i += 1

    subTail = reverse(subHead)

    curHead.next = subTail
    subHead.next = tail

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

#print("Nodes of original LinkedList are: ", end='')
# head.print_list()
result = reverse_sub_list(head, 2, 4)
#print("Nodes of reversed LinkedList are: ", end='')
# result.print_list()


def reverse_every_k_elements(head, k):
    cur = head
    prev = None
    while cur is not None:
        tHead = prev
        tTail = cur
        i = 0
        while i < k and cur is not None:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
            i += 1

        if tHead is not None:
            tHead.next = prev
        else:
            head = prev

        tTail.next = cur
        prev = tTail

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

#print("Nodes of original LinkedList are: ", end='')
# head.print_list()
result = reverse_every_k_elements(head, 3)
#print("Nodes of reversed LinkedList are: ", end='')
# result.print_list()


def reverse_alternate_k_elements(head, k):
    cur = head
    prev = None
    while cur is not None:
        tHead = prev
        tTail = cur
        i = 0
        while i < k and cur is not None:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
            i += 1

        if tHead is not None:
            tHead.next = prev
        else:
            head = prev

        tTail.next = cur

        i = 0
        while i < k and cur is not None:
            prev = cur
            cur = cur.next
            i += 1

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

#print("Nodes of original LinkedList are: ", end='')
# head.print_list()
result = reverse_alternate_k_elements(head, 2)
#print("Nodes of reversed LinkedList are: ", end='')
# result.print_list()


def rotate(head, rotations):
    c = 0
    cur = head
    while cur.next != None:
        cur = cur.next
        c += 1

    if rotations == c + 1:
        return head

    tail = cur
    rotations = (rotations % (c + 1)) - 1 if rotations > c else rotations

    i = 1
    cur = head
    while i < rotations:
        cur = cur.next
        i += 1

    tail.next = head
    head = cur.next
    cur.next = None

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

#print("Nodes of original LinkedList are: ", end='')
# head.print_list()
result = rotate(head, 6)
#print("Nodes of rotated LinkedList are: ", end='')
# result.print_list()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

#print("Nodes of original LinkedList are: ", end='')
# head.print_list()
result = rotate(head, 8)
#print("Nodes of rotated LinkedList are: ", end='')
# result.print_list()


def has_cycle(head):
    i = head
    j = head.next.next
    while i.value != j.value:
        if i.next is None or j.next is None or j.next.next is None:
            return False

        i = i.next
        j = j.next.next

    return True


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
#print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next
#print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next.next
#print("LinkedList has cycle: " + str(has_cycle(head)))


def find_start(head, k):
    i = head
    j = head

    for _ in range(k):
        j = j.next

    while i != j:
        i = i.next
        j = j.next

    return i


def find_cycle_length(i):
    k = 1
    j = i.next
    while j != i:
        j = j.next
        k += 1
    return k


def find_cycle(head):
    i = head
    j = head
    k = 0
    while True:
        j = j.next.next
        i = i.next
        if i == j:
            k = find_cycle_length(i)
            break

    return find_start(head, k)


def find_cycle_start(head):
    return find_cycle(head)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
#print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head.next.next.next
#print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head
#print("LinkedList cycle start: " + str(find_cycle_start(head).value))


def compute_square(num):
    s = 0
    while num != 0:
        s += (num % 10) * (num % 10)
        num = num // 10

    return s


def find_happy_number(num):
    i = num
    j = num
    while True:
        i = compute_square(i)
        j = compute_square(compute_square(j))

        if i == j:
            return i == 1


# print(find_happy_number(23))
# print(find_happy_number(12))


def find_middle_of_linked_list(head):
    i = head
    j = head
    while True:
        if j.next is None:
            return i
        elif j.next.next is None:
            return i.next

        i = i.next
        j = j.next.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

#print("Middle Node: " + str(find_middle_of_linked_list(head).value))

head.next.next.next.next.next = Node(6)
#print("Middle Node: " + str(find_middle_of_linked_list(head).value))

head.next.next.next.next.next.next = Node(7)
#print("Middle Node: " + str(find_middle_of_linked_list(head).value))


def circular_array_loop_exists(arr):
    i = 0
    j = 0
    reachBound = False
    while True:
        i = arr[i] + i
        if i >= len(arr):
            i -= len(arr)
        elif i < 0:
            i = len(arr) + i

        j = arr[j] + j
        if j >= len(arr):
            j -= len(arr)
            reachBound = True
        elif j < 0:
            j = len(arr) + j
            reachBound = True

        j = arr[j] + j
        if j >= len(arr):
            j -= len(arr)
            reachBound = True
        elif j < 0:
            j = len(arr) + j
            reachBound = True

        if i == j:
            return reachBound


print(circular_array_loop_exists([1, 2, -1, 2, 2]))
print(circular_array_loop_exists([2, 2, -1, 2]))
print(circular_array_loop_exists([2, 1, -1, -2]))
