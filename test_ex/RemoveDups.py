def removeDups(text):
    total = []
    for i  in text:
        if i not in total:
            total.append(i)
    return total
            

print(removeDups([1,0,1,0]))
print(removeDups(['The','big','cat']))
print(removeDups(['John','Taylor','John']))