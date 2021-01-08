"""

programmer: Felix Perez
Homework Assignment #6: DictionariesAndSets

*This program print in the screen the content of the a Dictionary and evaluate if the key and the value exists.

"""

favoriteSong = {"Artist":"Moby","YearRelease":2005,"Genre":"Pop Rock, Electronic","DurationMin":3.14,"Title":"Lift Me Up","Album":"Hotel","Recorded":2004}

for keys in favoriteSong:
    print(keys,":",favoriteSong[keys])

def evaluateFavoriteSong(findKeys,findValues):
    Output = False
    for keys in favoriteSong:
        if keys == findKeys and favoriteSong[keys] == findValues:
            Output = True
    return Output


respon = evaluateFavoriteSong("Artist","Moby")
print(respon)
respon = evaluateFavoriteSong("Artist","2020")
print(respon)
respon = evaluateFavoriteSong("Cost","Moby")
print(respon)