import numpy as np
from random import randint
import tkinter
import time

class Hoplit:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Elite:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Bogen:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Lanze:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
class Feldherr:
    def __init__(self,Spieler):
        if Spieler == "Nord":
            self.x = 0
            self.y = 3
        if Spieler == "Sued":
            self.x = 6
            self.y = 3

def wuerfel(angr_bonus=0,vert_bonus=0):
    wa=randint(1,4)
    wv=randint(1,4)
    _att=wa+angr_bonus
    _def=wv+vert_bonus
    print("- Angreifer:",env[OldPosition[0]][OldPosition[1]])
    print("- Verteidiger:",env[Position[0]][Position[1]])
    print("-- Würfelwurf Angreifer:",wa,"+",angr_bonus,"=",_att)
    print("-- Würfelwurf Verteidiger:",wv,"+",vert_bonus,"=",_def)
    if _att>_def:
        return "sieg_angr"
    else:
        return "sieg_vert"

def calc_bon(meuchel=0):
    a=0
    b=0
    if _nn-_ns>2:
        if _start2=="S":
            a+=1
            print("Berserker!")
    if _ns-_nn>2:
        if _start2=="N":
            a+=1
            print("Berserker!")
    if env[Position[0]][Position[1]][0]=="F":
        #print("Rüstungsbonus Feldherr: 1")
        b+=1
    if env[Position[0]][Position[1]][1] in ["1","2","3","4","5","6"]:
        if env[Position[0]][Position[1]][2]==" ":
            #print("Verteidigungsstellung!")
            b+=1
    if env[OldPosition[0]][OldPosition[1]][1]=="E":
        if env[OldPosition[0]][OldPosition[1]][2]=="A":
            #print("Elite-Angriffsstellung!")
            a+=2
    if env[OldPosition[0]][OldPosition[1]][1] in ["1","2","3","4","5","6"]:
        if env[OldPosition[0]][OldPosition[1]][2]=="A":
            #print("Angriffsstellung!")
            a+=1
    if env[Position[0]][Position[1]][1]=="E":
        if env[Position[0]][Position[1]][2]==" ":
            #print("Elite-Verteidigungsstellung!")
            b+=2
    if Einheit[1]=="L":
        #print("Reitangriffsbonus Lanzenträger: 1")
        a+=1
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i==0 and j==0:
                continue
            if Position[0]+i>-1 and Position[0]+i<7:
                if Position[1]+j>-1 and Position[1]+j<7:
                    if env[Position[0]+i][Position[1]+j][0]==_start2:
                        if Position[0]+i!=OldPosition[0] or Position[1]+j!=OldPosition[1]:
                            if env[Position[0]+i][Position[1]+j][1] in ["1","2","3","4","5","6","E"]:
                                if env[Position[0]+i][Position[1]+j][2]=="A":
                                    if env[Position[0]+i][Position[1]+j][1]=="E":
                                        #print("Angriffsunterstützung Elite!")
                                        a+=2
                                    else:
                                        #print("Angriffsunterstützung Hoplit!")
                                        a+=1
            if OldPosition[0]+i>-1 and OldPosition[0]+i<7:
                if OldPosition[1]+j>-1 and OldPosition[1]+j<7:
                    if env[OldPosition[0]+i][OldPosition[1]+j][0]==_start:
                        if OldPosition[0]+i!=Position[0] or OldPosition[1]+j!=Position[1]:
                            if env[OldPosition[0]+i][OldPosition[1]+j][1] in ["1","2","3","4","5","6","E"]:
                                if env[OldPosition[0]+i][OldPosition[1]+j][2]==" ":
                                    if env[OldPosition[0]+i][OldPosition[1]+j][1]=="E":
                                        #print("Verteidigungsunterstützung Elite!")
                                        b+=2
                                    else:
                                        #print("Verteidigungsunterstützung Hoplit!")
                                        b+=1
    if _Fernkampf==True:
        print("Fernkampf!")
        if _BogenschN==1 and _start2=="N":
            if env[Position[0]][Position[1]][1] not in ["B","L"]:
                if env[Position[0]][Position[1]][2]==" ":
                    a+=0
                else:
                    #print("Scharfschützenbonus: 2")
                    a+=2
            else:
                #print("Scharfschützenbonus: 2")
                a+=2
        if _BogenschS==1 and _start2=="S":
            if env[Position[0]][Position[1]][1] not in ["B","L"]:
                if env[Position[0]][Position[1]][2]==" ":
                    #print("Kein Bonus!")
                    a+=0
                else:
                    #print("Scharfschützenbonus: 2")
                    a+=2
            else:
                #print("Scharfschützenbonus: 2")
                a+=2
        #else:
            #if env[Position[0]][Position[1]][1] not in ["B","L"]:
                #if env[Position[0]][Position[1]][2]==" ":
                    #print("Ziel immun gegen Fernkampf!")
                    #b+=999
    if meuchel==1:
        print("Hinterhalt!")
        a=+4
    return [a,b]
    
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

