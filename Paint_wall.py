#first and second lines of code will accept input of height and width of the wall
test_h=int(input("Height of the wall:"))
test_w=int(input("Width of the wall:"))
coverge=5

def paint_wall(height,width,cover):
  number_of_can=round((height*width)/cover)
  print(f"You will need need {number_of_can} can of paint.")


paint_wall(height=test_h,width=test_w,cover=coverge)