import math


def max_sub_array_of_size_k(k, arr):
    c = 0
    i = 0
    while i < k:
        c += arr[i]
        i += 1

    m = c
    while i != len(arr) - 1:
        c += arr[i]
        c -= arr[i-k]
        if c > m:
            m = c
        i += 1

    return m


r = max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
# print(r)

r = max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])
# print(r)


def smallest_subarray_with_given_sum(s, arr):
    i = 0
    j = 1
    m = len(arr)
    c = arr[i]
    while i < len(arr):
        while j < len(arr) - 1 and c < s:
            c += arr[j]
            j += 1
        if (j - i) < m and c >= s:
            m = j - i
        c -= arr[i]
        i += 1

    if arr[len(arr) - 1] >= s:
        m = 1

    return m


r = smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])
# print(r)

r = smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])
# print(r)

r = smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])
# print(r)


def longest_substring_with_k_distinct(str, k):
    i = 0
    j = 1
    m = 0
    dic = {}
    dic[str[i]] = 1
    while i < len(str):
        while j != len(str) and (len(dic) < k or str[j] in dic):
            if str[j] not in dic:
                dic[str[j]] = 1
            else:
                dic[str[j]] += 1
            j += 1

        if (j - i) > m:
            m = j - i

        if dic[str[i]] == 1:
            del dic[str[i]]
        else:
            dic[str[i]] -= 1

        i += 1

    return m


r = longest_substring_with_k_distinct("araaci", 2)
# print(r)

r = longest_substring_with_k_distinct("araaci", 1)
# print(r)

r = longest_substring_with_k_distinct("cbbebi", 3)
# print(r)


def fruits_into_baskets(fruits):
    return longest_substring_with_k_distinct(''.join(fruits), 2)


r = fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
# print(r)

r = fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])
# print(r)


def non_repeat_substring(str):
    i = 0
    j = 1
    s = set()
    m = 0

    s.add(str[i])
    while i != len(str):
        while j != len(str) and str[j] not in s:
            s.add(str[j])
            j += 1

        if len(s) > m:
            m = len(s)

        s.remove(str[i])
        i += 1

    return m


r = non_repeat_substring("aabccbb")
# print(r)

r = non_repeat_substring("abbbb")
# print(r)

r = non_repeat_substring("abccde")
# print(r)


def length_of_longest_substring(str, k):
    i = 0
    j = 1
    m = 0
    dic = {}
    dic[str[i]] = 1
    while i != len(str):
        while j != len(str) and (len(dic) < 2 or str[j] in dic):
            if str[j] not in dic:
                dic[str[j]] = 1
            else:
                dic[str[j]] += 1
            j += 1

        if (j - i) > m:
            valid = False
            for key in dic:
                if dic[key] <= k:
                    valid = True
            if valid:
                m = j - i

        if dic[str[i]] == 1:
            del dic[str[i]]
        else:
            dic[str[i]] -= 1

        i += 1

    return m


r = length_of_longest_substring("aabccbb", 2)
# print(r)


def build_dic_ref(pattern):
    d = {}
    for c in pattern:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def build_dic(dpref):
    d = {}
    for key in dpref:
        d[key] = 0
    return d


def find_permutation(str, pattern):
    dpref = build_dic_ref(pattern)
    dp = build_dic(dpref)

    k = len(pattern)
    i = 0
    while i < len(pattern):
        if str[i] in dp:
            dp[str[i]] += 1
        i += 1

    if dp == dpref:
        return True

    while i < len(str):
        if str[i] in dp:
            dp[str[i]] += 1

        if str[i-k] in dp:
            dp[str[i-k]] -= 1

        if dp == dpref:
            return True
        i += 1

    return False


r = find_permutation("oidbcaf", "abc")
# print(r)

r = find_permutation("odicf", "dc")
# print(r)

r = find_permutation("bcdxabcdy", "bcdyabcdx")
# print(r)

r = find_permutation("aaacb", "abc")
# print(r)


def find_string_anagrams(str, pattern):
    dpref = build_dic_ref(pattern)
    dp = build_dic(dpref)

    k = len(pattern)
    i = 0
    r = []
    while i < len(pattern):
        if str[i] in dp:
            dp[str[i]] += 1
        i += 1

    if dp == dpref:
        r.append(0)

    while i < len(str):
        if str[i] in dp:
            dp[str[i]] += 1

        if str[i-k] in dp:
            dp[str[i-k]] -= 1

        i += 1

        if dp == dpref:
            r.append(i-k)

    return r


r = find_string_anagrams("ppqp", "pq")
# print(r)

r = find_string_anagrams("abbcabc", "abc")
# print(r)


def pair_with_targetsum(arr, target_sum):
    i = 0
    j = len(arr) - 1

    while True:
        s = arr[i] + arr[j]
        if s == target_sum:
            return [i, j]
        if s < target_sum:
            i += 1
        if s > target_sum:
            j -= 1

        if i == j:
            break

    return [-1, -1]


r = pair_with_targetsum([1, 2, 3, 4, 6], 6)
# print(r)

r = pair_with_targetsum([2, 5, 9, 11], 11)
# print(r)


def remove_duplicates(arr):
    lval = arr[0]
    lindex = 0
    for i in range(1, len(arr)):
        if arr[i] != lval:
            lindex += 1

        arr[lindex] = arr[i]
        lval = arr[i]
        i += 1

    return lindex + 1


