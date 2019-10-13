def  luckyNumbers(num, target):
    global ans
    ans = []

    def recursive(num, target, prev, cur, index, path):
        global ans
        if index == len(num):
            if cur == 0 and target - prev == 0:
                ans.append(path)
            return
        
        cur = cur * 10 + int(num[index])
        if not path:
            recursive(num, target, cur, 0, index + 1, path + str(cur))
        else:
            recursive(num, target - prev, cur, 0, index + 1, path + '+' + str(cur))
            recursive(num, target - prev, -cur, 0, index + 1, path + '-' + str(cur))
            recursive(num, target, prev * cur, 0, index + 1, path + '*' + str(cur))

            if cur != 0 and prev % cur == 0:
                recursive(num, target, prev / cur, 0, index + 1, path + '/' + str(cur))
            
        if cur != 0:
            recursive(num, target, prev, cur, index + 1, path)

    recursive(num, target, 0, 0, 0, "")
    return ans

print(luckyNumbers("123456", 1000))
