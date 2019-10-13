def  formPolygon(sticks, sides):
    if sides <= 2 or len(sticks) < sides or sum(sticks) % sides != 0:
        return False

    edge_length = sum(sticks) / sides

    def recursive(sticks, index, edge, edge_length):
        if index == len(sticks):
            return min(edge) == max(edge)
        
        res = False
        for i in range(len(edge)):
            if edge[i] + sticks[index] <= edge_length:
                edge[i] += sticks[index]
                res = res or recursive(sticks, index + 1, edge, edge_length)
                edge[i] -= sticks[index]
        return res
    
    return recursive(sticks, 0, [0] * sides, edge_length)

print(formPolygon([1,2,3,2,1], 3))