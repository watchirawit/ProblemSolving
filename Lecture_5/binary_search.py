def binary_Search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while(first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item:
            found = 'True this is you index find ' + str(item_list.index(item))

        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if type(found) == bool:
        found = 'Not found'
    
    return found 

print(binary_Search([1,2,3,5,8],6))
print(binary_Search([1,2,3,5,8],5))