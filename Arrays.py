dogs = ["Roger",1 , "Syd",True, "Quincy",7]

dogs[2] = "Beau"
dogs.append("judah")
print(dogs[-1])
dogs.extend(["Judah",5])
print(dogs[2:4])

dogs.remove("Quincy")

#sorting list
dogs.sort()
print(dogs)