def retrieve_input():
    global meuchel
    meuchel=textBox.get("1.0","end-1c")
    window.destroy()

print("\n\n- SPIELSTART! -\n\n")

_input=randint(0,1)
Hoplit1_N=Hoplit(0,1)
if _input==0:
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
_input=randint(0,1)
if _input==0:
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
env[Feldherr_N.x][Feldherr_N.y] = "FHN"
env[Feldherr_S.x][Feldherr_S.y] = "FHS"
env[Bogen_N.x][Bogen_N.y] = "NB "
env[Bogen_S.x][Bogen_S.y] = "SB "
env[Lanze_N.x][Lanze_N.y] = "NL "
env[Lanze_S.x][Lanze_S.y] = "SL "
env[Elite_N.x][Elite_N.y] = "NE "
env[Elite_S.x][Elite_S.y] = "SE "
print(format_board(env))
Meuchel_N=1
Meuchel_S=1
window=tkinter.Tk()
window.title("Phalanx")
tkinter.Label(window,text="Spieler Nord (GEHEIM!): Welche Einheit ist dein Meuchelmörder (Nr. 1-6)?").pack()
textBox=tkinter.Text(window,height=1,width=1)
textBox.pack()
button=tkinter.Button(window,text="OK",command=lambda: retrieve_input())
button.pack()
tkinter.mainloop()
Meuchel_N=int(meuchel[0])
window=tkinter.Tk()
window.title("Phalanx")
tkinter.Label(window,text="Spieler Süd (GEHEIM!): Welche Einheit ist dein Meuchelmörder (Nr. 1-6)?").pack()
textBox=tkinter.Text(window,height=1,width=1)
textBox.pack()
button=tkinter.Button(window,text="OK",command=lambda: retrieve_input())
button.pack()
tkinter.mainloop()
Meuchel_S=int(meuchel[0])
#_dict={
#    "N1 ":"Hoplit1_N",
#    "NB ":"Bogen_N",
#    "NL ":"Lanze_N",
#    "SB ":"Bogen_S",
#    "SL ":"Lanze_S",
#    "N2 ":"Hoplit2_N",
#    "N3 ":"Hoplit3_N",
#    "N4 ":"Hoplit4_N",
#    "N5 ":"Hoplit5_N",
#    "N6 ":"Hoplit6_N",
#    "S1 ":"Hoplit1_S",
#    "S2 ":"Hoplit2_S",
#    "S3 ":"Hoplit3_S",
#    "S4 ":"Hoplit4_S",
#    "S5 ":"Hoplit5_S",
#    "S6 ":"Hoplit6_S",
#    "NE ":"Elite_N",
#    "SE ":"Elite_S",
#    "N1A":"Hoplit1_N",
#    "N2A":"Hoplit2_N",
#    "N3A":"Hoplit3_N",
#    "N4A":"Hoplit4_N",
#    "N5A":"Hoplit5_N",
#    "N6A":"Hoplit6_N",
#    "S1A":"Hoplit1_S",
#    "S2A":"Hoplit2_S",
#    "S3A":"Hoplit3_S",
#    "S4A":"Hoplit4_S",
#    "S5A":"Hoplit5_S",
#    "S6A":"Hoplit6_S",
#    "NEA":"Elite_N",
#    "SEA":"Elite_S"}
_BogenschN=0
_BogenschS=0
_PunkteN=0
_PunkteS=0
_start=randint(1,2)
if _start==1:
    print("\n\nSpieler Nord ist Startspieler!\n")
    _start="N"
else:
    print("\n\nSpieler Süd ist Startspieler!\n")
    _start="S"
_end=False
_contrN=0
_contrS=0
_correx=0
_achtung="\nVor der Eingabe des Bewegungsziels findet eine Verifizierung der aktivierten Einheit mit der Wahl deines Meuchelmörders statt.\n\nWenn bei erfolgreicher Verifizierung nach deiner Bewegung kein Angriff möglich ist, musst du deinen Zug beenden und dein Gegner kennt den Standort deines Meuchelmörders!\n\n"

#MAINLOOP

