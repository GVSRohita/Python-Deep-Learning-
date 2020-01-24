# function which return reverse of a string
s = input("Enter a word : ");
s=s.casefold()
har = s[::-1]
if(s==har):
    print("yes, it is a palindrome")
else:
    print("no, it is not a palindrome")
