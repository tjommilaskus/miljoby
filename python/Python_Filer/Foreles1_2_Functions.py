# 1. Functions must be defined before usag
# 2. Variables, THAT change muest be defined by the global keyword



def summer(x, y):
    return x+y

print (summer(2,4))


def summer_tupple(t1, t2):
    return t1+t2

def summer_tupple2(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]

a = (1,1)
b = (2,1)

print (summer_tupple2(a,b))
