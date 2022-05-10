def twoNumberSum(array, targetSum):
  # Sorting the array with QuickSort
  array.sort()
  
  result = []
  i = 0
	j = len(array) - 1
	while result == [] and i < j:
		localSum = array[i] + array[j]
		if localSum == targetSum:
			result = [array[i], array[j]]
		if localSum < targetSum:
			i += 1
		if localSum > targetSum:
			j -= 1
    return result
