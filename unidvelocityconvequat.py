######################################################
#
#   The unidvelocityconvequat.py module
#   Developed by Cristovom A. Girodo
#   Date: 20230603 -- Version: 2.0(Stable)
#
######################################################

import math

def introduce():
    while True:
        try:
            def enterIntegerData():
                x = int(input('\t\t(º>º) Provide the [new] value? '))
                return x
            coeffic = enterIntegerData()

            while coeffic <= 0:
                print('\n\t*[ NO TYPE AN [NEGATIVE INTEGER NUMBER] or equal [ZERO]--Ok! ]*\n')
                coeffic = enterIntegerData()

            print('\t    **[The typed number]:',coeffic,'is a [valid float number!]**\n')
            return coeffic
        except ValueError as err:
            print('\t    ###')
            print('\t    º>º [Warning!]:',err)
            print('\t    \~/ [TYPE AN NEW POSITIVE INTEGER NUMBER IN NEXT INSTRUCTION -- OK!]\n')   

def realNumber():
    while True:
        try:
            def enterFloatData():
                y = float(input('\t(ª<ª) Enter the [new] value? '))
                return y
            coeffic1 = enterFloatData()

            while coeffic1 <= 0:
                print('\n\t*[ NO TYPE AN [NEGATIVE FLOAT NUMBER] or equal [ZERO]--Ok! ]*\n')
                coeffic1 = enterFloatData()

            print('\t**[ [The typed number]:',coeffic1,'is a [valid positive float number!] ]**\n')
            return coeffic1
        except ValueError as err:
            print('\t   _/§\_')
            print('\t    @<@ [Warning!]:',err)
            print('\t    \~/ [ TYPE AN [NEW POSITIVE FLOAT NUMBER ]')
            print('\t        [ IN NEXT INSTRUCTION -- OK! ]\n')

def title1():
    print('\n\t--[VELOCITY GIVEN IN MILE PER HOUR(MPH)]--')
    return

def title2():
    print('\n\t--[VELOCITY GIVEN IN KILOMETER PER HOUR(KPH)]--')
    return

def title3():
    print('\n\t--[VELOCITY GIVEN IN METER PER SECOND(MPS)]--')
    return

def title4():
    print('\n\t--[VELOCITY GIVEN IN FOOT PER SECOND(FPS)]--')
    return

def result():
    print('\t**[ANSWER]**')
    return

class Velocity:
    """Find the velocitys to conversions"""
    def __init__(self, mph=0, kph=0, mps=0, fps=0):
        self.mph = mph
        self.kph = kph
        self.mps = mps
        self.fps = fps

    def KilometerToMile(self):
        """Find the velocity in mile per hour."""
        title2()
        self.kph = realNumber()
        result()
        self.mph = 0.6215 * self.kph
        return self.mph

    def MeterToMile(self):
        """Find the velocity in mile per hour."""
        title3()
        self.mps = realNumber()
        result()
        self.mph = 2.2361 * self.mps
        return self.mph

    def FootToMile(self):
        """Find the velocity in mile per hour."""
        title4()
        fps = realNumber()
        result()
        self.mph = 0.6818 * fps
        return self.mph

    def MiletoKilometer(self):
        """Find the velocity in kilometer per hour."""
        title1()
        self.mph = realNumber()
        result()
        self.kilometer = 1.609 * self.mph
        return self.kilometer

    def MeterToKilometer(self):
        """Find the velocity in kilometer per hour."""
        title3()
        self.mps = realNumber()
        result()
        self.kilometer = 3.6 * self.mps
        return self.kilometer

    def FootToKilometer(self):
        """Find the velocity in kilometer per hour."""
        title4()
        self.fps = realNumber()
        result()
        self.kilometer = 1.0969 * fps
        return self.kilometer

    def MileToMeter(self):
        """Find the velocity in meter per second."""
        title1()
        self.mph = realNumber()
        result()
        self.mps = 0.4472 * self.mph
        return self.mps

    def KilometerToMeter(self):
        """Find the velocity in meter per second."""
        title2()
        self.kph = realNumber()
        result()
        self.mps = 0.2778 * self.kph
        return self.mps

    def FootToMeter(self):
        """Find the velocity in meter per second."""
        title4()
        self.fps = realNumber()
        result()
        self.mps = 0.3047 * self.fps
        return self.mps
        
    def MileToFoot(self):
        """Find the velocity in foot per second."""
        title1()
        self.mph = realNumber()
        result()
        self.fps = 1.4667 * self.mph
        return self.fps

    def KilometerToFoot(self):
        """Find the velocity in foot per second."""
        title2()
        self.kph = realNumber()
        result()
        self.fps = 0.9117 * self.kph
        return self.fps

    def MeterToFoot(self):
        """Find the velocity in foot per second."""
        title3()
        self.mps = realNumber()
        result()
        self.fps = 3.2820 * self.mps
        return self.fps
                     
# create the speed object
speed = Velocity()


	
        
        
