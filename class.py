# class ClassName:
#     def __init__(self):
#         self.Attribute = 0

#     def AnotherFunction(self):
#         Actions(s)

class Team:
    def __init__(self,Name,Origin):
        self.TeamName = Name
        self.TeamOrigin = Origin
    def DefineTeamName(self,Name):
        self.TeamName = Name
    def DefineTeamOrigin(self,Origin):
        self.TeamOrigin = Origin


Team1 = Team("pruebaA","pruebaB")
print(Team1.TeamName)
print(Team1.TeamOrigin)

Team1.DefineTeamName("PruebaC")
Team1.DefineTeamOrigin("PruebaD")

print(Team1.TeamName)
print(Team1.TeamOrigin)