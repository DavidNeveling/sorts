import random, time, sys
def main():

    sys.setrecursionlimit(sys.getrecursionlimit()*2) # quick sort breaks the default limit with len(list) = 1000

    list = [random.randrange(1, 50) for i in range(8)]
    funcList = [nativeSort, quickSort, mergeSort, radixSort, insertionSort, selectionSort, customSort, customSortPopFront]
    print("Checking for correctness\n")
    print("initial list")
    print(list)
    print("")

    for f in funcList:
        listB = list[:]
        start = time.clock()
        listB = f(listB)
        end = time.clock()
        print(f.__name__)
        print("\t"+str(listB))
        print("\ttime elapsed = " + str(end - start))

    print("\nTime Analysis")
    size = 1000
    print("list size: " + str(size))

    print("\nRandom order\n")
    list = [random.randrange(1, size) for i in range(size)]
    for f in funcList:
        listB = list[:]
        start = time.clock()
        listB = f(listB)
        end = time.clock()
        print(f.__name__)
        print("\ttime elapsed = " + str(end - start))

    print("\nSorted order\n")
    list = [i for i in range(1, size+1)]
    for f in funcList:
        listB = list[:]
        start = time.clock()
        listB = f(listB)
        end = time.clock()
        print(f.__name__)
        print("\ttime elapsed = " + str(end - start))

    print("\nSemi-Sorted order\n")
    list = [i%(size/20) for i in range(1, size+1)]
    for f in funcList:
        listB = list[:]
        start = time.clock()
        listB = f(listB)
        end = time.clock()
        print(f.__name__)
        print("\ttime elapsed = " + str(end - start))

    print("\nReverse order\n")
    list = [size - i for i in range(1, size+1)]
    for f in funcList:
        listB = list[:]
        start = time.clock()
        listB = f(listB)
        end = time.clock()
        print(f.__name__)
        print("\ttime elapsed = " + str(end - start))

    print("\nSemi-Reverse order\n")
    list = [(size - i)%(size/20) for i in range(1, size+1)]
    for f in funcList:
        listB = list[:]
        start = time.clock()
        listB = f(listB)
        end = time.clock()
        print(f.__name__)
        print("\ttime elapsed = " + str(end - start))


def nativeSort(list):
    return sorted(list)

def customSortPopFront(list):
    i = 0
    listlist = []
    while i < len(list):
        sublist, i = customSortHelper(list, i)
        listlist.append(sublist)
    while len(listlist) > 1:
        listA = listlist.pop(0)
        listB = listlist.pop(0)
        listlist.append(merge(listA, listB))
    return listlist[0]

# I read online about something called 'natural mergeSort'
# Here's something I wrote after reading the first 2 sentences of its description
def customSort(list):
    i = 0
    listlist = []
    while i < len(list):
        sublist, i = customSortHelper(list, i)
        listlist.append(sublist)
    while len(listlist) > 1:
        listA = listlist.pop()
        listB = listlist.pop()
        listlist.append(merge(listA, listB))
    return listlist[0]

def customSortHelper(list, index):
    newList = []
    ascending = False
    descending = False
    stop = False
    i = index + 1
    prevVal = list[index]
    newList.append(prevVal)
    while i < len(list) and not stop:
        if ascending:
            if list[i] >= prevVal:
                prevVal = list[i]
                newList.append(prevVal)
            else:
                return (newList, i)
        if descending:
            if list[i] < prevVal:
                prevVal = list[i]
                newList.append(prevVal)
            else:
                newList.reverse()
                return (newList, i)
        if not ascending and not descending:
            if list[i] >= prevVal:
                ascending = True
            if list[i] < prevVal:
                descending = True
            prevVal = list[i]
            newList.append(prevVal)
        i += 1
    return (newList, len(list))

# im stupid so i got this one off the internet
def radixSort(list, base=10):
    def listToBuckets(list, base, iteration):
        buckets = [[] for x in range(base)]
        for number in list:
            digit = (number // (base ** iteration)) % base
            buckets[digit].append(number)
        return buckets
    def bucketsToList(buckets):
        numbers = []
        for bucket in buckets:
            for number in bucket:
                numbers.append(number)
        return numbers
    maxval = max(list)
    it = 0
    while base ** it <= maxval:
        list = bucketsToList(listToBuckets(list, base, it))
        it += 1
    return list

def mergeSort(list):
    if len(list) <= 1:
        return list
    m = len(list)/2
    return merge(mergeSort(list[0:m]), mergeSort(list[m:len(list)]))

def merge(sortedListA, sortedListB):
    newList = []
    while len(sortedListA) > 0 or len(sortedListB) > 0:
        if len(sortedListA) == 0:
            while len(sortedListB) > 0:
                newList.append(sortedListB.pop(0))
        elif len(sortedListB) == 0:
            while len(sortedListA) > 0:
                newList.append(sortedListA.pop(0))
        else:
            if sortedListA[0] > sortedListB[0]:
                newList.append(sortedListB.pop(0))
            else:
                newList.append(sortedListA.pop(0))
    return newList

def quickSort(list):
    return quickSortAlgorithm(list, 0, len(list)-1)

def quickSortAlgorithm(list, low, high):
    if low < high:
        p = quickSortPartitionLomuto(list, low, high)
        quickSortAlgorithm(list, low, p-1) # Lomuto
        quickSortAlgorithm(list, p+1, high)
    return list

def quickSortPartitionLomuto(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    i += 1
    list[i], list[high] = list[high], list[i]
    return (i)

def quickSortPartitionHoare(list, low, high):
    pivot = list[low]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if list[i] < pivot:
                break
        while True:
            j -= 1
            if list[j] > pivot:
                break
        if i >= j:
            return j
        list[i], list[j] = list[j], list[i]

def selectionSort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
    return list

def insertionSort(list):
    for i in range(1, len(list)):
        item = list[i]
        j = i-1
        while j >= 0 and item < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = item
    return list

if __name__ == "__main__":
    main()
