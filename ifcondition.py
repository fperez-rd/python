# if condition:
#     Action

click = False

Like = 0

click = True

if click == True:
    Like += 1
    click = False

print(Like)

Temperature = 20
Thermo = 15
print(Thermo)

if Temperature <= 15:
    Thermo += 5

print(Thermo)

if Temperature >= 20:
    Thermo -= 3

print(Thermo)

Time = "Night"
Sleepy = True
Pajamas = "Off"
InBed = True

if Time == "Night" and Sleepy == True:
    Pajamas = 'On'
elif Time == "Morning":
    Pajamas = 'On'
else:
    Pajamas = "Off"

print(Pajamas)

click = True
Like = 0                      
if click:
    Like = Like + 1           
print(Like)
