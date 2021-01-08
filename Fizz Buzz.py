"""

programmer: Felix Perez
Homework Assignment #5: Basic Loops

*This program print the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".

"""
def PrimeNumber(numbers):
    evaluate = numbers-1
    prime = True

    while evaluate > 1:
        if numbers%evaluate == 0:
            prime = False
            break
        evaluate -= 1
    
    if prime == True and numbers > 1:
        prime = "prime"
    else:
        prime = ""

    return prime


def FizzBuzz():
    for numbers in range(1,101):

        if numbers%3 == 0 and numbers%5 == 0:
            print(numbers,"FizzBuzz",PrimeNumber(numbers))
        elif numbers%3 == 0:
            print(numbers,"Fizz    ",PrimeNumber(numbers))
        elif numbers%5 == 0:
            print(numbers,"Buzz    ",PrimeNumber(numbers))
        else:
            print(numbers,"        ",PrimeNumber(numbers))


FizzBuzz()