global ans
ans = []

def  recursive(elements, index, K, path):
    global ans
    # problem: K == 0
    if K == 0:
    	ans.append(path)
        return

    # problem: index == length || K < 0
    if index == len(elements) or K < 0:
    	return
    
    # if index == len(elements):
    #     if K == 0:
    # 	    ans.append(path)
    # 	return
    
    recursive(elements, index + 1, K - elements[index], path + [elements[index]])

    temp = index + 1
    while len(elements) > temp > 0 and elements[temp] == elements[temp - 1]:
        temp += 1
    recursive(elements, temp, K, path)

def  subsetSums(elements, K):
	global ans
	ans = []
	elements = sorted(elements)
	recursive(elements, 0, K, [])
	return ans

print(subsetSums([1,1,2,2,3,3,4,4], 10))