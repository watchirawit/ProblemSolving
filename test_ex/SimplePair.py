def simplePair(num,sums):
    total = []
    k = 0
    o = 1
    for i,n in enumerate(num):
        if i != 2:
            if i == 0:
                while k < 2:
                    k += 1
                    if n * num[o] == sums:
                        total.append(n)
                        total.append(num[o])
                        o = 0
                        k = 2
                    else:
                        o +=1
            else: 
                if n * num[i + 1] == sums:
                    total.append(n)
                    total.append(num[i+1])

    return total if len(total) != 0 else 'null'



print(simplePair([1,2,3],9))
print(simplePair([1,2,3],6))
print(simplePair([1,2,3],3))
        


        
        
    
        

