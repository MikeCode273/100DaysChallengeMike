count = 0
while count< 10:
    print('The condition is TRUE!')
    count = count + 1 

print("After the loop")   

items = [1,2,3,4,5]

for index, item in enumerate(items):
    print(index,item)


items = [1,2,3,4,5]
for  item in items:
    if item == 2:
        break
    print(item)    