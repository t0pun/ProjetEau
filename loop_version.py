import matplotlib
import matplotlib.pyplot as plt

import numpy as np

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

x = [i for i in range(15)]
hauteur_max =150
hauteur_min =0
init_y = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50,40,30,20,10]

##Groupe:Anas/Ilyas
def mouvement1(Max,Min,transition,NS,S,indexTemoin):

    while(S[indexTemoin] > Min):
        plt.clf()
        for i in range(15):
            S[i] = (S[i] - transition)
            if S[i] < 0 :
                S[i] = 0
        plt.bar(range(15),S,color="blue")
        plt.ylim(Min,Max)
        plt.pause(0.1)

    return S

##Groupe:Ayoub/Nabil
def mouvement2_iter(hauteur_max,hauteur_min,nombre_source,scale):

    for i in range(0,nombre_source):
        plt.clf()
        y = init_y
        for j in range(nombre_source-1,nombre_source-2-i,-1):
            y[j]=y[j]+scale

        data = np.column_stack((np.arange(len(y)),y))
        plt.bar(x,y,align='center',color="blue")
        plt.ylim(hauteur_min,hauteur_max)
        plt.pause(0.1)

    return y

##Groupe : Thomas/Abdullah
def mv3(size):
    all_tab = []
    tab_temp = []
    j = 8  # milieu+1
    for i in range(6, -1, -1):
        tab_temp = init_y
        tab_temp[i] = tab_temp[i + 1] + 10
        if j < size:
            tab_temp[j] = tab_temp[j - 1] + 10
            j= j+1
        all_tab.append(tab_temp)
        plt.clf()
        plt.bar(range(15),tab_temp,color="blue")
        plt.ylim(0,150)
        plt.pause(0.1)
    while tab_temp[0]<150:
        tab_temp = init_y
        for u in range(6, -1,-1):
            tab_temp[u]+=10
        for r in range(7,15):
            tab_temp[r]+=10
        all_tab.append(tab_temp)
        plt.clf()
        plt.bar(range(15),tab_temp,color="blue")
        plt.ylim(0,150)
        plt.pause(0.1)
    
    return tab_temp

def mouvement_fin(hauteur_max,hauteur_min,nombre_source,scale):
    y = init_y
    while(len(set(y))!=1):
        plt.clf()
        for i in range(len(y)):
            if(y[i]<120):
                y[i]+=10
            elif(y[i]>120):
                y[i]-=10

        print(y)
        data = np.column_stack((np.arange(len(y)),y))
        plt.bar(x,y,align='center',color="blue")
        plt.ylim(hauteur_min,hauteur_max)
        plt.pause(0.1)

    all_tab = []
    tab_temp = []
    j = 8  # milieu+1
    for i in range(6, -1, -1):
        tab_temp = init_y
        tab_temp[i] = tab_temp[i + 1] - 10
        if j < 15:
            tab_temp[j] = tab_temp[j - 1] - 10
            j= j+1
        all_tab.append(tab_temp)
        plt.clf()
        plt.bar(range(15),tab_temp,color="blue")
        plt.ylim(0,150)
        plt.pause(0.1)
        print(tab_temp)
    while tab_temp[0]>150:
        tab_temp = init_y
        for u in range(6, -1,-1):
            tab_temp[u]-=10
        for r in range(7,15):
            tab_temp[r]-=10
        print(tab_temp)
        all_tab.append(tab_temp)
        plt.clf()
        plt.bar(range(15),tab_temp,color="blue")
        plt.ylim(0,150)
        plt.pause(0.1)

    while(len(set(y))!=1 and y[6]>=0):
        plt.clf()
        for i in range(len(y)):
            if(y[i]>0):
                y[i]-=10
        print(tab_temp)

        data = np.column_stack((np.arange(len(y)),y))
        plt.bar(x,y,align='center',color="blue")
        plt.ylim(hauteur_min,hauteur_max)
        plt.pause(0.01)

    return init_y

init_y = mouvement1(150,0,15,10,init_y,0)
init_y = mouvement2_iter(150,0,15,10)
init_y = mouvement1(150,0,15,10,init_y,14)
init_y = mv3(15)
print(mouvement_fin(150,0,15,10))

# plt.show()