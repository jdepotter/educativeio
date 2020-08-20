from heapq import *


class MedianOfAStream:
    minheap = []
    maxheap = []

    def insert_num(self, num):
        if len(self.maxheap) == 0 or -self.maxheap[0] >= num:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def find_median(self):
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0

        return -self.maxheap[0]


medianOfAStream = MedianOfAStream()
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(1)
#print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(5)
#print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(4)
#print("The median is: " + str(medianOfAStream.find_median()))


class SlidingWindowMedian:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def insert_num(self, num):
        if len(self.maxheap) == 0 or -self.maxheap[0] >= num:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        self.balance_heap()

    def balance_heap(self):
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def remove_num(self, num):
        t = []
        if len(self.maxheap) > 0 and -self.maxheap[0] >= num:
            while len(self.maxheap) > 0:
                v = heappop(self.maxheap)
                if v != -num:
                    t.append(v)
                else:
                    for e in t:
                        heappush(self.maxheap, e)
                    break
        else:
            while len(self.minheap) > 0:
                v = heappop(self.minheap)
                if v != num:
                    t.append(v)
                else:
                    for e in t:
                        heappush(self.minheap, e)
                    break

        self.balance_heap()

    def find_median(self):
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0

        return -self.maxheap[0] / 1.0

    def find_sliding_window_median(self, nums, k):
        result = []

        i = 0
        j = 0
        while j < k - 1:
            self.insert_num(nums[j])
            j += 1

        while j < len(nums):
            vj = nums[j]
            self.insert_num(vj)

            result.append(self.find_median())

            vi = nums[i]
            self.remove_num(vi)
            i += 1
            j += 1

        return result


slidingWindowMedian = SlidingWindowMedian()
result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
#print("Sliding window medians are: " + str(result))

slidingWindowMedian = SlidingWindowMedian()
result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
#print("Sliding window medians are: " + str(result))


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    capheap = []
    proheap = []
    curcap = initialCapital

    for i in range(len(capital)):
        heappush(capheap, (capital[i], i))

    for _ in range(numberOfProjects):
        while capheap and capheap[0][0] <= curcap:
            cap, i = heappop(capheap)
            heappush(proheap, (-profits[i], i))

        if len(proheap) == 0:
            break

        curcap += -heappop(proheap)[0]

    return curcap


#print("Maximum capital: " + str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
#print("Maximum capital: " + str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    result = []

    minheapstart = []
    for i in range(len(intervals)):
        heappush(minheapstart, (intervals[i].start, i))

    for i in range(len(intervals)):
        minheaptemp = []
        while minheapstart and (minheapstart[0][0] < intervals[i].end or minheapstart[0][1] == i):
            (v, j) = heappop(minheapstart)
            heappush(minheaptemp, (v, j))

        if minheapstart:
            result.append(minheapstart[0][1])
        else:
            result.append(-1)

        minheaptemp = heapify(list(merge(minheapstart, minheaptemp)))

    return result


result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
#print("Next interval indices are: " + str(result))

result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
#print("Next interval indices are: " + str(result))


class Solution:
    maxHeap = []
    result = [-1] * len(nums)

      i = len(nums) - 1
       while i >= 0:
            if maxHeap:
                tHeap = []
                index = -1
                while maxHeap and -maxHeap[0][0] >= nums[i]:
                    val = heappop(maxHeap)
                    if index < val[1] and -val[0] > nums[i]:
                        result[i] = -val[0]
                        index = val[1]

                    heappush(tHeap, val)

                while tHeap:
                    heappush(maxHeap, heappop(tHeap))

            heappush(maxHeap, (-nums[i], i))

            i -= 1

        i = 0
        maxHeap = []
        while i < len(nums):
            if result[i] == -1 and maxHeap:
                tHeap = []
                index = len(nums) - 1
                while maxHeap and -maxHeap[0][0] >= nums[i] and result[i] == -1:
                    val = heappop(maxHeap)
                    if index > val[1] and -val[0] > nums[i]:
                        result[i] = -val[0]
                        index = val[1]

                    heappush(tHeap, val)

                while tHeap:
                    heappush(maxHeap, heappop(tHeap))

            heappush(maxHeap, (-nums[i], i))

            i += 1

        return result


s = Solution()

print(s.nextGreaterElements([1, 2, 3, 4, 3]))
