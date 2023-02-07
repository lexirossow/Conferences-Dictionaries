#Programming Assignment 4
#Lexi Rossow
#February 6, 2023
#Dictionaries of the football conferences and mascots


#dictionaries


#SEC dictionaries
SEC = {"Georgia":"Bulldogs",
       "Auburn":"Tigers",
       "Tennessee":"Volunteers",
       "Mississippi States":"Bulldogs",
       "Florida":"Gators"
       }

ACC = {"Central Florida":"Knights",
       "Florida States":"Seminoles",
       "Georgia Tech":"Yellow Jackets",
       "South Florida":"Bulls",
       "Miami":"Hurricanes"
       }

FIFA = {"Inter Milan":"Serpents",
        "West Ham":"Bubbles",
        "Juventus":"Zebras",
        "Leeds":"Kop Cat",
        "Manchester United":"Red Devils"
        }


#list of dictionaries
conferences = ["SEC",
               "ACC",
               "FIFA"
               ]

#list of conferences as variables
conferencesV = [SEC, ACC, FIFA]


#print the listo f conferences using a for loop with implicit key iteration
for conference in conferences:
    print()
    print(f"\tTeams in the {conference} dictionary: ")
    indexConf = conferences.index(conference)
    print()

    for college in conferencesV[indexConf]:
        print(f"\t{college}'s mascot is the {conferencesV[indexConf][college]}")


#print the list of conferences using a for loop with implicit key iteration
#SEC
print()
print("Teams in the", conferences[0], "dictionary: ")
print()
for team, mascot in SEC.items():
    print(team + "'s mascot is the " + mascot + "!")
print()

#ACC
print()
print("Teams in the", conferences[1], "dictionary: ")
print()
for team, mascot in ACC.items():
    print(team + "'s mascot is the " + mascot + "!")
print()

#FIFA
print()
print("I added a new dictionary of", conferences[2], "teams and mascots to my list of conferences: ")
print()
for team, mascot in FIFA.items():
    print(team + "'s mascot is the " + mascot + "!")

#prompt the user for a dictionary to search
print()
print()
userDictionary = input("Which dictionary do you want to search? ")
userDictionaryUpper = userDictionary.upper()
userTeam = input("What is the name of the team? ")
userTeamTitle = userTeam.title()
print()
print()

if userDictionaryUpper == "SEC":
    print(userTeamTitle + "'s mascot is the " + SEC.get(userTeamTitle) + "!")
elif userDictionaryUpper == "ACC":
    print(userTeamTitle + "'s mascot is the " + ACC.get(userTeamTitle) + "!")
elif userDictionaryUpper == "FIFA":
    print(userTeamTitle + "'s mascot is the " + FIFA.get(userTeamTitle) + "!")


#prompt the user for a name of a team to delete from the ACC conference
print()
print()
userRemove = input("Which team in the ACC would you like to remove? ")
userRemoveTitle = userRemove.title()
print()
print("The", userRemoveTitle, ACC.get(userRemoveTitle), "have been dropped from the conference.")
removedTeam = ACC.pop(userRemoveTitle)
print()
print()
print("This is the updated", conferences[1], "dictionary: ")
for team, mascot in ACC.items():
    print(team + "'s mascot is the " + mascot + "!")





