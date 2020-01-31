'''Write a program that returns every other char of a given string starting with first using a function named
“string_alternative”
Str = “Good evening”
Output: Go vnn
Note: You need to create a function named “string_alternative” for
this program and call it from main function.
'''
# Creating a function string_alternative to print the alternative string

str2 = ""

def string_alternative(str):
    bar= ""
    for i in range(len(str)):
        # This % will gives us character at even number of the string
        if i % 2 == 0:
            bar += str[i]
    print(bar)

#the main function is declared
if __name__ == '__main__':
    str = str(input("Please input the string : "))
    print("The given data :", str)
    string_alternative(str)
