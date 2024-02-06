#Using range in for loops

#Sum up all even numbers from 1 - 100
total= 0
for number in range(0,101,2):
  total+=number
print(f"The sum of all Even numbers between (0- 100): {total}")