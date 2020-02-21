import numpy as np
from random import randint
import tkinter

class Hoplit:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = 0
    def __str__(self):
        return f"{self.x}, {self.y}"
    def action(self, choice, mx=0, my=0,stellung="vert"):
        if choice == "bewegung":
            self.move(x=mx, y=my)
    def move(self, x=0, y=0):
        self.x += x
        self.y += y

class Elite:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = 0
    def __str__(self):
        return f"{self.x}, {self.y}"
    def action(self, choice, mx=0, my=0,stellung="vert"):
        if choice == "bewegung":
            self.move(x=mx, y=my)
    def move(self, x=0, y=0):
        self.x += x
        self.y += y

class Bogen:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}, {self.y}"
    def action(self, choice, mx=0, my=0,stellung="vert"):
        if choice == "bewegung":
            self.move(x=mx, y=my)
    def move(self, x=0, y=0):
        self.x += x
        self.y += y

class Lanze:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}, {self.y}"
    def action(self, choice, mx=0, my=0,stellung="vert"):
        if choice == "bewegung":
            self.move(x=mx, y=my)
    def move(self, x=0, y=0):
        self.x += x
        self.y += y

class Feldherr:
    def __init__(self,Spieler):
        if Spieler == "Nord":
            self.x = 0
            self.y = 3
        if Spieler == "Sued":
            self.x = 6
            self.y = 3
    def __str__(self):
        return f"{self.x}, {self.y}"

def wuerfel(angr_bonus=0,vert_bonus=0):
    _att=randint(1,4)+angr_bonus
    _def=randint(1,4)+vert_bonus
    if _att>_def:
        return "sieg_angr"
    else:
        return "sieg_vert"
    
def format_row(row):
    return '|' + '|'.join('{0:^3s}'.format(x) for x in row) + '|'

def format_board(board):
    return '\n\n'.join(format_row(row) for row in board)

def buttonpress(x,y):
    global Einheit
    Einheit=str(x)
    global OldPosition
    OldPosition=[int(y[0]),int(y[1])]
    window.destroy()

def buttonpress2(x):
    global Position
    Position=[int(x[0]),int(x[1])]
    window.destroy()

def buttonpress3(x):
    global z
    z=x
    window.destroy()

try:
    window.destroy()
    print("\n\n- SPIELSTART! -")
except:
    print("\n\n- SPIELSTART! -")

_input=None
Hoplit1_N=Hoplit(0,1)
#_input=input("Spieler Nord:   Wo steht dein Bogenschütze (L/R) ?   ")
print()
if _input=="L":
    Bogen_N=Bogen(0,2)
    Lanze_N=Lanze(0,4)
else:
    Bogen_N=Bogen(0,4)
    Lanze_N=Lanze(0,2)
Hoplit2_N=Hoplit(0,5)
Hoplit3_N=Hoplit(1,1)
Hoplit4_N=Hoplit(1,2)
Hoplit5_N=Hoplit(1,4)
Hoplit6_N=Hoplit(1,5)
Hoplit1_S=Hoplit(5,1)
#_input=input("Spieler Süd:   Wo steht dein Bogenschütze (L/R) ?   ")
print()
if _input=="L":
    Bogen_S=Bogen(6,2)
    Lanze_S=Lanze(6,4)
else:
    Bogen_S=Bogen(6,4)
    Lanze_S=Lanze(6,2)
Hoplit2_S=Hoplit(5,2)
Hoplit3_S=Hoplit(5,4)
Hoplit4_S=Hoplit(5,5)
Hoplit5_S=Hoplit(6,1)
Hoplit6_S=Hoplit(6,5)
Einheiten_N=[Hoplit1_N,Hoplit2_N,Hoplit3_N,Hoplit4_N,Hoplit5_N,Hoplit6_N]
Einheiten_S=[Hoplit1_S,Hoplit2_S,Hoplit3_S,Hoplit4_S,Hoplit5_S,Hoplit6_S]
Elite_N=Elite(1,3)
Elite_S=Elite(5,3)
Feldherr_N=Feldherr("Nord")
Feldherr_S=Feldherr("Sued")
env = np.array([["   ","   ","   ","   ","   ","   ","   "],
                ["   ","   ","   ","   ","   ","   ","   "],
                ["   ","   ","   ","   ","   ","   ","   "],
                ["   ","   ","   ","   ","   ","   ","   "],
                ["   ","   ","   ","   ","   ","   ","   "],
                ["   ","   ","   ","   ","   ","   ","   "],
                ["   ","   ","   ","   ","   ","   ","   "]])
