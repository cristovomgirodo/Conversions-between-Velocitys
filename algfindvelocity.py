############################################################################
#
# The [Algoríthm: algfindvelocity.py] will find the [value] of the velocity
# nas Unidades: [Mph] ou [Kph] ou [Mps] ou [Fps].
# Developed by Cristovom A. Girodo 
# Date: 20230605  -- Version: 2.0(Stable)
#
############################################################################


print("\n\t\t\t====================================")
print("\t\t\t* [ALGORÍTHM: ALGFINDVELOCITY.PY] *")
print("\t\t\t====================================")

print('\n\n\tºº[ DEFINITION OF THE VARIABLES GETED IN RESULT ]ºº\n')
print('\t--[Mph]: Mile per hour')
print('\t--[Kph]: Kilometer per hour')
print('\t--[Mps]: Meter per second')
print('\t--[Fps]: Foot per second')

print("\n\n\t*[ INSTRUCTIONS FOR USE ]*\n")
print("\t------------------------------------------------------------")
print("\t- To [conversion] of the [Velocity]: [Kph] to [Mph] key [1].")
print("\t- To [conversion] of the [Velocity]: [Mps] to [Mph] key [2].")
print("\t- To [conversion] of the [Velocity]: [Fps] to [Mph] key [3].")
print("\t------------------------------------------------------------")
print("\t- To [conversion] of the [Velocity]: [Mph] to [Kph] key [4].")
print("\t- To [conversion] of the [Velocity]: [Mps] to [Kph] key [5].")
print("\t- To [conversion] of the [Velocity]: [Fps] to [Kph] key [6].")
print("\t------------------------------------------------------------")
print("\t- To [conversion] of the [Velocity]: [Mph] to [Mps] key [7].")
print("\t- To [conversion] of the [Velocity]: [Kph] to [Mps] key [8].")
print("\t- To [conversion] of the [Velocity]: [Fps] to [Mps] key [9].")
print("\t------------------------------------------------------------")
print("\t- To [conversion] of the [Velocity]: [Mph] to [Fps] key [10].")
print("\t- To [conversion] of the [Velocity]: [Kph] to [Fps] key [11].")
print("\t- To [conversion] of the [Velocity]: [Mps] to [Fps] key [12].")
print("\t-------------------------------------------------------------\n")

from unidvelocityconvequat import *

print('\t\t- Select an only [previous option] given -- Ok!')
number = introduce()

if number == 1:
	print(f'\t-- The velocity in [Mph] is: {speed.KilometerToMile():<10.2f}')

elif number == 2:
	print(f'\t-- The velocity in [Mph] is: {speed.MeterToMile():<10.2f}')
	
elif number == 3:
	print(f'\t-- The velocity in [Mph] is: {speed.FootToMile():<10.2f}')

elif number == 4:
	print(f'\t-- The velocity in [Kph] is: {speed.MiletoKilometer():<10.2f}')
	
elif number == 5:
	print(f'\t-- The velocity in [Kph] is: {speed.MeterToKilometer():<10.2f}')
	
elif number == 6:
	print(f'\t-- The velocity in [Kph] is: {speed.FootToKilometer():<10.2f}')
	
elif number == 7:
	print(f'\t-- The velocity in [Mps] is: {speed.MileToMeter():<10.2f}')
	
elif number == 8:
	print(f'\t-- The velocity in [Mps] is: {speed.KilometerToMeter():<10.2f}')
	
elif number == 9:
	print(f'\t-- The velocity in [Mps] is: {speed.FootToMeter():<10.2f}')
	
elif number == 10:
	print(f'\t-- The velocity in [Fps] is: {speed.MileToFoot():<10.2f}')

elif number == 11:
	print(f'\t-- The velocity in [Fps] is: {speed.KilometerToFoot():<10.2f}')

elif number == 12:
	print(f'\t-- The velocity in [Fps] is: {speed.MeterToFoot():<10.2f}')
	
else:
	print("\n\n\t\t--[NONE OF THE OPTIONS PREVIOUS WAS USED!]--")
	print("\t-_- [ USE THE PROGRAM: ALGFINDVELOCITY.PY] AGAIN -- OK! ]\n")
	
print("\n\n\t\t\t ////")
print("\t\t\t º<º . . .[END PROGRAM -- OK!]. . .")
print("\t\t\t \-/")

input("\n\n\t\t. . .KEY [ENTER] TO EXIT OF THE PROGRAM!. . .\n")
      


