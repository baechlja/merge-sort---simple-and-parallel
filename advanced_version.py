import time
import multiprocessing
import random
import matplotlib.pyplot as plt


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


def merge_wrap(left_list_and_right_list):
    """" this function assigns each one to its corresponding variable and does the merge() """
    left_partition, right_partition = left_list_and_right_list
    return merge(left_partition, right_partition)


def merge_sort_parallel(list_to_sort):
    """ this function uses multiprocessing"""
    processes = 4  # gives back the number of cores
    pool = multiprocessing.Pool(processes=processes)  # set the number of processes created/used as the number of cores
    size = len(list_to_sort)  # number of elements in each chunk
    # divide into chunks to get iterable for Pool.map()
    chunk_list = [list_to_sort[item:item + size] for item in range(0, len(list_to_sort), size)]
    sorted_sub_list = pool.map(merge_sort, chunk_list)  # We do merge sort of each chunk in the list
    # we need to merge() each one of the chunks to finish the algorithm.
    while len(sorted_sub_list) > 1:
        # make a merge of each neighbor chunk, so that if we have an odd number of chunks
        # perform the last merge of that chunk with the chunk of all the previous merge
        # merge of all the neighboring chunks (from tuple to tuple) until only 1 chunk remains.
        chunk_list = [(sorted_sub_list[i], sorted_sub_list[i + 1]) for i in range(0, len(sorted_sub_list) - 1, 2)]
        sorted_sub_list = pool.map(merge_wrap, chunk_list)
    # All the chunks have been combined into a single list, so in the first index we have the result
    return sorted_sub_list[0]


def run_merge_sort():
    """run the simple merge sort"""
    #print("Starting simple merge sort")
    #print("Unsorted list: ", unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    #print("Simple Sorted list: ", sorted_list)


def run_merge_sort_parallel():
    """run the parallel merge sort"""
    #print("Starting parallel merge sort")
    #print("Unsorted list: ", unsorted_list)
    sorted_list = merge_sort_parallel(unsorted_list)
    #print("Parallel Sorted list: ", sorted_list)


if __name__ == "__main__":
    input_list_sizes = []
    execution_time_simple = []
    execution_time_parallel = []
    for i in range(11):  # loop the input list n times to create for every loop a bigger list
        list_size = 5 ** i  # use list_size to create a n**i bigger list
        input_list_sizes.append(i)
        unsorted_list = [random.randint(-10000, 10000) for i in range(list_size)]  # create a random list to sort it

        # Start the simple merge sort

        start_time_simple = time.time()
        run_merge_sort()
        end_time_simple = time.time()
        executed_simple = end_time_simple - start_time_simple
        execution_time_simple.append(executed_simple)
       # print("Executed for: ", executed_simple, "sec")

        # Start the parallel merge sort

        start_time_parallel = time.time()
        run_merge_sort_parallel()
        end_time_parallel = time.time()
        executed_parallel = end_time_parallel - start_time_parallel
        execution_time_parallel.append(executed_parallel)
       # print("Executed for: ", executed_parallel, "sec")

    # visualize the results of simple merge osrt and parallel merge sort
    plt.xlabel("List size")
    plt.ylabel("Execution time")
    plt.plot(input_list_sizes, execution_time_simple)
    plt.plot(input_list_sizes, execution_time_parallel)
    plt.legend(["simple", "parallel"], loc=2)
    plt.show()
