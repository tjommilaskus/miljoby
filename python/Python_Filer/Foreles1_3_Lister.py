

#funksjoner & lister
def kvadrer(n):
    return n*n

list0 = [1,2,3,4,5,6]
list1 = []

for x in list0:
    list1.append(kvadrer(x))
#alternativt
print(list0)
print(list1)

list2 = [x * x for x in list0]
print(list2)

list3 = [kvadrer(x) for x in list0]
print(list3)

# Hva i all verden foregår her ????
list4 = list(map(kvadrer, list3))
# Create and write to a file

print( list4 )

#Datoer
from datetime import date
d0 = date(2024, 1, 1)
d1 = date(2024, 4, 1)
delta = d1 - d0
print(f'Antall dager mell 1.jan og 1.april : {delta.days}')


#Slicing (oppdeling) av lister
daysY:list = list(range(1,365))
daysJan = daysY[0:30:1]
print(f'Januar {daysJan}')


#create a list from 1..100
daysW = list(range(1,7))
print (daysW)
print (f'mandag-onsdag {daysW[0:2]}' )


#en annen type liste som er mye brukt
import numpy as np
days2x = np.linspace(2, 20, 10)
print (days2x)

