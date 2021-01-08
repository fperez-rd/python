"""

programmer: Felix Perez
Homework Assignment #3: "If" Statements

*This program use conditional statements to compare three parameters and return true if one parameter is equal of them others or false if the three parameter are distinct.

"""

def compare(one,two,three):

    output = False

    if int(one) == int(two) or int(one) == int(three) or int(two) == int(three):
        output = True
    else: output = False

    return output

one, two, three = 1, 2, 3

output = compare(one,two, three)

print(output)