r = remove_duplicates([2, 3, 3, 3, 6, 9, 9])
# print(r)

r = remove_duplicates([2, 2, 2, 11])
# print(r)


def make_squares(arr):
    squares = [-1] * len(arr)
    i = 0
    j = len(arr) - 1
    lindex = len(arr) - 1

    while i <= j:
        sqi = arr[i] * arr[i]
        sqj = arr[j] * arr[j]

        if sqi > sqj:
            squares[lindex] = sqi
            i += 1
        else:
            squares[lindex] = sqj
            j -= 1

        lindex -= 1
    return squares


r = make_squares([-2, -1, 0, 2, 3])
# print(r)

r = make_squares([-3, -1, 0, 1, 2])
# print(r)


def search_triplets(arr):
    triplets = []
    arr.sort()

    for k in range(len(arr)):
        if k > 0 and arr[k] == arr[k-1]:
            continue
        i = k + 1
        j = len(arr) - 1
        target = -arr[k]
        while i < j:
            s = arr[i] + arr[j]
            if s == target:
                triplets.append([arr[k], arr[i], arr[j]])
                i += 1
                j -= 1
                while i < j and arr[i] == arr[i-1]:
                    i += 1
                while i < j and arr[j] == arr[j+1]:
                    j -= 1
            elif s < target:
                i += 1
            else:
                j -= 1

    return triplets


r = search_triplets([-3, 0, 1, 2, -1, 1, -2])
# print(r)

r = search_triplets([-5, 2, -1, -2, 3])
# print(r)


def triplet_sum_close_to_target(arr, target_sum):
    m = math.inf
    arr.sort()

    for k in range(len(arr)):
        i = k + 1
        j = len(arr) - 1
        while i < j:
            s = target_sum - arr[k] - arr[i] - arr[j]
            if s == 0:
                return target_sum
            if abs(s) < abs(m) or (s == -m and s > m):
                m = s
            if s > 0:
                i += 1
            else:
                j -= 1

    return target_sum - m


r = triplet_sum_close_to_target([-2, 0, 1, 2], 2)
# print(r)

r = triplet_sum_close_to_target([-3, -1, 1, 2], 1)
# print(r)

r = triplet_sum_close_to_target([1, 0, 1, 1], 100)
# print(r)


def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()

    for k in range(len(arr)):
        i = k + 1
        j = len(arr) - 1
        while i < j:
            s = arr[k] + arr[i] + arr[j]
            if s < target:
                count += j - i
                i += 1
            else:
                j -= 1

    return count


r = triplet_with_smaller_sum([-1, 0, 2, 3], 3)
# print(r)

r = triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)
# print(r)


def find_subarrays(arr, target):
    result = []
    i = 0
    j = i + 1
    while i < len(arr):
        p = arr[i]

        if p < target:
            result.append(p)

        r = [p]
        while j < len(arr) and p * arr[j] < target:
            r.append(arr[j])
            p *= arr[j]
            result.append(r)
            j += 1

        i += 1
        j = i + 1
    return result


r = find_subarrays([2, 5, 3, 10], 30)
# print(r)

r = find_subarrays([8, 2, 6, 5], 50)
# print(r)


def dutch_flag_sort(arr):
    i = 0
    j = len(arr) - 1

    k = 0
    while k <= j:
        if arr[k] == 0:
            arr[i], arr[k] = arr[k], arr[i]
            i += 1
            k += 1

        elif arr[k] == 2:
            arr[j], arr[k] = arr[k], arr[j]
            j -= 1

        elif arr[k] == 1:
            k += 1

    return


arr = [1, 0, 2, 1, 0]
dutch_flag_sort(arr)
# print(arr)

arr = [2, 2, 0, 1, 2, 0]
dutch_flag_sort(arr)
# print(arr)


def backspace_compare(str1, str2):
    i = len(str1) - 1
    j = len(str2) - 1
    while i >= 0 or j >= 0:
        f = 0
        while i > 0 and str1[i] == '#':
            i -= 1
            f += 1

        i -= f

        f = 0
        while j > 0 and str2[j] == '#':
            j -= 1
            f += 1

        j -= f

        if str1[i] != str2[j]:
            return False

        i -= 1
        j -= 1

    return True


r = backspace_compare("xy#z", "xzz#")
# print(r)

r = backspace_compare("xy#z", "xyz#")
# print(r)

r = backspace_compare("xp#", "xyz##")
# print(r)

r = backspace_compare("xywrrmp", "xywrrmu#p")
# print(r)


def shortest_window_sort(arr):
    l = len(arr)
    i = 0
    j = l - 1

    while i < l - 1 and arr[i] <= arr[i+1]:
        i += 1

    if i == l - 1:
        return 0

    while j > 0 and arr[j] >= arr[j-1]:
        j -= 1

    mi = arr[i]
    ma = arr[j]

    for k in range(i,j+1):
        mi = min(mi, arr[k])
        ma = max(ma, arr[k])

    while i > 0 and arr[i-1] > mi:
        i -= 1

    while j < l - 1 and arr[j+1] < ma:
        j += 1

    return j - i + 1


r = shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12])
print(r)

r = shortest_window_sort([1, 3, 2, 0, -1, 7, 10])
print(r)

r = shortest_window_sort([1, 2, 3])
print(r)

r = shortest_window_sort([3, 2, 1])
print(r)


