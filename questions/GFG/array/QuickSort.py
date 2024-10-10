# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1
			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	# Return the position from where partition is done
	return i + 1

# function to perform quicksort
def quickSort(array, low, high):
	if low < high:
    	# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)




# def partition(array, start, end):
#     pivot = array[start]
#     low = start + 1
#     high = end

#     while True:
#         # If the current value we're looking at is larger than the pivot
#         # it's in the right place (right side of pivot) and we can move left,
#         # to the next element.
#         # We also need to make sure we haven't surpassed the low pointer, since that
#         # indicates we have already moved all the elements to their correct side of the pivot
#         while low <= high and array[high] >= pivot:
#             high = high - 1

#         # Opposite process of the one above
#         while low <= high and array[low] <= pivot:
#             low = low + 1

#         # We either found a value for both high and low that is out of order
#         # or low is higher than high, in which case we exit the loop
#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#             # The loop continues
#         else:
#             # We exit out of the loop
#             break
#     array[start], array[high] = array[high], array[start]
#     print(low, array[low],"-----------",high, array[high])
#     return high

# def quick_sort(array, start, end):
#     if start >= end:
#         return

#     p = partition(array, start, end)
#     quick_sort(array, start, p-1)
#     quick_sort(array, p+1, end)

# array = [56, 26, 93, 17, 31]
# # array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
# quick_sort(array, 0, len(array) - 1)
# print(array)





# def pivotPlace(lst, start, end):
#     pivot = lst[start]
#     left = start+1
#     right = end

    
#     while True:
#         while left <= right and lst[left] <= pivot:
#             left = left+1
#         while left <= right and lst[right] >= pivot:
#             right = right-1   

#         if right < left:
#             break
#         else:
#             lst[left], lst[right] = lst[right], lst[left]
#     lst[start], lst[right] = lst[right], lst[start]

#     return right

# def QuickSort(lst, start, end):
#     if start < end:
#         p = pivotPlace(lst, start, end)
#         QuickSort(lst, start, p-1)
#         QuickSort(lst, p+1, end)


# # main funtion 
# lst = [56, 26, 93, 17, 31, 44]
# n = len(lst)
# QuickSort(lst, 0, n-1)
# print(lst)
       

