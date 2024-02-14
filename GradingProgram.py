student_scores={
  "Harry":81,
  "Ron":78,
  "Hermione":99,
  "Draco":74,
  "Neville":62,
}

#creating an empty dictionary called student 
student_grades={}

for key in student_scores:
  if key=="Harry":
    student_grades["Harry"]="Exceeds expectation"
  elif key=="Ron":
    student_grades["Ron"]="Acceptable"
  elif key=="Hermione":
    student_grades["Hermione"]="Outstanding"
  elif key=="Draco":
    student_grades["Draco"]="Exceeds expectation"
  elif key=="Neville":
    student_grades["Neville"]="Fail"
  
print(student_grades)