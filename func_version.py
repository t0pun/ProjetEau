import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def f1(t,tab):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=-10*i+(150-t*10)
        if tab[i]<0:
            tab[i]=0
    return current_tab

def f2(t,tab):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=10*i+(-150+t*10)
    return current_tab

def f2bis(t,tab):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=10*i-(t*10)
    return current_tab

def f3(t,tab):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=abs(10*i-70)-70+t*10
    return current_tab

def mouvement(function,init_y):
    for i in range(0,16):
        plt.clf()
        print(function(i,init_y))
        plt.bar(range(15),init_y,color="blue")
        plt.ylim(0,150)
        plt.pause(0.5)

    return init_y

init_y = [0 for i in range(15)]
mouvement(f1,init_y)
mouvement(f2,init_y)
mouvement(f2bis,init_y)
mouvement(f3,init_y)
plt.show()