def merge_sort(array):
    """this function splits the input list into a left partition and right partition"""
    list_length = len(array)  # store the length of the list

    if list_length == 1:
        return array

    mid_point = list_length // 2  # finding the midpoint from the list

    left_partition = merge_sort(array[:mid_point])  # dividing the list in a right and left half
    right_partition = merge_sort(array[mid_point:])
    return merge(left_partition, right_partition)


def merge(left, right):
    """this function takes 2 lists and returns a sorted list"""
    output = []  # creating an empty output list
    i = j = 0  # initializing i and j as pointers

    while i < len(left) and j < len(right):  # while loop as long as pointers are less than the length of the lists
        if left[i] < right[j]:  # comparing the left and right elements at every position
            output.append(left[i])  # output is filled with smaller value
            i += 1  # pointer to right
        else:
            output.append(right[j])  # output is filled with the smaller value
            j += 1  # pointer to the right
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def run_merge_sort():
    """run the simple merge sort"""
    unsorted_list = [4, 1, 7, 6, 18, 6, 10, 33, 5, 7, 23, 89, 2, 16, 500]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)


run_merge_sort()
