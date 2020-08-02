# Basic Variables
myFirstVariable = 5 # int
print(myFirstVariable)
myFirstVariable = 6.7 # float
print(myFirstVariable)
myFirstString = 'this is a string'
print(myFirstString)
myBoolean = (4 < 5)
print(myBoolean)

# Variable Operations
x = 5; y = 7
y = y + 1; y -= 1
z = x + y; print('z = ' + str(z))
w = x - y; print('w = ' + str(w))
a = w * z; print('a = ' + str(a))
b = w / z; print('b = ' + str(b))

# Boolean Logic
myFirstBool = (4 == 5)
mySecondBool = (56 * 4 < 65 * 5)
print(myFirstBool)
print(mySecondBool)
print(myFirstBool and mySecondBool)
print(myFirstBool or mySecondBool)
print(not myFirstBool)
myFirstBool = (4 <= 5 and (5 >= 4 or not 6 == 7))
print(myFirstBool)

# Lists
myFirstList = [1, 2, 3, 4]; print(myFirstList[0])
print(myFirstList[-1])
myFirstList[3] = 5; print(repr(myFirstList))
myFirstList.append(5); print(repr(myFirstList))

# More List Operations
print('last two: ' + repr(myFirstList[3:5]))
print('skipping by twos: ' + repr(myFirstList[0:5:2]))
print('first two: ' + repr(myFirstList[:2]))
print('3rd item onwards: ' + repr(myFirstList[2:]))

# Nested Lists
listInList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listInList[0][1])
print(len(listInList))

# Sets
myFirstList = [1, 2, 3, 5, 5]
print(set(myFirstList))
mySecondList = [1, 2, 3, 5, 6]
print(set(myFirstList).intersection(set(mySecondList)))

# Strings
sentence = 'I love natural language processing.'
splitSentence = sentence.split()
print(repr(splitSentence))
sentenceJoinedBackTogether = ' '.join(splitSentence)
print(sentenceJoinedBackTogether)
print(sentenceJoinedBackTogether[1:5])

# Loops
for i in range(10):
 print(i)
for number in myFirstList:
 print(number+1)
for i in listInList:
 for j in i:
   print(j)

# Conditional Statements
myStatement = (54 < 18 * 3)
myOtherStatement = (len('yes') == 3)
if(myStatement == False):
  print('myStatement is false!')
elif(myOtherStatement == True):
  print('myOtherStatement is true!')
else:
  print('haha nope')

# Functions
def average(numbers):
  total = 0
  for i in numbers:
    total += i
  return total/len(numbers)

print(average([1, 2, 3, 4, 5, 6]))

# List Comprehension
slightlyFancyList = [i for i in range(12)]
print(repr(slightlyFancyList))
slightlyFancierList = [i for i in range(12) if not i == 4]
print(repr(slightlyFancierList))
reallyFancyList = [average(i) for i in listInList if average(i) > 3]
print(repr(reallyFancyList))
