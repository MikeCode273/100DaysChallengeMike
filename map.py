# mapping
number = [1, 2, 3,4,5,6,7,8]


result = map(lambda a : a*2, number) 

print(list(result))

#filtering



result = filter(lambda n : n%2 ==0, number)

print(list(result))


