from functools import reduce

items_cost = [999, 888, 1100, 1200, 1300, 777]
lowest = reduce(lambda x,y: x if x > y else y, items_cost)
sum_ = reduce(lambda x, y: x+y, items_cost)
print(sum_)
