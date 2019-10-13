def  findSubArrays(arr):
    hashmap = {0: [-1]}
    _sum = 0
    ans = []

    for index in range(len(arr)):
        _sum += arr[index]

        if _sum in hashmap:
            for x in hashmap[_sum]:
                ans.append([x + 1, index])
            hashmap[_sum].append(index)
        else:
            hashmap[_sum] = [index]
    return sorted(ans)