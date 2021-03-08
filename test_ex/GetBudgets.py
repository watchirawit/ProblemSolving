def getBudgets(Budgets):
    budget = []
    total  = {} 
    for i in Budgets:
       total.update(dict(i))
       budget.append(total['budget'])
    return sum(budget)

    
print(getBudgets([{'name':'John','age':21,'budget':23000},
{'name':'Steve','age':32,'budget':40000},
{'name':'Martin','age':16,'budget':2700}]))


print(getBudgets([{'name':'John','age':21,'budget':29000},
{'name':'Steve','age':32,'budget':32000},
{'name':'Martin','age':16,'budget':1600}]))
