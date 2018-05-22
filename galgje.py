import random

# HANGMAN = (
# """
# -----
# |   |
# |
# |
# |
# |
# |
# |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# |
# |
# |
# |
# |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# |  -+-
# |
# |
# |
# |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# | /-+-
# |
# |
# |
# |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# | /-+-\
# |
# |
# |
# |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# | /-+-\
# |   |
# |
# |
# |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# | /-+-\
# |   |
# |   |
# |
# |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# | /-+-\
# |   |
# |   |
# |  |
# |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# | /-+-\
# |   |
# |   |
# |  |
# |  |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# | /-+-\
# |   |
# |   |
# |  | |
# |  |
# |
# --------
# """,
# """
# -----
# |   |
# |   0
# | /-+-\
# |   |
# |   |
# |  | |
# |  | |
# |
# --------
# """)

print('vul je eerste letter in')
woorden = ("tjiftjaf","grafeem","maquette","kitsch","pochet","convocaat","jakkeren","cesium","hyenavel","dehydreren","sige")
woord = random.choice(woorden)
correct = 0 #geraden of niet
lg = 0 #aantal letters goed
#print(woord)
#print(str(len(woord))) #lengte van het woord / aantal letters
plek = [0]*len(woord)
levens = 6

while lg != len(woord) and levens > 0:
    invoer = input()
    letter = invoer[0]
    if letter in woord:
        pl1 = woord.find(letter)  # levert -1 als de letter niet gevonden is
        plek[pl1] = letter
        pl2 = woord.find(letter, pl1 + 1)  # levert -1 als de letter niet gevonden is
        lg = lg + 1
        print(plek)
        if pl2 != -1:
            plek[pl2] = letter
            print(plek)
            lg = lg + 1
            pl3 = woord.find(letter, pl2 + 1)
            if pl3 != -1:
                plek[pl2] = letter
                print(plek)
                lg = lg + 1

    else:
        print('je hebt nog: ', levens-1,' poging(en) over')
        levens = levens - 1

if lg == len(woord):
    print('je hebt het woord geraden')
elif levens == 0:
    print('het woord was', woord)