while _end==False:
    _nn=0
    _ns=0
    for i in range(7):
        for j in range(7):
            if env[i,j][0]=="N":
                _nn+=1
            if env[i,j][0]=="S":
                _ns+=1
    _ff=0
    _Fernkampf=False
    if _start=="S":
        print("Spieler Süd ist dran!\n")
    else:
        print("Spieler Nord ist dran!\n")
    z=0
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
            if Einheit[0:2]=="FH" and Einheit[2]==_start:
                if _ff==0:
                    print("Willst du wirklich aufgeben?\n")
                _ff+=1
            if Einheit[0:2]!="FH":
                if _start in Einheit:
                    if _correx!=1:
                        if _BogenschN==1:
                            _contrN+=1
                        if _BogenschS==1:
                            _contrS+=1
                    _correx=0
                    if _contrN==3:
                        _contrN=0
                        _BogenschN=0
                        for i in range(7):
                            for j in range(7):
                                if env[i,j]=="NBZ":
                                    env[i,j]="NB "
                        if Einheit=="NBZ":
                            Einheit="NB "                                      
                    if _contrS==3:
                        _contrS=0
                        _BogenschS=0
                        for i in range(7):
                            for j in range(7):
                                if env[i,j]=="SBZ":
                                    env[i,j]="SB "
                        if Einheit=="SBZ":
                            Einheit="SB "  
                    if _start=="S":
                        _start="N"
                        _start2="S"
                    else:
                        _start="S"
                        _start2="N"
                    break
        if _ff==1:
            continue
        if _ff==2:
            print("- SPIELER",_start,"VERLIERT! -\n")
            break
        print("Keine oder falsche Einheit ausgewählt! Bitte wiederholen!\n")
    if _ff==2:
        break
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
        button6=tkinter.Button(window,text="Meuchelmord A",command=lambda arg=6: buttonpress3(arg))
        button6.pack()
        button6.config(height = 5, width = 30)
        button7=tkinter.Button(window,text="Meuchelmord B&A",command=lambda arg=7: buttonpress3(arg))
        button7.pack()
        button7.config(height = 5, width = 30)
        button8=tkinter.Button(window,text="Zurück zur Auswahl!",command=lambda arg=8: buttonpress3(arg))
        button8.pack()
        button8.config(height = 5, width = 30)
        button9=tkinter.Button(window,text="QUIT GAME",command=lambda arg=9: buttonpress3(arg))
        button9.pack()
        button9.config(height = 5, width = 30)
        window.mainloop()
        if z==1:
            break
        if z==2:
            if "B" in Einheit:
                treffer=0
                for i in [-3,-2,-1,0,1,2,3]:
                    for j in [-3,-2,-1,0,1,2,3]:
                        if i==0 and j==0:
                            continue
                        if abs(i)==3 and abs(j)==3:
                            continue
                        if (OldPosition[0]+i>6) or (OldPosition[1]+j>6):
                            continue
                        if (OldPosition[0]+i<0) or (OldPosition[1]+j<0):
                            continue
                        if env[OldPosition[0]+i][OldPosition[1]+j]=="   ":
                            continue
                        if env[OldPosition[0]+i][OldPosition[1]+j][0:3]!="FH"+_start2:
                            if _start2!=env[OldPosition[0]+i][OldPosition[1]+j][0]:
                                if Einheit[2]!="Z":
                                    if env[OldPosition[0]+i][OldPosition[1]+j][1:3] in ["1 ","2 ","3 ","4 ","5 ","6 ","E "]:
                                        if abs(i)>1 or abs(j)>1:
                                            continue    
                                treffer=1
                if treffer==1:
                    break
            else:
                treffer=0
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if i==0 and j==0:
                            continue
                        if (OldPosition[0]+i>6) or (OldPosition[1]+j>6):
                            continue
                        if (OldPosition[0]+i<0) or (OldPosition[1]+j<0):
                            continue
                        if env[OldPosition[0]+i][OldPosition[1]+j]!="FH"+_start2:
                            if _start==env[OldPosition[0]+i][OldPosition[1]+j][0]:                           
                                treffer=1
                if treffer==1:
                    break
            print("Angreifen nicht möglich mit",Einheit,"!\n")
        if z==3:
            if "A" in Einheit:
                break
            if "L" in Einheit:
                break
            if "B" in Einheit:
                treffer=0
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if i==0 and j==0:
                            continue
                        if (OldPosition[0]+i>6) or (OldPosition[1]+j>6):
                            continue
                        if (OldPosition[0]+i<0) or (OldPosition[1]+j<0):
                            continue
                        if env[OldPosition[0]+i][OldPosition[1]+j]=="   ":            
                            treffer=1
                if treffer==1:    
                    break
            print("Bewegung & Angriff mit",Einheit,"nicht möglich!\n")
        if z==4:
            if Einheit[1]=="E":
                break
            if Einheit[1] in ["1","2","3","4","5","6"]:
                break
            print("Stellungsänderung mit",Einheit,"nicht möglich!\n")
        if z==5:
            if Einheit[1]=="B":
                break
            print("Kein Bogenschütze ausgewählt!\n")
        if z==6:
            if _start2=="N":
                if str(Meuchel_N)==env[OldPosition[0]][OldPosition[1]][1]:
                    treffer=0
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            if i==0 and j==0:
                                continue
                            if (OldPosition[0]+i>6) or (OldPosition[1]+j>6):
                                continue
                            if (OldPosition[0]+i<0) or (OldPosition[1]+j<0):
                                continue
                            if env[OldPosition[0]+i][OldPosition[1]+j]!="FH"+_start2:
                                if _start==env[OldPosition[0]+i][OldPosition[1]+j][0]:                           
                                    treffer=1
                    if treffer==1:
                        break
                print("Hinterhalt bei Spieler",_start2,"und Einheit",Einheit,"nicht möglich!\n")
            if _start2=="S":
                if str(Meuchel_S)==env[OldPosition[0]][OldPosition[1]][1]:
                    treffer=0
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            if i==0 and j==0:
                                continue
                            if (OldPosition[0]+i>6) or (OldPosition[1]+j>6):
                                continue
                            if (OldPosition[0]+i<0) or (OldPosition[1]+j<0):
                                continue
                            if env[OldPosition[0]+i][OldPosition[1]+j]!="FH"+_start2:
                                if _start==env[OldPosition[0]+i][OldPosition[1]+j][0]:                           
                                    treffer=1
                    if treffer==1:
                        break
                print("Hinterhalt bei Spieler",_start2,"und Einheit",Einheit,"nicht möglich!\n")
        if z==7:
            window=tkinter.Tk()
            window.title("ACHTUNG!")
            tkinter.Label(window,text=_achtung).pack()
            button1=tkinter.Button(window,text="OK",command=lambda arg=1: buttonpress3(arg))
            button1.pack()
            button1.config(height = 4, width = 20)
            button2=tkinter.Button(window,text="Zurück",command=lambda arg=2: buttonpress3(arg))
            button2.pack()
            button2.config(height = 4, width = 20)
            window.mainloop()
            if z==2:
                print("Zug abgebrochen! Standort Meuchelmörder nicht verifiziert!\n")
                continue
            if z==1:
                if _start2=="N":
                    if str(Meuchel_N)==env[OldPosition[0]][OldPosition[1]][1]:
                        if "A" in Einheit:
                            z=7
                            break
                    print("Hinterhalt bei Spieler",_start2,"und Einheit",Einheit,"nicht möglich!\n")
                if _start2=="S":
                    if str(Meuchel_S)==env[OldPosition[0]][OldPosition[1]][1]:
                        if "A" in Einheit:
                            z=7
                            break
                    print("Hinterhalt bei Spieler",_start2,"und Einheit",Einheit,"nicht möglich!\n")
        if z==8:
            z=0
            break
        if z==9:
            z="END"
            break
    if z==0:
        _correx=1
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
            if Position==[0,3] or Position==[6,3]:
                treffer=1
            if env[Position[0],Position[1]]!="   ":
                treffer=1
            a=abs(-OldPosition[0]+Position[0])
            b=abs(-OldPosition[1]+Position[1])
            _choice=[[-1,0],[1,0],[0,-1],[0,1]]
            _weg=0
            start=OldPosition
            for i in _choice:
                if _weg==1:
                    break
                if start[0]+i[0]<0 or start[0]+i[0]>6:
                    continue
                if start[1]+i[1]<0 or start[1]+i[1]>6:
                    continue
                if env[start[0]+i[0],start[1]+i[1]][0]==_start:
                    continue
                if env[start[0]+i[0],start[1]+i[1]]=="FH"+_start:
                    continue
                start1=[start[0]+i[0],start[1]+i[1]]
                if start1==Position:
                    _weg=1
                    break
                for i in _choice:
                    if _weg==1:
                        break
                    if start1[0]+i[0]<0 or start1[0]+i[0]>6:
                        continue
                    if start1[1]+i[1]<0 or start1[1]+i[1]>6:
                        continue
                    if env[start1[0]+i[0],start1[1]+i[1]][0]==_start:
                        continue
                    if env[start1[0]+i[0],start1[1]+i[1]]=="FH"+_start:
                        continue
                    if [start1[0]+i[0],start1[1]+i[1]]==start:
                        continue
                    start2=[start1[0]+i[0],start1[1]+i[1]]
                    if start2==Position:
                        _weg=1
                        break
                    for i in _choice:
                        if _weg==1:
                            break
                        if start2[0]+i[0]<0 or start2[0]+i[0]>6:
                            continue
                        if start2[1]+i[1]<0 or start2[1]+i[1]>6:
                            continue
                        if [start2[0]+i[0],start2[1]+i[1]]==start:
                            continue
                        if env[start2[0]+i[0],start2[1]+i[1]][0]==_start:
                            continue
                        if env[start2[0]+i[0],start2[1]+i[1]]=="FH"+_start:
                            continue
                        if [start2[0]+i[0],start2[1]+i[1]]==start1:
                            continue
                        start3=[start2[0]+i[0],start2[1]+i[1]]
                        if start3==Position:
                            _weg=1
                            break
                        for i in _choice:
                            if _weg==1:
                                break
                            if start3[0]+i[0]<0 or start3[0]+i[0]>6:
                                continue
                            if start3[1]+i[1]<0 or start3[1]+i[1]>6:
                                continue
                            if [start3[0]+i[0],start3[1]+i[1]]==start:
                                continue
                            if env[start3[0]+i[0],start3[1]+i[1]][0]==_start:
                                continue
                            if env[start3[0]+i[0],start3[1]+i[1]]=="FH"+_start:
                                continue
                            if [start3[0]+i[0],start3[1]+i[1]]==start2:
                                continue
                            start4=[start3[0]+i[0],start3[1]+i[1]]
                            if start4==Position:
                                _weg=1
                                break
                            if Einheit[1]=="L":
                                for i in _choice:
                                    if _weg==1:
                                        break
                                    if start4[0]+i[0]<0 or start4[0]+i[0]>6:
                                        continue
                                    if start4[1]+i[1]<0 or start4[1]+i[1]>6:
                                        continue
                                    if [start4[0]+i[0],start4[1]+i[1]]==start:
                                        continue
                                    if env[start4[0]+i[0],start4[1]+i[1]][0]==_start:
                                        continue
                                    if env[start4[0]+i[0],start4[1]+i[1]]=="FH"+_start:
                                        continue
                                    if [start4[0]+i[0],start4[1]+i[1]]==start3:
                                        continue
                                    start5=[start4[0]+i[0],start4[1]+i[1]]
                                    if start5==Position:
                                        _weg=1
                                        break
            if Einheit[1]=="L":
                if a<4 and b<4 and a+b<6 and treffer==0 and _weg==1:
                    break
            else:
                if a<3 and b<3 and treffer==0 and _weg==1:
                    break
            print("Bewegung nicht zulässig! Neues Zielfeld wählen!\n")
        env[OldPosition[0]][OldPosition[1]] = "   "
        env[Position[0]][Position[1]] = Einheit
        if Einheit[1] not in ["L","B"]:
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
            if a>1 or b>1:
                if "B" in Einheit:
                    if a<4 and b<4 and a+b<6:
                        if env[Position[0]][Position[1]]!="   ":
                            if _start==env[Position[0]][Position[1]][0]:
                                if env[Position[0]][Position[1]][1:3] in ["1A","2A","3A","4A","5A","6A","EA","B ","L "]:
                                    _Fernkampf=True
                                    break
                            if _start==env[Position[0]][Position[1]][2]:
                                _Fernkampf=True
                                break
            else:
                if Position!=OldPosition and env[Position[0]][Position[1]]!="   ":
                    if a<2 and b<2:
                        if _start==env[Position[0]][Position[1]][0]:
                            break
                        if _start==env[Position[0]][Position[1]][2]:
                            break
            print("Angriff nicht zulässig! Neues Zielfeld wählen!\n")
        if Einheit[1] not in ["L","B"]:
            if "A" not in Einheit:
                window=tkinter.Tk()
                window.title("Begibt sich die Einheit "+Einheit+"in Angriffsstellung?")
                button1=tkinter.Button(window,text="Ja",command=lambda arg=1: buttonpress3(arg))
                button1.pack()
                button1.config(height = 5, width = 120)
                button2=tkinter.Button(window,text="Nein",command=lambda arg=2: buttonpress3(arg))
                button2.pack()
                button2.config(height = 5, width = 120)
                window.mainloop()
                if z==1:
                    env[OldPosition[0]][OldPosition[1]]=Einheit[0:2]+"A"
                    Einheit=Einheit[0:2]+"A"
        temp=calc_bon()
        if wuerfel(temp[0],temp[1])=="sieg_angr":
            if env[Position[0]][Position[1]][0]=="F":
                print("Sieg! Feldherr verletzt!\n")
                if _start2=="S":
                    _PunkteS+=1
                if _start2=="N":
                    _PunkteN+=1
                if _PunkteN==2 or _PunkteS==2:
                    print("- SPIELER",_start2,"GEWINNT! -\n")
                    time.sleep(5)
                    _end=True
            else:
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
            if Position==[0,3] or Position==[6,3]:
                treffer=1
            if env[Position[0],Position[1]]!="   ":
                treffer=1
            a=abs(-OldPosition[0]+Position[0])
            b=abs(-OldPosition[1]+Position[1])
            _choice=[[-1,0],[1,0],[0,-1],[0,1]]
            _weg=0
            start=OldPosition
            for i in _choice:
                if _weg==1:
                    break
                if start[0]+i[0]<0 or start[0]+i[0]>6:
                    continue
                if start[1]+i[1]<0 or start[1]+i[1]>6:
                    continue
                if env[start[0]+i[0],start[1]+i[1]][0]==_start:
                    continue
                if env[start[0]+i[0],start[1]+i[1]]=="FH"+_start:
                    continue
                start1=[start[0]+i[0],start[1]+i[1]]
                if start1==Position:
                    _weg=1
                    break
                for i in _choice:
                    if _weg==1:
                        break
                    if start1[0]+i[0]<0 or start1[0]+i[0]>6:
                        continue
                    if start1[1]+i[1]<0 or start1[1]+i[1]>6:
                        continue
                    if env[start1[0]+i[0],start1[1]+i[1]][0]==_start:
                        continue
                    if env[start1[0]+i[0],start1[1]+i[1]]=="FH"+_start:
                        continue
                    if [start1[0]+i[0],start1[1]+i[1]]==start:
                        continue
                    start2=[start1[0]+i[0],start1[1]+i[1]]
                    if start2==Position:
                        _weg=1
                        break
                    if Einheit[1]!="B":
                        for i in _choice:
                            if _weg==1:
                                break
                            if start2[0]+i[0]<0 or start2[0]+i[0]>6:
                                continue
                            if start2[1]+i[1]<0 or start2[1]+i[1]>6:
                                continue
                            if [start2[0]+i[0],start2[1]+i[1]]==start:
                                continue
                            if env[start2[0]+i[0],start2[1]+i[1]][0]==_start:
                                continue
                            if env[start2[0]+i[0],start2[1]+i[1]]=="FH"+_start:
                                continue
                            if [start2[0]+i[0],start2[1]+i[1]]==start1:
                                continue
                            start3=[start2[0]+i[0],start2[1]+i[1]]
                            if start3==Position:
                                _weg=1
                                break
                            for i in _choice:
                                if _weg==1:
                                    break
                                if start3[0]+i[0]<0 or start3[0]+i[0]>6:
                                    continue
                                if start3[1]+i[1]<0 or start3[1]+i[1]>6:
                                    continue
                                if [start3[0]+i[0],start3[1]+i[1]]==start:
                                    continue
                                if env[start3[0]+i[0],start3[1]+i[1]][0]==_start:
                                    continue
                                if env[start3[0]+i[0],start3[1]+i[1]]=="FH"+_start:
                                    continue
                                if [start3[0]+i[0],start3[1]+i[1]]==start2:
                                    continue
                                start4=[start3[0]+i[0],start3[1]+i[1]]
                                if start4==Position:
                                    _weg=1
                                    break
                                if Einheit[1]=="L":
                                    for i in _choice:
                                        if _weg==1:
                                            break
                                        if start4[0]+i[0]<0 or start4[0]+i[0]>6:
                                            continue
                                        if start4[1]+i[1]<0 or start4[1]+i[1]>6:
                                            continue
                                        if [start4[0]+i[0],start4[1]+i[1]]==start:
                                            continue
                                        if env[start4[0]+i[0],start4[1]+i[1]][0]==_start:
                                            continue
                                        if env[start4[0]+i[0],start4[1]+i[1]]=="FH"+_start:
                                            continue
                                        if [start4[0]+i[0],start4[1]+i[1]]==start3:
                                            continue
                                        start5=[start4[0]+i[0],start4[1]+i[1]]
                                        if start5==Position:
                                            _weg=1
                                            break
            if Einheit[1]=="L":
                if a<4 and b<4 and a+b<6 and treffer==0 and _weg==1:
                    break
            if Einheit[1]=="B":
                if a<2 and b<2 and treffer==0 and _weg==1:
                    break
            else:
                if a<3 and b<3 and treffer==0 and _weg==1:
                    break
            print("Bewegung nicht zulässig! Neues Zielfeld wählen!\n")
        env[OldPosition[0]][OldPosition[1]] = "   "
        env[Position[0]][Position[1]] = Einheit
        print("Welche Einheit möchtest du mit",Einheit,"angreifen?\n")
        OldPosition=Position
        while True:
            _abbr="NEIN"
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
            if a>1 or b>1:
                if "B" in Einheit:
                    if a<4 and b<4 and a+b<6:
                        if env[Position[0]][Position[1]]!="   ":
                            if _start==env[Position[0]][Position[1]][0]:
                                if env[Position[0]][Position[1]][1:3] in ["1A","2A","3A","4A","5A","6A","EA","B ","L "]:
                                    _Fernkampf=True
                                    break
                            if _start==env[Position[0]][Position[1]][2]:
                                _Fernkampf=True
                                break
            else:
                if Position!=OldPosition and env[Position[0]][Position[1]]!="   ":
                    if a<2 and b<2:
                        if _start==env[Position[0]][Position[1]][0]:
                            break
                        if _start==env[Position[0]][Position[1]][2]:
                            break
            print("Angriff nicht zulässig! Neues Zielfeld wählen!\n")
            window=tkinter.Tk()
            window.title("Angriff abbrechen?")
            button1=tkinter.Button(window,text="Nein",command=lambda arg=1: buttonpress3(arg))
            button1.pack()
            button1.config(height = 5, width = 60)
            button2=tkinter.Button(window,text="Ja",command=lambda arg=2: buttonpress3(arg))
            button2.pack()
            button2.config(height = 5, width = 60)
            window.mainloop()
            if z==2:
                _abbr="JA"
                break
        if _abbr=="JA":
            _abbr="NEIN"
            continue
        temp=calc_bon()
        if wuerfel(temp[0],temp[1])=="sieg_angr":
            if env[Position[0]][Position[1]][0]=="F":
                print("Sieg! Feldherr verletzt!\n")
                if _start2=="S":
                    _PunkteS+=1
                if _start2=="N":
                    _PunkteN+=1
                if _PunkteN==2 or _PunkteS==2:
                    print("- SPIELER",_start2,"GEWINNT! -\n")
                    time.sleep(5)
                    _end=True
            else:
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
        if _start2=="N":
            print("Bogenschütze Nord zielend!\n")
            _BogenschN=1
            _contrN=0
            for i in range(7):
                for j in range(7):
                    if env[i,j]=="NB ":
                        env[i,j]="NBZ"
        if _start2=="S":
            print("Bogenschütze Süd zielend!\n")
            _BogenschS=1
            _contrS=0
            for i in range(7):
                for j in range(7):
                    if env[i,j]=="SB ":
                        env[i,j]="SBZ"
        continue
    if z==6:
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
                    if _start==env[Position[0]][Position[1]][0]:
                        break
                    if _start==env[Position[0]][Position[1]][2]:
                        break
            print("Angriff nicht zulässig! Neues Zielfeld wählen!\n")
        if _start2=="N":
            Meuchel_N=0
        if _start2=="S":
            Meuchel_S=0
        if Einheit[1] not in ["L","B"]:
            if "A" not in Einheit:
                window=tkinter.Tk()
                window.title("Begibt sich die Einheit "+Einheit+"in Angriffsstellung?")
                button1=tkinter.Button(window,text="Ja",command=lambda arg=1: buttonpress3(arg))
                button1.pack()
                button1.config(height = 5, width = 120)
                window.mainloop()
                if z==1:
                    env[OldPosition[0]][OldPosition[1]]=Einheit[0:2]+"A"
        temp=calc_bon(meuchel=1)
        if wuerfel(temp[0],temp[1])=="sieg_angr":
            if env[Position[0]][Position[1]][0]=="F":
                print("Sieg! Feldherr verletzt!\n")
                if _start2=="S":
                    _PunkteS+=1
                if _start2=="N":
                    _PunkteN+=1
                if _PunkteN==2 or _PunkteS==2:
                    print("- SPIELER",_start2,"GEWINNT! -\n")
                    time.sleep(5)
                    _end=True
            else:
                print("Sieg! Einheit besiegt!\n")
                env[Position[0]][Position[1]] = "   "       
        else:
            print("Kein Sieg. Nichts passiert.\n")
    if z==7:
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
            if Position==[0,3] or Position==[6,3]:
                treffer=1
            if env[Position[0],Position[1]]!="   ":
                treffer=1
            a=abs(-OldPosition[0]+Position[0])
            b=abs(-OldPosition[1]+Position[1])
            _choice=[[-1,0],[1,0],[0,-1],[0,1]]
            _weg=0
            start=OldPosition
            for i in _choice:
                if _weg==1:
                    break
                if start[0]+i[0]<0 or start[0]+i[0]>6:
                    continue
                if start[1]+i[1]<0 or start[1]+i[1]>6:
                    continue
                if env[start[0]+i[0],start[1]+i[1]][0]==_start:
                    continue
                if env[start[0]+i[0],start[1]+i[1]]=="FH"+_start:
                    continue
                start1=[start[0]+i[0],start[1]+i[1]]
                if start1==Position:
                    _weg=1
                    break
                for i in _choice:
                    if _weg==1:
                        break
                    if start1[0]+i[0]<0 or start1[0]+i[0]>6:
                        continue
                    if start1[1]+i[1]<0 or start1[1]+i[1]>6:
                        continue
                    if env[start1[0]+i[0],start1[1]+i[1]][0]==_start:
                        continue
                    if env[start1[0]+i[0],start1[1]+i[1]]=="FH"+_start:
                        continue
                    if [start1[0]+i[0],start1[1]+i[1]]==start:
                        continue
                    start2=[start1[0]+i[0],start1[1]+i[1]]
                    if start2==Position:
                        _weg=1
                        break
                    for i in _choice:
                        if _weg==1:
                            break
                        if start2[0]+i[0]<0 or start2[0]+i[0]>6:
                            continue
                        if start2[1]+i[1]<0 or start2[1]+i[1]>6:
                            continue
                        if [start2[0]+i[0],start2[1]+i[1]]==start:
                            continue
                        if env[start2[0]+i[0],start2[1]+i[1]][0]==_start:
                            continue
                        if env[start2[0]+i[0],start2[1]+i[1]]=="FH"+_start:
                            continue
                        if [start2[0]+i[0],start2[1]+i[1]]==start1:
                            continue
                        start3=[start2[0]+i[0],start2[1]+i[1]]
                        if start3==Position:
                            _weg=1
                            break
                        for i in _choice:
                            if _weg==1:
                                break
                            if start3[0]+i[0]<0 or start3[0]+i[0]>6:
                                continue
                            if start3[1]+i[1]<0 or start3[1]+i[1]>6:
                                continue
                            if [start3[0]+i[0],start3[1]+i[1]]==start:
                                continue
                            if env[start3[0]+i[0],start3[1]+i[1]][0]==_start:
                                continue
                            if env[start3[0]+i[0],start3[1]+i[1]]=="FH"+_start:
                                continue
                            if [start3[0]+i[0],start3[1]+i[1]]==start2:
                                continue
                            start4=[start3[0]+i[0],start3[1]+i[1]]
                            if start4==Position:
                                _weg=1
                                break
