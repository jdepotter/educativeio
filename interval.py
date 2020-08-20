from __future__ import print_function
from heapq import *


class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    merged = intervals[:]
    i = 0
    start = 0
    while i < len(merged):
        for j in range(i+1, len(merged)):
            int1 = merged[i]
            int2 = merged[j]
            if int2.start <= int1.start <= int2.end or int2.start <= int1.end <= int2.end or int1.start <= int2.start <= int1.end or int1.start <= int2.end <= int1.end:
                merged[j] = interval(
                    min(int1.start, int2.start), max(int1.end, int2.end))
                start = i + 1
        i += 1

    return merged[start:len(merged)]


#print("Merged intervals: ", end='')
#for i in merge([interval(1, 4), interval(2, 5), interval(7, 9)]): i.print_interval()
# print()

#print("Merged intervals: ", end='')
# for i in merge([interval(6, 7), interval(2, 4), interval(5, 9)]):
#        i.print_interval()
# print()

#print("Merged intervals: ", end='')
# for i in merge([interval(1, 4), interval(2, 6), interval(3, 5)]):
#        i.print_interval()
# print()


def insert(intervals, new_interval):
    merged = []

    j = 0
    while j < len(intervals):
        i = intervals[j]
        if new_interval is not None:
            if new_interval[0] > i[1]:
                merged.append([i[0], i[1]])
            else:
                if new_interval[1] > i[1]:
                    new_interval = [min(i[0], new_interval[0]),
                                    max(i[1], new_interval[1])]
                elif new_interval[1] < i[0]:
                    merged.append([new_interval[0], new_interval[1]])
                    merged.append([i[0], i[1]])
                    new_interval = None
                else:
                    merged.append([min(i[0], new_interval[0]),
                                   max(i[1], new_interval[1])])
                    new_interval = None
        else:
            merged.append([i[0], i[1]])

        j += 1

    return merged

#print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
#print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
#print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


def merge(intervals_a, intervals_b):
    result = []
    i = 0
    j = 0
    while i < len(intervals_a) and j < len(intervals_b):
        aob = intervals_a[i][0] >= intervals_b[j][0] and intervals_a[i][0] <= intervals_b[j][1]
        boa = intervals_b[j][0] >= intervals_a[i][0] and intervals_b[j][0] <= intervals_a[i][1]

        if aob or boa:
            result.append([max(intervals_a[i][0], intervals_b[j][0]), min(
                intervals_a[i][1], intervals_b[j][1])])

        if intervals_a[i][1] >= intervals_b[j][1]:
            j += 1
        else:
            i += 1

    return result


#print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
#print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            return False

    return True


#print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
#print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
#print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)
    minheap = []
    minM = 0

    for m in meetings:
        while minheap and minheap[0] <= m.start:
            heappop(minheap)

        heappush(minheap, m.end)
        minM = max(len(minheap), minM)

    return minM


# print("Minimum meeting rooms required: " + str(min_meeting_rooms(
#    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
# print("Minimum meeting rooms required: " +
#      str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
# print("Minimum meeting rooms required: " +
#      str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
# print("Minimum meeting rooms required: " +
#      str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
# print("Minimum meeting rooms required: " + str(min_meeting_rooms(
#    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))

class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


def find_max_cpu_load(jobs):
    minheap = []
    maxLoad = 0
    cLoad = 0

    jobs.sort(key=lambda x: x.start)
    for j in jobs:
        while minheap and minheap[0][0] <= j.start:
            cLoad -= heappop(minheap)[1]

        cLoad += j.cpu_load
        heappush(minheap, (j.end, j.cpu_load))
        maxLoad = max(maxLoad, cLoad)

    return maxLoad

#print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
#print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
#print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


def find_employee_free_time(schedule):
    result = []
    schedule.sort(key=lambda x: x.start)
    return result


input = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
print("Free intervals: ", end='')
for interval in find_employee_free_time(input):
        interval.print_interval()
print()

input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
print("Free intervals: ", end='')
for interval in find_employee_free_time(input):
    interval.print_interval()
print()

input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
print("Free intervals: ", end='')
for interval in find_employee_free_time(input):
    interval.print_interval()
print()
