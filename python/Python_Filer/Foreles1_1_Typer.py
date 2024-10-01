#variabler og typer
kurs:int = 37
pi:float = 3.14
name:str = "Richard"
print(pi, name)

point:tuple= (1,1,1)
weekdays:tuple = (1,2,3,4,5,6,7)

print(f'Ukedager: {weekdays}')

ricdata:tuple = ("Richard", 1963)
print(ricdata)


#Tupler
import math
p1 = (1,1)
p2 = (3,3)
dist = math.dist(p1,p2)
print (f'Avstanden mellom{p1} og {p2} : {dist}')