#                            if Einheit[1]=="L":
#                                for i in _choice:
#                                    if _weg==1:
#                                        break
#                                    if start4[0]+i[0]<0 or start4[0]+i[0]>6:
#                                        continue
#                                    if start4[1]+i[1]<0 or start4[1]+i[1]>6:
#                                        continue
#                                    if [start4[0]+i[0],start4[1]+i[1]]==start:
#                                        continue
#                                    if env[start4[0]+i[0],start4[1]+i[1]][0]==_start:
#                                        continue
#                                    if env[start4[0]+i[0],start4[1]+i[1]]=="FH"+_start:
#                                        continue
#                                    if [start4[0]+i[0],start4[1]+i[1]]==start3:
#                                        continue
#                                    start5=[start4[0]+i[0],start4[1]+i[1]]
#                                    if start5==Position:
#                                        _weg=1
#                                        break
            if Einheit[1]=="L":
                if a<4 and b<4 and a+b<6 and treffer==0 and _weg==1:
                    break
            else:
                if a<3 and b<3 and treffer==0 and _weg==1:
                    break
            print("Bewegung nicht zulässig! Neues Zielfeld wählen!\n")
        env[OldPosition[0]][OldPosition[1]] = "   "
        env[Position[0]][Position[1]] = Einheit
        print("Welche Einheit möchtest du mit",Einheit,"angreifen?\n")
        OldPosition=Position
        while True:
            _abbr="NEIN"
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
                    if _start==env[Position[0]][Position[1]][0]:
                        break
                    if _start==env[Position[0]][Position[1]][2]:
                        break
            print("Angriff nicht zulässig! Neues Zielfeld wählen!\n")
            window=tkinter.Tk()
            window.title("Angriff abbrechen?")
            button1=tkinter.Button(window,text="Nein",command=lambda arg=1: buttonpress3(arg))
            button1.pack()
            button1.config(height = 5, width = 60)
            button2=tkinter.Button(window,text="Ja",command=lambda arg=2: buttonpress3(arg))
            button2.pack()
            button2.config(height = 5, width = 60)
            window.mainloop()
            if z==2:
                _abbr="JA"
                break
        if _abbr=="JA":
            _abbr="NEIN"
            continue
        if _start2=="N":
            Meuchel_N=0
        if _start2=="S":
            Meuchel_S=0
        temp=calc_bon(meuchel=1)
        if wuerfel(temp[0],temp[1])=="sieg_angr":
            if env[Position[0]][Position[1]][0]=="F":
                print("Sieg! Feldherr verletzt!\n")
                if _start2=="S":
                    _PunkteS+=1
                if _start2=="N":
                    _PunkteN+=1
                if _PunkteN==2 or _PunkteS==2:
                    print("- SPIELER",_start2,"GEWINNT! -\n")
                    time.sleep(5)
                    _end=True
            else:
                print("Sieg! Einheit besiegt!\n")
                env[Position[0]][Position[1]] = "   "    
        else:
            print("Kein Sieg. Nichts passiert.\n")

print("Tschüss!")