from tkinter import *

root = Tk() #Tk zorgt voor een 'frame', niets tussen () is gewoon een simpele blanke

#functie
def printName():
    print('mijn naam is Sige!')

def printName2(event):
    print('lololol')

#wat knoppen en tekst
'''
topFrame = Frame(root)
topFrame.pack()


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text="knop 1", fg="red")    #Button(waar?, wat?, kleur? van de tekst)
button2 = Button(topFrame, text="knop 2", fg="blue")
button3 = Button(topFrame, text="knop 3", fg="green")
button4 = Button(bottomFrame, text="knop 4", fg="purple")

widget1 = Label(root, text="one",bg="red",fg="blue") #bg = background color, fg = textkleur (foreground)
widget2 = Label(root, text="two",bg="green",fg="black")
widget3 = Label(root,text="three",bg="black",fg="white")
button1.pack(side=TOP) #om je button te maken, als je er niets in zet dan komt het onder elkaar
widget1.pack(side=TOP)
widget2.pack(side=BOTTOM,fill=X) #zorgt ervoor dat de 'widget' zo groot wordt als de grootte van je frame in de X richting = horizontaal
widget3.pack(side=TOP,fill=Y) #fill Y = evengroot als de grootte van je frame in de verticale richting
button2.pack(side=LEFT) #side=LEFT, plaats het zoveel mogelijk aan de linkerkant
button3.pack(side=BOTTOM)
button4.pack(side=LEFT)

'''
#naam + 'wachtwoord'
label_1 = Label(root,text='Name')
label_2 = Label(root,text='password')
entry_1 = Entry(root) #invul box
entry_2 = Entry(root)
label_1.grid(row=0, sticky=E) #voegt in principe niets toe, want row 0 = de standaard, sticky 'alligned' de tekst. E = east = rechts
label_2.grid(row=1, sticky=E) #dit zit dus onder de eerste rij
entry_1.grid(row=0, column=1) #je wilt het wachtwoord ernaast
entry_2.grid(row=1, column=1)

c = Checkbutton(root,text='keep me logged in')
c.grid(columnspan=2, row = 3) #columnspan 2 geeft aan dat het 2 kolommen gebruikt

#button die actie aanroept, in dit geval functie printName
button_naam = Button(root,text='print mijn naam', command=printName)
button_naam.grid(columnspan=2, row=2)

#button die actie aanroept MET conditie rechtermuisknop of linkermuisknop
button_naam2 = Button(root,text='rechtermuisknop')
button_naam2.bind("<Button-3>",printName2) #Button-x, met x = 1 is de linkermuisknop, x=2 is de middelste knop of scroll ding indrukken, x=3 is de rechtermuisknop
button_naam2.grid(columnspan=2, row=4)


root.mainloop() #zodat die hem altijd runt, anders blijft de window er maar 0.01 seconde ofso
