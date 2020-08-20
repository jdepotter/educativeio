from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def traverse(root):
    result = []
    q = deque()

    q.append(root)
    while q:
        c = len(q)
        rl = []
        for _ in range(c):
            cur = q.popleft()
            rl.append(cur.val)
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)

        result.append(rl)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
#print("Level order traversal: " + str(traverse(root)))


def traverse(root):
    result = deque()
    q = deque()

    q.append(root)
    while q:
        c = len(q)

        rl = []
        for _ in range(c):
            cur = q.popleft()
            rl.append(cur.val)
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)

        result.appendleft(rl)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
# print("Reverse level order traversal: " + str(traverse(root)))


def traverse(root):
    result = []
    q = deque()

    q.append(root)
    rev = False
    while q:
        c = len(q)
        rl = []
        for _ in range(c):
            cur = q.popleft()
            if not rev:
                rl.append(cur.val)
            else:
                rl.insert(0, cur.val)
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)

        rev = not rev

        result.append(rl)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)
# print("Zigzag traversal: " + str(traverse(root)))


def find_level_averages(root):
    result = []
    q = deque()

    q.append(root)
    while q:
        c = len(q)
        s = 0
        for _ in range(c):
            cur = q.popleft()
            s += cur.val
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)

        result.append(s/c)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
# print("Level averages are: " + str(find_level_averages(root)))


def find_minimum_depth(root):
    q = deque()
    q.append(root)
    i = 0
    while q:
        c = len(q)
        i += 1
        for _ in range(c):
            cur = q.popleft()
            if cur.left is None and cur.right is None:
                return i

            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
# print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
root.left.left = TreeNode(9)
root.right.left.left = TreeNode(11)
# print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


def find_successor(root, key):
    q = deque()

    q.append(root)
    while q:
        cur = q.popleft()
        if cur.left != None:
            q.append(cur.left)
        if cur.right != None:
            q.append(cur.right)

        if cur.val == key:
            return q.popleft()

    return None


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
result = find_successor(root, 12)
# if result:
#    print(result.val)
result = find_successor(root, 9)
# if result:
#    print(result.val)


def connect_level_order_siblings(root):
    q = deque()

    q.append(root)
    while q:
        c = len(q)
        for i in range(c):
            cur = q.popleft()
            if i < c - 1:
                cur.next = q[0]
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)

    return


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connect_level_order_siblings(root)

#print("Level order traversal using 'next' pointer: ")
# root.print_level_order()


def connect_all_siblings(root):
    q = deque()

    q.append(root)
    while q:
        c = len(q)
        last = None
        for i in range(c):
            cur = q.popleft()
            if i < c - 1:
                cur.next = q[0]
            if cur.left is not None:
                q.append(cur.left)
                if last is None:
                    last = cur.left
            if cur.right is not None:
                q.append(cur.right)
                if last is None:
                    last = cur.right

            if cur.next == None:
                cur.next = last

    return


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connect_all_siblings(root)
# root.print_tree()


def tree_right_view(root):
    result = []
    q = deque()

    q.append(root)
    result.append(root)
    while q:
        c = len(q)
        for i in range(c):
            cur = q.popleft()
            if cur.left is not None:
                q.append(cur.left)
                if cur.right is None and cur.left.right is None and cur.left.left is None:
                    result.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
                result.append(cur.right)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(3)
result = tree_right_view(root)
#print("Tree right view: ")
# for node in result:
#    print(str(node.val) + " ", end='')


def has_path(root, sum):
    sum -= root.val

    if root.left is None and root.right is None and sum == 0:
        return True

    return root.left is not None and has_path(root.left, sum) or root.right is not None and has_path(root.right, sum)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
#print("Tree has path: " + str(has_path(root, 23)))
#print("Tree has path: " + str(has_path(root, 16)))


def find_paths(root, sum, curPath=[], allPaths=[]):
    sum -= root.val
    curPath.append(root.val)

    if root.left is None and root.right is None and sum == 0:
        allPaths.append(curPath)
        return

    if root.left is not None:
        find_paths(root.left, sum, curPath.copy(), allPaths)

    if root.right is not None:
        find_paths(root.right, sum, curPath.copy(), allPaths)

    return allPaths


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
sum = 23
#print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))


def find_sum_of_path_numbers(root, curPath=0):
    if root == None:
        return 0

    curPath = curPath * 10 + root.val

    if root.left is None and root.right is None:
        return curPath

    return find_sum_of_path_numbers(root.left, curPath) + find_sum_of_path_numbers(root.right, curPath)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
#print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


def find_path(root, sequence, level=0):
    if root is None or len(sequence) - 1 < level or root.val != sequence[level]:
        return False

    if root.left is None and root.right is None and root.val == sequence[level]:
        return True

    return find_path(root.left, sequence, level + 1) or find_path(root.right, sequence, level + 1)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

#print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
#print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


def count_paths(root, S, currentPath=[]):
    if root is None:
        return 0

    currentPath.append(root.val)
    pathCount = 0
    pathSum = 0
    for i in range(len(currentPath)-1, -1, -1):
        pathSum += currentPath[i]
        if pathSum == S:
            pathCount += 1

    pathCount += count_paths(root.left, S, currentPath) + \
        count_paths(root.right, S, currentPath)

    del currentPath[-1]

    return pathCount


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
#print("Tree has paths: " + str(count_paths(root, 11)))


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter_recursive(self, root):
        if root is None:
            return 0

        l = self.find_diameter_recursive(root.left)
        r = self.find_diameter_recursive(root.right)

        self.treeDiameter = max(self.treeDiameter, l + r + 1)

        return max(l, r) + 1

    def find_diameter(self, root):
        self.find_diameter_recursive(root)
        return self.treeDiameter


treeDiameter = TreeDiameter()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
#rint("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
root.left.left = None
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.left.right.left = TreeNode(10)
root.right.right.left.left = TreeNode(11)
#print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))

import math

class MaximumPathSum:

    def __init__(self):
        self.maxSum = -math.inf

    def find_maximum_path_sum(self, root):
        self.find_maximum_path_sum_recursive(root)
        return self.maxSum

    def find_maximum_path_sum_recursive(self, root):
        if root is None:
            return 0

        l = max(self.find_maximum_path_sum_recursive(root.left), 0)
        r = max(self.find_maximum_path_sum_recursive(root.right), 0)

        self.maxSum = max(self.maxSum, l + r + root.val)

        return max(l, r) + root.val


maximumPathSum = MaximumPathSum()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

maximumPathSum = MaximumPathSum()
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

maximumPathSum = MaximumPathSum()
root = TreeNode(-1)
root.left = TreeNode(-3)
print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
