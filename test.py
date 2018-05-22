from random import *
import pickle

invoer = open('score.pkl','rb')
hs = int(pickle.load(invoer))
invoer.close()
print('Jouw beste score is', hs,'keer')
antwoord = randint(1,100)
print('Welkom bij hoger-lager')
print('Ben je er klaar voor?')
ready = input()
win = 0
teller = 0

if(ready == "ja"):
    print('Voer jouw eerste getal in')
    while(win != 1):
        test = int(input())
        teller = teller +1
        if(test<antwoord):
            print('hoger')
        elif(test>antwoord):
            print('lager')
        else:
            print('gewonnen')
            win = 1
            print('je deed hier', teller,'keer over')

            if(teller <= hs):
                uitvoer = open('score.pkl','wb')
                pickle.dump(teller, uitvoer)
                uitvoer.close()
                print('wilt u nog een keer spelen? ja/nee')
                check = 0
                while (check != 1):
                    nogmaals = input()
                    if (nogmaals == 'ja'):
                        invoer = open('score.pkl', 'rb')
                        hs = int(pickle.load(invoer))
                        invoer.close()
                        print('Jouw beste score is', hs, 'keer')
                        print('voer jouw eerste getal in')
                        antwoord = randint(1, 100)
                        teller = 0
                        win = 0
                        check = 1
                    elif (nogmaals == 'nee'):
                        print('Dan wellicht een andere keer')
                        win = 1
                        check = 1
                    else:
                        print("Dat was geen 'ja of nee', probeer het nog eens")
                        check = 0

            else:
                print('wilt u nog een keer spelen? ja/nee')
                check = 0
                while(check != 1):
                    nogmaals = input()
                    if(nogmaals == 'ja'):
                        invoer = open('score.pkl', 'rb')
                        hs = int(pickle.load(invoer))
                        invoer.close()
                        print('Jouw beste score is', hs, 'keer')
                        print('voer jouw eerste getal in')
                        antwoord = randint(1,100)
                        teller = 0
                        win = 0
                        check = 1
                    elif(nogmaals == 'nee'):
                      print('Dan wellicht een andere keer')
                      win = 1
                      check = 1
                    else:
                      print("Dat was geen 'ja of nee', probeer het nog eens")
                      check = 0

else:
    print('Dan wellicht een andere keer')