n=1
for i in Einheiten_N:
    env[i.x][i.y] = "N"+str(n)+" "
    n+=1
n=1
for i in Einheiten_S:
    env[i.x][i.y] = "S"+str(n)+" "
    n+=1
env[Feldherr_N.x][Feldherr_N.y] = "FH "
env[Feldherr_S.x][Feldherr_S.y] = "FH "
env[Bogen_N.x][Bogen_N.y] = "NB "
env[Bogen_S.x][Bogen_S.y] = "SB "
env[Lanze_N.x][Lanze_N.y] = "NL "
env[Lanze_S.x][Lanze_S.y] = "SL "
env[Elite_N.x][Elite_N.y] = "NE "
env[Elite_S.x][Elite_S.y] = "SE "
print("1       2\n3 4   5 6")
#Meuchel_N=input("Spieler Nord:   Welche Einheit ist dein Meuchelmörder (Nr. 1-6)?   ")
print()
print("1 2   3 4\n5       6")
#Meuchel_S=input("Spieler Süd:   Welche Einheit ist dein Meuchelmörder (Nr. 1-6)?   ")
print()
print("-----------------------------")
print()
print(format_board(env))
_AnzS=9
_AnzN=9
_dict={
    "N1 ":Hoplit1_N,
    "NB ":Bogen_N,
    "NL ":Lanze_N,
    "SB ":Bogen_S,
    "SL ":Lanze_S,
    "N2 ":Hoplit2_N,
    "N3 ":Hoplit3_N,
    "N4 ":Hoplit4_N,
    "N5 ":Hoplit5_N,
    "N6 ":Hoplit6_N,
    "S1 ":Hoplit1_S,
    "S2 ":Hoplit2_S,
    "S3 ":Hoplit3_S,
    "S4 ":Hoplit4_S,
    "S5 ":Hoplit5_S,
    "S6 ":Hoplit6_S,
    "NE ":Elite_N,
    "SE ":Elite_S,
    "N1A":Hoplit1_N,
    "N2A":Hoplit2_N,
    "N3A":Hoplit3_N,
    "N4A":Hoplit4_N,
    "N5A":Hoplit5_N,
    "N6A":Hoplit6_N,
    "S1A":Hoplit1_S,
    "S2A":Hoplit2_S,
    "S3A":Hoplit3_S,
    "S4A":Hoplit4_S,
    "S5A":Hoplit5_S,
    "S6A":Hoplit6_S,
    "NEA":Elite_N,
    "SEA":Elite_S}
_BerserkN=False
_BerserkS=False

_start=randint(1,2)
_end=False

if _start==1:
    print("\n\nSpieler Nord ist Startspieler!\n")
    _start="N"
else:
    print("\n\nSpieler Süd ist Startspieler!\n")
    _start="S"

backup2=None
backup=None

