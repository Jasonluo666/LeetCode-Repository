def dfs(arr, index, _max):
	if index >= len(arr):
		return True
	
	if _max is not None and _max <= arr[index]:
		return False
	
	return dfs(arr, (index + 1) * 2 - 1, arr[index]) and dfs(arr, (index + 1) * 2, arr[index])

def  isMaxHeap(arr):
	return dfs(arr, 0, None)