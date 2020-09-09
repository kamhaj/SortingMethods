'''
compare sorting methods efficiency
'''

from sorting_algorithms import selection_sort

def main():
    nums = [5, 3, 8, 2, 9, 7]

    print("SELECTION SORT:")
    print(selection_sort.selection_sort(nums) )



if __name__ == "__main__":
    main()