# import sys #voor mario

'''
##Hello

print('Hello, world!\n')


##Water
print('Vul AUB in hoeveel minuten je onder de douche hebt gestaan')
minuten = int(input())
print('aantal minuten onder de douche: ',minuten)
flessen = minuten*12

print('aantal flessen kunnen vullen: ', flessen,'\n')


##mario
print('vul een getal in')

#als je gebruik wilt maken van pycharm
#invul = int(input())

# voor in de powershell
invul = int(sys.argv[1])    #1 staat  voor de 2e input na 'python'.
print('hoogte = ',invul)
i = 0
done = 0

while done != 1:
    if invul > 0 and invul <= 23:
        for i in range(invul):
            i = i + 1
            s = invul - i
            print(s*' '+i*'#'+'#')
        done = 1
    else:
        print('vul een geldig getal in')
        invul = int(input())



##mario dubbel
print('vul een getal in')
invul = int(input())
print('hoogte = ',invul)
done = 0

while done != 1:
    if invul > 0 and invul <= 23:
        for i in range(invul):
            i = i + 1
            s = invul - i
            print(s*' '+i*'#'+'# '+'#'+i*'#')
            done = 1
    else:
        print('vul een geldige waarde in')
        invul = int(input())

'''


##munten wisselaar
print("Vul in hoeveel wisselgeld je krijgt (in euro's)")
invul = 100*float(input())
invul = round(invul)
print('Zoveel wisselgeld: ',invul)
teller = 0
#mogelijke munten: 1,2,5,10,20,50

while invul / 50 >= 1:
    invul = invul - 50
    teller = teller + 1

while invul / 20 >= 1:
    invul = invul - 20
    teller = teller + 1

while invul / 10 >= 1:
    invul = invul - 10
    teller = teller +1

while invul / 5 >= 1:
    invul = invul - 5
    teller = teller + 1

while invul / 2 >= 1:
    invul = invul - 2
    teller = teller + 1

while invul / 1>= 1:
    invul = invul - 1
    teller = teller +1

print('Zoveel munten nodig: ',teller)