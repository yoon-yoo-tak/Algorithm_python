from collections import Counter


def findLongestConseqSubseq(arr, n):
    '''We insert all the array elements into set.'''
    str = 0
    stl = 0
    l = 0
    r = 0
    S = set(arr)

    # check each possible sequence from the start
    # then update optimal length
    ans = 0
    for e in arr:
        l = 0
        r = 0
        # i contains current element of array
        i = e
        # count represents the length of current sequence
        count = 1

        # if current element is the starting
        # element of a sequence
        if i - 1 not in S:
            l = i - 1
            # Then check for next elements in the
            # sequence
            while i + 1 in S:
                # increment the value of array element
                # and repeat search in the set
                i += 1
                count += 1

                # Update optimal length if this length
                # is more.
                r = i
            if count > ans:
                stl = l
                str = r
            ans = max(ans, count)
    return [stl, str]


# Function to find the number of array
# elements with frequency more than n/k times
def printElements(arr, n, k):
    # Calculating n/k
    x = k

    # Counting frequency of every
    # element using Counter
    mp = Counter(arr)

    # Traverse the map and print all
    # the elements with occurrence
    # more than n/k times
    la = []
    for it in mp:
        if mp[it] >= x:
            la.append(it)
    return la


# Driver code
# arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
# n = len(arr)
# k = 4

# printElements(arr, n, k)

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    arr = sorted(printElements(l, n, k))
    prev = -2
    flag = False
    if len(arr) == 0:
        print(-1)
        flag = True
    if not flag:
        for j in arr:
            if j - prev == 1:
                break
            prev = j
        else:
            flag = True
            print(arr[0])
        if not flag:
            counter = 1
            stl = 0
            str = 0
            r = 0
            l = 0
            mc = 0
            a = findLongestConseqSubseq(arr, len(arr))
            if a[0] == 1 and a[1] == None:
                print(a[0], a[0])
            else:
                print(a[0] + 1, a[1])