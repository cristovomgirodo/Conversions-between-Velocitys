#
# The ConvUnidVelocidade.py module 
# Developed by Isabelle G. Girodo
# Data: 28/10/2020
# 

import math

def MileVelocityUnit():
    M = eval(input("\n\t@ Enter with the new [numerical] value of the [velocity] without write\n\t  the [Mile per hour(Mph)] Unit? "))
    return M

def KilometerVelocityUnit():
    K = eval(input("\n\t@ Provide the new [numerical] value of the [velocity] without write\n\t  the [Kilometer per hour(Kph)] Unit? "))
    return K

def MeterVelocityUnit():
    m = eval(input("\n\t@ Type the new [numerical] value of the [velocity] without write\n\t  the [Meter per second(Mps)] Unit? "))
    return m

def FootVelocityUnit():
    P = eval(input("\n\t@ Give the new [numerical] value of the [velocity] without write\n\t  the [Foot per second(Fts)] Unit? "))
    return P

def Mile1():
    Kph = KilometerVelocityUnit()
    mph1 = 0.6215 * Kph
    return mph1

def Mile2():
    Mps = MeterVelocityUnit()
    mph2 = 2.2361 * Mps
    return mph2

def Mile3():
    Fts = FootVelocityUnit()
    mph3 = 0.6818 * Fts
    return mph3

def Kilometer1():
    Mph = MileVelocityUnit()
    kph1 = 1.609 * Mph
    return kph1

def Kilometer2():
    Mps = MeterVelocityUnit()
    kph2 = 3.6 * Mps
    return kph2

def Kilometer3():
    Fts = FootVelocityUnit()
    kph3 = 1.0969 * Fts
    return kph3

def Meter1():
    Mph = MileVelocityUnit()
    mps1 = 0.4472 * Mph
    return mps1

def Meter2():
    Kph = KilometerVelocityUnit()
    mps2 = 0.2778 * Kph
    return mps2

def Meter3():
    Fts = FootVelocityUnit()
    mps3 = 0.3047 * Fts
    return mps3

def Foot1():
    Mph = MileVelocityUnit()
    Fts1 = 1.4667 * Mph
    return Fts1

def Foot2():
    Kph = KilometerVelocityUnit()
    Fts2 = 0.9117 * Kph
    return Fts2

def Foot3():
    Mps = MeterVelocityUnit()
    Fts3 = 3.2820 * Mps
    return Fts3

    
    
    
    
