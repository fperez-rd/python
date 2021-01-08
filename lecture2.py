# def FunctionName (Input):
#     Action
#     return Output

def addOne(Number):
    Number += 1
    return Number

Var = 0
print(Var)
Var2 = addOne(Var)
Var3 = addOne(Var2)
Var4 = addOne(2.1+3.4)
print(Var2)
print(Var3)
print(Var4)

def addOneAddTwo(NumberOne,NumberTwo):
    Output = NumberOne + 1
    Output += NumberTwo + 2
    return Output

Sum = addOneAddTwo(Var2,Var3)

print(Sum)

def hello():
     print("I am a beginner")
hello()
hello()

# def sumA(count):
#      a = count+1
#      return a
# print(a)

def printmessage(message, ntimes = 1):
      print(message * ntimes)
printmessage("Hello")
printmessage("Hello", 5)


num = 1
def func():
     num = 4
     print(num)
func()
print(num)


def addOne(number):
       number += 1
       return number
one = addOne(0)
two = addOne(one)
print(two)