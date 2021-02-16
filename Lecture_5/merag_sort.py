def merag_Sort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        
        merag_Sort(lefthalf)
        merag_Sort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i+=1
            else:
                nlist[k]=righthalf[j]
                j+=1
            k+=1
        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j+=1
            k+=1

    print('Merging',nlist)
nlist = [14,46,43,27,57,41,21,70]
merag_Sort(nlist)
print(nlist)