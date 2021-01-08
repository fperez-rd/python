"""

programmer: Felix Perez
Homework Assignment #2: Functions

*This program use funcion to return the attributes of a song and use function to prints them on the screen.

"""

# An artist is a person engaged in an activity related to creating art, practicing the arts, or demonstrating an art.
def artist():
    Artist = "Moby"
    return Artist

# The action of making a film, recording, or other product available to the public.
def year():
    Year = 2005
    return Year

# Genre (from French genre 'kind, sort') is any form or type of communication in any mode (written, spoken, digital, artistic, etc.) with socially-agreed-upon conventions developed over time.
def genre():
    Genre = "Pop Rock, Electronic"
    return Genre

"""
data type boolean use

"""

# An artist is a person engaged in an activity related to creating art, practicing the arts, or demonstrating an art.
def artistType():
    Output = type(artist()) == str 
    return Output

# The action of making a film, recording, or other product available to the public.
def yearType():
    Output = type(year()) == str 
    return Output

# Genre (from French genre 'kind, sort') is any form or type of communication in any mode (written, spoken, digital, artistic, etc.) with socially-agreed-upon conventions developed over time.
def genreType():
    Output = type(genre()) == str 
    return Output

# declare variables to assign the return of function

Artist = artist()
ArtistType = artistType()
Year = year()
YearType = yearType()
Genre = genre()
GenreType = genreType()

# print in CLI

print(Artist)
print("The variable Artist is a string?",ArtistType)
print(Year)
print("The variable is a string?",YearType)
print(Genre)
print("The variable is a string?",GenreType)