#using for loops to find the highest score
student_scores = input("Input a list of student scores(1-100): ").split()
for n in range(0,len(student_scores)):
  student_scores[n]= int(student_scores[n])
print(student_scores)

#Higest score
max_value =0
for i in student_scores:
  if i>max_value:
    max_value=i
print(f"The Highest score is {max_value}")

#lowest score     
min_value = 100
for x in student_scores:
  if x<min_value:
    min_value=x
print(f"The lowest score is {min_value}")

