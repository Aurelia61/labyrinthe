# print("+--" *40,"+", sep="" )
# for i in range(10) :
#     print("|  ","   "*38,"   |", sep="" )
#     print("+  ","   "*38,"   +", sep="" )
# print("+--" *40,"+", sep="" )

# print("+--" *40,"+", sep="" )
# for i in range(10) :
#     print("|  ","   "*38,"   |", sep="" )
#     print("+  ","   "*38,"   +", sep="" )
# print("+--" *40,"+", sep="" )


# chaine = "|        |\n+        +"
# print(chaine)
# liste = list(chaine.strip())
# print(liste)



# ████████████████████
# █ ██████████████████
#   ██████████████████
# █ █████████    
# █ █████████ ████████
# █ █████████ ████████
# █ █         ████████
# █ █ ████████████████
# █   ████████████████
# ████████████████████

labyrinth = [["█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
             ["█"," ","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
             [" "," ","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
             ["█"," ","█","█","█","█","█","█"," "," "," "," "," "," "," "," ","█","█","█","█"],
             ["█"," ","█","█","█","█","█","█"," ","█","█","█","█","█","█"," ","█","█","█","█"],
             ["█"," ","█","█","█","█","█","█"," ","█","█","█","█","█"," "," ","█","█","█","█"],
             ["█"," ","█"," "," "," "," "," "," ","█","█","█","█","█"," ","█","█","█","█","█"],
             ["█"," ","█"," ","█","█","█","█","█","█","█","█","█","█"," ","█","█","█","█","█"],
             ["█"," "," "," ","█","█","█","█","█","█","█","█","█","█"," ","█","█","█","█","█"],
             ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"," ","█","█","█","█","█"]]





displayMap=map("".join,labyrinth)
print("\n".join(displayMap))