import random

inFile = open("quotes.txt","r")
##outFile = open("signature.txt","w")

data = []
numLines = inFile.readline()
numLines = int(numLines)
for  i in range(numLines):
    data.append(inFile.readline())

inFile.close()

rnd = random.randint(0,numLines)
lineLen = 56
while len(data[rnd]) > lineLen * 4:
    rnd = random.randint(0,numLines)

if len(data[rnd]) > lineLen * 3:
    print(data[rnd][:lineLen] + "-")
    print(data[rnd][lineLen :lineLen * 2] + "-")
    print(data[rnd][lineLen * 2:lineLen * 3] + "-")
    print(data[rnd][lineLen * 3:])
elif len(data[rnd]) > lineLen * 2:
    print(data[rnd][:lineLen] + "-")
    print(data[rnd][lineLen :lineLen * 2] + "-")
    print(data[rnd][lineLen * 2:])
elif len(data[rnd]) > lineLen:
    print(data[rnd][:lineLen] + "-")
    print(data[rnd][lineLen:])
else:
    print(data[rnd])

##outFile.write(data[rnd])
##outFile.close()
