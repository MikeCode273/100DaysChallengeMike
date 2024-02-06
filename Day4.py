#Creating loops

#fruits = ["Apple","Peach","Pear"]

#declaring the for loop
#for fruit in fruits:
##  print(fruit)
  #print(fruit +" false")
#print(fruits)
 
 
student_heights= input("Input a list of student heights ").split()

for n in range(0,len(student_heights)):
  student_heights[n]=int(student_heights[n])

print(student_heights)

#finding the sum of the heigth
total_height =0
for height in student_heights:
  total_height+=height
print(f"Total number of student height are {total_height}\n")

#finding the length of thr height using for loops
total_length =0
for length in student_heights:
  total_length += 1
print(f"The size of the list is {total_length}\n")

#Averaget height equal total height divided by the total size of student height
average_height = round(total_height/total_length)
print(f"The Average Height of the Student is {average_height}")