VacationsSpots = ["London","Paris","New York","Utah","iceland"]
VacationFile = open("VacationPlaces","w")

for Spots in VacationsSpots:
    VacationFile.write(Spots + "\n")

VacationFile.close()

VacationFile = open("VacationPlaces","r")

# TheWholeFile = VacationFile.read()

# print(TheWholeFile)

FirstLine = VacationFile.readline()
print(FirstLine)
SecondLine = VacationFile.readline()
print(SecondLine)
for line in VacationFile:
    print(line, end= "")

VacationFile.close()

FinalSpot = "Thailand\n"

VacationFile = open("VacationPlaces","a")
VacationFile.write(FinalSpot)
VacationFile.close()

VacationFile = open("VacationPlaces","r")
for line in VacationFile:
    print(line, end = "")

VacationFile.close()

with open("VacationPlaces","r") as VacationFile:
    for line in VacationFile:
        print(line)