while _end==False:
    if _start=="S":
        print("Spieler Süd ist dran!\n")
    else:
        print("Spieler Nord ist dran!\n")
    z=0
    backup3=backup2
    backup2=backup
    backup=env
    print("Welche Einheit möchtest du aktivieren?\n")
    while True:
        window=tkinter.Tk()
        window.title("Phalanx")
        window.grid()
        for i in range(7):
            for j in range(7):
                button=tkinter.Button(window,text=env[i,j],command=lambda arg=env[i,j],
                                      arg2=str(i)+str(j): buttonpress(arg,arg2))
                button.grid(row=i,column=j)
                button.config(height = 5, width = 10)
        window.mainloop()
        if Einheit!="   ":
            if Einheit!="FH ":
                if _start in Einheit:
                    if _start=="S":
                        _start="N"
                    else:
                        _start="S"
                    break
        print("Keine oder falsche Einheit ausgewählt! Bitte wiederholen!\n")
    print("Was möchtest du mit",Einheit,"tun?\n")
    while True:
        window=tkinter.Tk()
        window.title("Phalanx")
        button1=tkinter.Button(window,text="Bewegung",command=lambda arg=1: buttonpress3(arg))
        button1.pack()
        button1.config(height = 5, width = 30)
        button2=tkinter.Button(window,text="Angriff",command=lambda arg=2: buttonpress3(arg))
        button2.pack()
        button2.config(height = 5, width = 30)
        button3=tkinter.Button(window,text="Bewegung & Angriff",command=lambda arg=3: buttonpress3(arg))
        button3.pack()
        button3.config(height = 5, width = 30)
        button4=tkinter.Button(window,text="Stellungsänderung",command=lambda arg=4: buttonpress3(arg))
        button4.pack()
        button4.config(height = 5, width = 30)
        button5=tkinter.Button(window,text="Bogenschütze",command=lambda arg=5: buttonpress3(arg))
        button5.pack()
        button5.config(height = 5, width = 30)
        button6=tkinter.Button(window,text="Meuchelmord",command=lambda arg=6: buttonpress3(arg))
        button6.pack()
        button6.config(height = 5, width = 30)
        button7=tkinter.Button(window,text="Zurück zur Auswahl!",command=lambda arg=7: buttonpress3(arg))
        button7.pack()
        button7.config(height = 5, width = 30)
        button8=tkinter.Button(window,text="QUIT GAME",command=lambda arg=8: buttonpress3(arg))
        button8.pack()
        button8.config(height = 5, width = 30)
        window.mainloop()
        if z==1:
            break
        if z==2:
            break
        if z==3:
            if "A" in Einheit:
                break
            print("Bewegung & Angriff mit",Einheit,"nicht möglich!\n")
        if z==4:
            if Einheit[1]=="E":
                break
            if Einheit[1] in ["1","2","3","4","5","6"]:
                break
            print("Stellungsänderung mit",Einheit,"nicht möglich!\n")
        if z==5:
            break
        if z==6:
            break
        if z==7:
            z=0
            break
        if z==8:
            z="END"
            break
    if z==0:
        if _start=="S":
            _start="N"
        else:
            _start="S"
        continue
    if z=="END":
        break
    if z==1:
        print("Wohin möchtest du die Einheit",Einheit,"bewegen?\n")
        while True:
            window=tkinter.Tk()
            window.title("Phalanx")
            window.grid()
            for i in range(7):
                for j in range(7):
                    button=tkinter.Button(window,text=env[i,j],command=lambda arg=str(i)+str(j): buttonpress2(arg))
                    button.grid(row=i,column=j)
                    button.config(height = 5, width = 10)
            window.mainloop()
            treffer=0
            for i in _dict:
                if i==Einheit:
                    continue
                tmp=str(_dict[i])
                temp=[int(tmp[0]),int(tmp[3])]
                if temp==Position:
                    treffer=1
            a=abs(-OldPosition[0]+Position[0])
            b=abs(-OldPosition[1]+Position[1])
            if a<3 and b<3 and treffer==0:
                break
            print("Bewegung nicht zulässig! Neues Zielfeld wählen!\n")
        env[OldPosition[0]][OldPosition[1]] = "   "
        _dict[Einheit].action("bewegung",-OldPosition[0]+Position[0],-OldPosition[1]+Position[1])
        env[Position[0]][Position[1]] = Einheit
        window=tkinter.Tk()
        window.title("In welche Stellung begibt sich die Einheit "+Einheit+"?")
        button1=tkinter.Button(window,text="Verteidigung",command=lambda arg=1: buttonpress3(arg))
        button1.pack()
        button1.config(height = 5, width = 120)
        button2=tkinter.Button(window,text="Angriff",command=lambda arg=2: buttonpress3(arg))
        button2.pack()
        button2.config(height = 5, width = 120)
        window.mainloop()
        if z==1:
            if "A" in Einheit:
                env[Position[0]][Position[1]]=Einheit[0:2]+" "
        if z==2:
            if " " in Einheit:
                env[Position[0]][Position[1]]=Einheit[0:2]+"A"
        continue
    if z==2:
        print("Welche Einheit möchtest du mit",Einheit,"angreifen?\n")
        while True:
            window=tkinter.Tk()
            window.title("Phalanx")
            window.grid()
            for i in range(7):
                for j in range(7):
                    button=tkinter.Button(window,text=env[i,j],command=lambda arg=str(i)+str(j): buttonpress2(arg))
                    button.grid(row=i,column=j)
                    button.config(height = 5, width = 10)
            window.mainloop()
            a=abs(-OldPosition[0]+Position[0])
            b=abs(-OldPosition[1]+Position[1])
            if Position!=OldPosition and env[Position[0]][Position[1]]!="   ":
                if a<2 and b<2:
                    break
            print("Angriff nicht zulässig! Neues Zielfeld wählen!\n")
        if wuerfel()=="sieg_angr":
            print("Sieg! Einheit besiegt!\n")
            env[Position[0]][Position[1]] = "   "
            
        else:
            print("Kein Sieg. Nichts passiert.\n")
    if z==3:
        print("Wohin möchtest du die Einheit",Einheit,"bewegen?\n")
        while True:
            window=tkinter.Tk()
            window.title("Phalanx")
            window.grid()
            for i in range(7):
                for j in range(7):
                    button=tkinter.Button(window,text=env[i,j],command=lambda arg=str(i)+str(j): buttonpress2(arg))
                    button.grid(row=i,column=j)
                    button.config(height = 5, width = 10)
            window.mainloop()
            treffer=0
            for i in _dict:
                if i==Einheit:
                    continue
                tmp=str(_dict[i])
                temp=[int(tmp[0]),int(tmp[3])]
                if temp==Position:
                    treffer=1
            a=abs(-OldPosition[0]+Position[0])
            b=abs(-OldPosition[1]+Position[1])
            if a<3 and b<3 and treffer==0:
                break
            print("Bewegung nicht zulässig! Neues Zielfeld wählen!\n")
        env[OldPosition[0]][OldPosition[1]] = "   "
        _dict[Einheit].action("bewegung",-OldPosition[0]+Position[0],-OldPosition[1]+Position[1])
        env[Position[0]][Position[1]] = Einheit
        print("Welche Einheit möchtest du mit",Einheit,"angreifen?\n")
        OldPosition=Position
        while True:
            window=tkinter.Tk()
            window.title("Phalanx")
            window.grid()
            for i in range(7):
                for j in range(7):
                    button=tkinter.Button(window,text=env[i,j],command=lambda arg=str(i)+str(j): buttonpress2(arg))
                    button.grid(row=i,column=j)
                    button.config(height = 5, width = 10)
            window.mainloop()
            a=abs(-OldPosition[0]+Position[0])
            b=abs(-OldPosition[1]+Position[1])
            if Position!=OldPosition and env[Position[0]][Position[1]]!="   ":
                if a<2 and b<2:
                    break
            print("Angriff nicht zulässig! Neues Zielfeld wählen!\n")
        if wuerfel()=="sieg_angr":
            print("Sieg! Einheit besiegt!\n")
            env[Position[0]][Position[1]] = "   "
            
        else:
            print("Kein Sieg. Nichts passiert.\n")
    if z==4:
        window=tkinter.Tk()
        window.title("In welche Stellung begibt sich die Einheit "+Einheit+"?")
        button1=tkinter.Button(window,text="Verteidigung",command=lambda arg=1: buttonpress3(arg))
        button1.pack()
        button1.config(height = 5, width = 120)
        button2=tkinter.Button(window,text="Angriff",command=lambda arg=2: buttonpress3(arg))
        button2.pack()
        button2.config(height = 5, width = 120)
        window.mainloop()
        if z==1:
            if "A" in Einheit:
                env[OldPosition[0]][OldPosition[1]]=Einheit[0:2]+" "
        if z==2:
            if " " in Einheit:
                env[OldPosition[0]][OldPosition[1]]=Einheit[0:2]+"A"
    if z==5:
        continue
    if z==6:
        continue

try:
    window.destroy()
    print("Tschüss!")
except:
    print("Tschüss!")