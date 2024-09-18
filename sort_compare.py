import argparse

# other imports go here

import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    startTime = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    endTime = time.time() - startTime
    return endTime


def shellSort(alist):
    startTime = time.time()
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        # print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2
    endTime = time.time() - startTime
    return endTime


def gapInsertionSort(alist, start, gap):

    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    startTime = time.time()
    sorted(a_list)
    endTime = time.time() - startTime
    return endTime


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]
    totalTimes = {
        "pythonSort": 0,
        "shell": 0,
        "insertionSort": 0,
    }

    for the_size in list_sizes:
        for i in range(100):
            myList = get_me_random_list(the_size)

            check = python_sort(myList)
            totalTimes["pythonSort"] += check

            check = shellSort(myList)
            totalTimes["shell"] += check

            check = insertion_sort(myList)
            totalTimes["insertionSort"] += check

        averageTimes = {
            "pythonSort": totalTimes["pythonSort"] / 100,
            "shell": totalTimes["shell"] / 100,
            "insertionSort": totalTimes["insertionSort"] / 100,
        }

        print(
            f"Python sort took {averageTimes['pythonSort']:10.7f} seconds to run, on average for a list of {the_size} elements"
        )
        print(
            f"Insertion sort took {averageTimes['insertionSort']:10.7f} seconds to run, on average for a list of {the_size} elements"
        )
        print(
            f"Shell sort took {averageTimes['shell']:10.7f} seconds to run, on average for a list of {the_size} elements\n"
        )
