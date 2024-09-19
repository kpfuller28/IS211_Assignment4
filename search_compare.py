import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False
    startTime = time.perf_counter()

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    endTime = time.perf_counter() - startTime
    return found, endTime


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    startTime = time.perf_counter()
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    endTime = time.perf_counter() - startTime
    return found, endTime


def binary_search_iterative(a_list, item):
    first = 0
    startTime = time.perf_counter()

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    endTime = time.perf_counter() - startTime
    return found, endTime


def binary_search_recursive(a_list, item, startTime=None):
    if startTime is None:
        startTime = time.perf_counter()
    if len(a_list) == 0:
        endTime = time.perf_counter() - startTime
        return False, endTime
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            endTime = time.perf_counter() - startTime
            return True, endTime
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item, startTime)
            else:
                return binary_search_recursive(a_list[midpoint + 1 :], item, startTime)


if __name__ == "__main__":
    """Main entry point"""
    sizes = [500, 1000, 5000]

for j in sizes:
    totalTime = {
        "binaryIterative": 0,
        "binaryRecursive": 0,
        "sequential": 0,
        "orderedSequential": 0,
    }
    the_size = j
    for i in range(100):
        mylist = get_me_random_list(the_size)
        # sorting is not needed for sequential search.
        check = sequential_search(mylist, 99999999)
        totalTime["sequential"] += check[1]

        mylist = sorted(mylist)
        check = ordered_sequential_search(mylist, 99999999)
        totalTime["orderedSequential"] += check[1]
        check = binary_search_iterative(mylist, 99999999)
        totalTime["binaryIterative"] += check[1]
        check = binary_search_recursive(mylist, 99999999)
        totalTime["binaryRecursive"] += check[1]

    averageTimes = {
        "binaryIterative": totalTime["binaryIterative"] / 100,
        "binaryRecursive": totalTime["binaryRecursive"] / 100,
        "sequential": totalTime["sequential"] / 100,
        "orderedSequential": totalTime["orderedSequential"] / 100,
    }
    print(
        f"Binary Search Iterative took {averageTimes['binaryIterative']:10.7f} seconds to run, on average for a list of {the_size} elements"
    )
    print(
        f"Binary Search Recursive took {averageTimes['binaryRecursive']:10.7f} seconds to run, on average for a list of {the_size} elements"
    )
    print(
        f"Sequential Search took {averageTimes['sequential']:10.7f} seconds to run, on average for a list of {the_size} elements"
    )
    print(
        f"Ordered Sequential Search took {averageTimes['orderedSequential']:10.7f} seconds to run, on average for a list of {the_size} elements\n"
    )
