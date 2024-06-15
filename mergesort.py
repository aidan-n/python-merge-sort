def mergeSort(array):
    if len(array) > 1:

        
        halfway = len(array)//2
        l = array[:halfway]
        r = array[halfway:]

        # Sort the two halves
        mergeSort(l)
        mergeSort(r)

        i = 0
        j = 0
        k = 0

        # Until the end of l or r is reached, pick the larger among
        # elements in l and r and place them in the correct position
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        # When l or r have been exhausted,
        # pick the remaining elements and insert them
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':
    array = [5, 1, 2, 4, 8, 9, 3]

    mergeSort(array)

    print("Sorted array: ")
    printList(array)