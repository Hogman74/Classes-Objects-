
# python program to
# demonstrate defining
# a student class

class Student:
def __init__(self, name, age, tracks, score):

# user_input
self.name = name
self.age = age
self.tracks = tracks
self.score = score

def introduce_self(self):
print ("My name is " + Student_name)
print ("My age is ", Student_age)
print ("My tracks are " + Student_track)
print ("My score is ", Student_score)

# get Student input
Student_name = input("Student name ")
Student_age = int(input("Student age "))
Student_track = input(["Student tracks"])
Student_score = float(input("Student score "))

# running output
Student.introduce_self("self")
