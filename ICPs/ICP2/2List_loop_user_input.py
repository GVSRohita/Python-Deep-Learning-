'''Write a program, which reads weights (lbs.) of Nstudents into a list and convert
these weights to kilograms in a separate list using:1) Loops and2)
List comprehensionsN: No of students (Read input from user)
Ex: L1: [150,155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]
'''
# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
print("Please enter",n,"no of weights")
# iterating till the range
for i in range(0, n):
    ele = int(input())
# adding the element
    lst.append(ele)
# printing the list
print("Given the list of weights in the lbs(pounds)",lst)
# converting the student weights from Lbs to Kgs
kgs = [i*0.45359237 for i in lst]
print("Convert list of weights in Kilograms",kgs)

