import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from math import *

def f1(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=-10*i+(150-t*10)
        if tab[i]<0:
            tab[i]=0
    return current_tab

def f2(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=10*i+(-150+t*10)
    return current_tab

def f2bis(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=10*i-(t*10)
    return current_tab

def f3(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=abs(10*i-70)-70+t*10
    return current_tab

def f4(t,tab,t_total):
    current_tab = tab
    if t>=3:
        for i in range(len(tab)):
            tab[i]=round(((1.4285*(4-t))*abs(i-7)+t*10+80)/10)*10
    else:
        for i in range(len(tab)):
            tab[i]=round(((1.4285+2.857*(4-1-t))*abs(i-7)+(10*t+80))/10)*10
    return current_tab

def f5(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        if t<=10:
            tab[i]=(-t*abs(i-7)+120)
        else:
            tab[i]=(-10*abs(i-7)+120-(t-10)*10)
    return current_tab

def mouvement(function,init_y,temps):
    for i in range(0,temps):
        plt.clf()
        function(i,init_y,temps)
        plt.bar(range(15),init_y,color="blue")
        plt.ylim(0,150)
        plt.pause(0.1)

    return init_y

init_y = [0 for i in range(15)]
mouvement(f1,init_y,15)
print(init_y)
mouvement(f2,init_y,15)
mouvement(f2bis,init_y,15)
mouvement(f3,init_y,15)
mouvement(f4,init_y,5)
print(mouvement(f5,init_y,23))
plt.show()