def quick_Sort(data_list):
    quick_Sort_hlp(data_list,0,len(data_list)-1)

def quick_Sort_hlp(data_list,first,last):
    if first < last:
        splitpoint = partiton(data_list,first,last)
        quick_Sort_hlp(data_list,first,splitpoint-1)
        quick_Sort_hlp(data_list,splitpoint+1,last)

def partiton(data_list,first,last):
    pivotvalue = data_list[first]

    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        pass
        
        
