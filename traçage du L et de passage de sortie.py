import matplotlib.pyplot as plt
import numpy as np
import random as r



def bords (l):
    borda=[0]*(l+1)               
    bordo=[]
    for i in range(l+1): #bord gauche
        bordo.append(i)
    
    bordo=bordo+[l]*(l+1) #bord du haut
    for i in range(l+1):   
        borda.append(i)
    
    borda=borda+[l]*(l+1)   #bord droit
    for i in range(l+1):   
        bordo.append(l-i)
    
    bordo=bordo+[0]*(l+1) #bord du bas
    for i in range(l+1):   
        borda.append(l-i)
    return borda, bordo

def trace_labyrinthe_solution(M):
    plt.clf()
    
    for i in range (l):
        a=[] #abscisse
        o=[] #ordonnée
        for j in range(l):
            a=[] #abscisse
            o=[] #ordonnée
            if M[i,j,0]==1: #mur est à la case i,j présent            
                a.append(j+1) #cf dessin
                a.append(j+1)
                o.append(l-i)
                o.append(l-1-i)
            if M[i,j,1]==1: #mur sud à la case i,j present 
                a.append(j)
                a.append(j+1)
                o.append(l-i-1)
                o.append(l-i-1)
            plt.plot(a,o,color = "black")
    
    eo = [l-depart[0],l-depart[0]] # liste de l'ordonnée de l'entrée
    ea=[depart[0],depart[0]+1]
    so = [l-sortie[1]-1,l-sortie[1]-1] # liste de l'ordonnée de la sortie
    sa=[sortie[1],sortie[1]+1]
    
    borda, bordo = bords(l)
    plt.plot(borda,bordo,color = "black")
    plt.plot(ea,eo,color = "white")
    plt.plot(sa,so,color = "white")
    plt.axis("equal")
    
    
    b=[]#abscisse du chemin pris par l'homme
    c=[]#ordonée du chemin pris par l'homme

    for i in range(len(P)):
        [g,h]=P[i]
        b.append(h+0.5)
        c.append(l-0.5-g)
    plt.plot(b,c,color = "red")
    plt.show()

        