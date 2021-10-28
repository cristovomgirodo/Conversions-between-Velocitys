#############################################################################
#
# The [Algoríthm: algconbunveloc.py] will calculus the value of the velocity
# nas Unidades: [Mph] ou [Kph] ou [Mps] ou [Fts].
# Developed by Isabelle G. Girodo -- Version: 1.0
# Data: 28/10/2020
#
#############################################################################

from ConvUnidVelocidade import *

print("\n\t\t\t====================================")
print("\t\t\t* [ALGORÍTHM: ALGCONBUNVELOCID.PY] *")
print("\t\t\t====================================")

print('\n\n\tºº[ DEFINITION OF THE VARIABLES GETED IN RESULT ]ºº\n')
print('\t--[Mph]: Mile per hour')
print('\t--[Kph]: Kilometer per hour')
print('\t--[Mps]: Meter per second')
print('\t--[Fts]: Foot per second')

print("\n\n\t<<[ INSTRUCTIONS FOR USE ]>>\n")
print("\t- If the [Velocity] will calculed in [Mile per hour] key [1]")
print("\t- If the [Velocity] will calculed in [Kilometer per hour] key [2]")
print("\t- If the [Velocity] will calculed in [Meter per second]key [3]")
print("\t- If the [Velocity] will calculed in [Foot per second]key [4]")

def InstMens1():
    print("\t+ If the [Velocity Unit] is given in [Mph] key: [i] or [I].")
    return

def InstMens2():
    print("\t+ If the [Velocity Unit] is given in [Kph] key: [k] or [K].")
    return

def InstMens3():
    print("\t+ If the [Velocity Unit] is given in [Mps] key: [m] or [M].")
    return

def InstMens4():
    print("\t+ If the [Velocity Unit] is given in [Fts] key: [f] or [F].")
    return

def Resultado1():
    print("\n\t* The [Velocity] is:", format(Mph,"<10.2f"),"Mph")
    return

def Resultado2():
    print("\n\t* The [Velocity] is:", format(Kph,"<10.2f"),"Kph")
    return

def Resultado3():
    print("\n\t* The [Velocity] is:", format(Mps,"<10.2f"),"Mps")
    return

def Resultado4():
    print("\n\t* The [Velocity] is:", format(Fts,"<10.2f"),"fts")
    return

def Unidade():
    u = input("\n\t<> Select a only [previous variable] of [Velocity Unit] given in problem? ")
    return u

def View():
    print("\n\n\t\t--[NONE OF THE OPTIONS PREVIOUS WAS USED!]--")
    print("\t-_- [ USE THE PROGRAM: ALGCONBUNVELOC.PY AGAIN -- OK! ]\n")
    return

number = int(input("\n\t§ What is the [previous numerical option] that will be used? "))

if number == 1:
    print("\n\n\t\t--[VELOCITY CALCULED IS IN MILE PER HOUR(Mph)]--\n")
    InstMens2()
    InstMens3()
    InstMens4()
    unid = Unidade()
    if unid == 'k' or unid == 'K':
        Mph = Mile1()
        Solução = Resultado1()
    elif unid == 'm' or unid == 'M':
        Mph = Mile2()
        Solução = Resultado1()
    elif unid == 'f' or unid == 'F':
        Mph = Mile3()
        Solução = Resultado1()
    else:
        View()
        
elif number == 2:
    print("\n\n\t\t--[VELOCITY CALCULED IN KILOMETER PER HOUR(Kph)]--\n")
    InstMens1()
    InstMens3()
    InstMens4()
    unid = Unidade()
    if unid == 'i' or unid == 'I':
        Kph = Kilometer1()
        Solução = Resultado2()
    elif unid == 'm' or unid == 'M':
        Kph = Kilometer2()
        Solução = Resultado2()
    elif unid == 'f' or unid == 'F':
        Kph = Kilometer3()
        Solução = Resultado2()
    else:
        View()

elif number == 3:
    print("\n\n\t\t--[VELOCITY CALCULED IN METER PER SEGUNDO(Mps)]--\n")
    InstMens1()
    InstMens2()
    InstMens4()
    unid = Unidade()
    if unid == 'i' or unid == 'I':
        Mps = Meter1()
        Solução = Resultado3()
    elif unid == 'k' or unid == 'K':
        Mps = Meter2()
        Solução = Resultado3()
    elif unid == 'f' or unid == 'F':
        Mps = Meter3()
        Solução = Resultado3()
    else:
        View()

elif number == 4:
    print("\n\n\t\t--[VELOCITY CALCULED IN FOOT PER SECOND(Fts)]--\n")
    InstMens1()
    InstMens2()
    InstMens3()
    unid = Unidade()
    if unid == 'i' or unid == 'I':
        Fts = Foot1()
        Solução = Resultado4()
    elif unid == 'k' or unid == 'K':
        Fts = Foot2()
        Solução = Resultado4()
    elif unid == 'm' or unid == 'M':
        Fts = Foot3()
        Solução = Resultado4()
    else:
        View()
else:
    View()

print("\n\n\t\t\t ////")
print("\t\t\t º<º . . .[END PROGRAM -- OK!]. . .")
print("\t\t\t \-/")

input("\n\n\t\t\t. . .KEY [ENTER] TO EXIT OF THE PROGRAM!. . .\n")
    


      
