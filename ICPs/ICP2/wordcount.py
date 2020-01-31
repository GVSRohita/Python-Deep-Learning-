#One way to do wordcount in a file for each line

# f = open("sample.txt","r")
#
# worddic ={}
# words = []
# count=0
# for i in f.read().split():
#     words.append(i)
# print(words)
# for word in words:
#     try:
#         worddic.update({word:worddic[word]+1})
#     except:
#         worddic[word] = 1
#
#
# print(worddic)


#Another way to do wordcount in a file for each line

#Open sample text file
f = open("sample.txt","r")

#Opening output file to store the results
outputfile = open("output.txt","w")

worddic ={}
words = []
count=0

#Spliting  of each line into word from the file and appening as a list
for i in f.read().split():
    words.append(i)
print(words)

#Logic to find word count
for word in words:
    if word in worddic.keys():
        worddic.update({word:worddic[word]+1})
    else:
        worddic.update({word:1})

print(worddic)
# outputfile.write(str(worddic))

#Looping to making the result in a formatted way
for k,v in worddic.items():
    outputfile.write("{} {} \n".format(k,v))