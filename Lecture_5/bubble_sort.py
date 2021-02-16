def bubble_Sort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            print(i,end=' ')
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
            
nlist = [14,46,43,27,57,41,45,21,70]
bubble_Sort(nlist)
print(nlist)