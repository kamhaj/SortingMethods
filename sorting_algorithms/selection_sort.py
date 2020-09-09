'''
we go from start to end, find the minimum (or maximum) value in a list and put it at the beginning
(to avoid simple swapping of all pairs, n times.
'''
import numpy as np  #to use inbuilt min and max functions


def selection_sort(nums_list):
    for i in range(len(nums_list)-1):
        (selected_value, index) = find_min(nums_list, i)
        swap(nums_list, selected_value, index, i)
    return nums_list



def swap(nums_list, selected_value, index, i):         #list is passed by reference
    temp = nums_list[i]
    nums_list[i] = selected_value
    nums_list[index] = temp
    return 0


def find_min(nums_list, start):
    min_value = nums_list[start]
    index = start
    for i in range(start, len(nums_list)-1):
        if nums_list[i+1] <= min_value:
            min_value = nums_list[i+1]
            index = i+1
    return (min_value, index)


def find_max(nums_list, start):
    max_value = nums_list[start]
    index = start
    for i in range(start, len(nums_list)-1):
        if nums_list[i+1] >= max_value:
            max_value = nums_list[i+1]
            index = i+1
    return (max_value, index)
