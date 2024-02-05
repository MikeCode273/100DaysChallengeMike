from functools import reduce

expenses = [('dinner',200),('car repair',120)]

sum = reduce(lambda a,b: a[1]+b[1], expenses)

print(sum)