def totalVolume(*alls):
    lens = len(alls)
    p = 1
    sumnum = []
    for i in range(lens):
        for k in alls[i]:
            j = p * k
            p=j
        sumnum.append(p)
        p = 1   
    return sum (sumnum)

print(totalVolume([4,2,4],[3,3,3],[1,1,2],[2,1,1]))
print(totalVolume([2,2,2],[2,1,1]))
print(totalVolume([1,1,1]))
    