import math


def find_single_number(arr):
    x = 0
    for n in arr:
        x ^= n
    return x


arr = [1, 4, 2, 1, 3, 2, 3]
# print(find_single_number(arr))


def find_single_numbers(nums):
    x1 = 0
    for n in nums:
        x1 ^= n

    b = 1
    while (b & x1) == 0:
        b = b << 1

    r = [0, 0]
    for n in nums:
        if b & n != 0:
            r[0] ^= n
        else:
            r[1] ^= n

    return r


#print('Single numbers are:' + str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
#print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


def calculate_bitwise_complement(n):
    nbBit = int((math.log(n) / math.log(2)) + 1)
    r = 0

    for i in range(nbBit):
        b = 1 & (n >> i)
        r = r | ((b ^ 1) << i)

    return r


#print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
#print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


def flip_and_invert_image(matrix):
    x = len(matrix)
    z = len(matrix[0])
    y = int(z/2)

    for i in range(x):
        for j in range(y):
            matrix[i][j], matrix[i][z-1-j] = 1^matrix[i][z-1-j], 1^matrix[i][j]
        
        if z % 2 != 0:
            matrix[i][j+1] ^= 1

    return matrix


print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
print(flip_and_invert_image(
    [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
