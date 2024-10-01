def SummerTreTall(tallA=0, tallB=0, tallC=0):
    return tallA+tallB+tallC


print(SummerTreTall(10,15,20))
print(SummerTreTall(tallA=10, tallB=10))
print(SummerTreTall(tallC=10, tallA=20))


#must use global, because we are changing the variable x
def incrementX(n=1):
    global x
    x = x + n

x = 100
incrementX(55)
print(x)