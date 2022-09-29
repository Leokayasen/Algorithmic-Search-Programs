def bubbleSort(arr):
	n = len(arr)

	# Check through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

		# Check the array from 0 to n-i-1
		# Swap if the element found is greater
		# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [25, 14, 11, 33, 15, 16, 31, 22]
print("This is the unsorted array")
print(arr)

bubbleSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
	print("%d" %arr[i])
