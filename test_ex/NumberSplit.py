from timeit import timeit
def numberSplit(num):
    total_1 = num // 2
    all_num = []
    if  num % 2 != 0:
        total_2 = total_1 + 1
    else:
        total_2 = total_1
    all_num.append(total_1)
    all_num.append(total_2)
    
    return all_num

def numberSplit2(num):
    a = [num//2,num//2 + num % 2]
    return a



times_numberSplit = timeit(lambda:numberSplit(20),number=10000000)
times_numberSplit2 = timeit(lambda:numberSplit2(20),number=10000000)

print(times_numberSplit)
print(times_numberSplit2)



