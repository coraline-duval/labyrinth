import matplotlib.pyplot as plt
import numpy as np
import random as r

## Constantes : 
# chemin = 0
# mur =1
# N,S,E,O=4,5,6,7
#depart et sortie déjà défini avec le programme qui fait M

tmax= 3600*8 #secondes en 1h*nmb heure --> temps max avant abandon
#matrice M qui a été exécuter par un autre programme
odepart=4 #orientation est l'orientation derriere nous (de la où on arrive)

##Variables :  

t=0 #mesure le temps passé dans le L
[x,y]=depart #position dans le L de la personne qui le parcourt
orientation=odepart #orientation de la personne qui permet de se placer comme elle dans le L et prendre meme type de decision


## Fonctions intermédiaires

def recherche_sequentielle2 (D,o):
    for i in range (len(D)):
        if D[i]==o:
            return o
    return None

def direction_possibles(M,x,y):
    """cases vers lesquelles on peut aller à partir d'une position x,y (pas de mur et pas hors du L)"""
    D=[4,5,6,7] # N,S,E,O
    if x==0 or M[x-1,y,1]==1:
        D.remove(4)
    if x==l-1 or M[x,y,1]==1:
        D.remove(5)
    if y==l-1 or M[x,y,0]==1:
        D.remove(6)
    if y==0 or M[x,y-1,0]==1:
        D.remove(7)
    return D

def parcourt (x,y,direction):
    '''avance d'une case selon une direction donné et défini l'orientation suivante'''
    if direction==4: #Nord
        x=x-1
        orientation=5 #le sud est derrière nous
    if direction==5: #Sud
        x=x+1 
        orientation=4
    if direction==6: #Est
        y=y+1
        orientation=7
    if direction==7: #Ouest
        y=y-1
        orientation=6
    return x,y,orientation


def cases_intuitives (M,x,y,orientation): 
    """ donne une direction via les cases que préfère l'H (pas revenir sur ses pas sauf impasse) dans les cases possibles"""
    D=direction_possibles(M,x,y)
    direction=0
    if D!=[orientation]: #si on n'est pas dans une impasse
        preferee=orientation_preferee(orientation,M,x,y) #il n'y a pas le choix de revenir sur ses pas (car pas ds une impasse) car le choix n'est pas dans preferee
        direction=r.choice(preferee) 
    else : #on est alors dans une impasse, car la seule orientation possible est celle d'où l'on vient. 
        direction=D[0] #on revient en arrière et on aura 2 possibilités de direction, elle va donc enlever celle d'où on vient, ce qui permet de sortir de l'impasse 
    return direction


def orientation_preferee(orientation,M,x,y):
    '''enleve le choix de l'impasse et pondere le choix de direction : d'abord devant, puis a droite et enfin à gauche)'''
    D=direction_possibles(M,x,y)
    preferee=[]
    if orientation==4: #nord derriere moi
        for k in range (len(D)):
            if D[k]==5: #Devant pondéré à 10/20
                preferee=preferee+10*[5]
            if D[k]==6:#Droite pondéré à 7
                preferee=preferee+7*[6]
            if D[k]==7:#gauche pondéré à 3
                preferee=preferee+3*[7]
    if orientation==5:
        for k in range (len(D)):
            if D[k]==4: #Devant pondéré à 10/20
                preferee=preferee+10*[4]
            if D[k]==7:#Droite pondéré à 7
                preferee=preferee+7*[7]
            if D[k]==6:#gauche pondéré à 3
                preferee=preferee+3*[6]
    if orientation==6:
        for k in range (len(D)):
            if D[k]==7: #Devant pondéré à 10/20
                preferee=preferee+10*[7]
            if D[k]==5:#Droite pondéré à 7
                preferee=preferee+7*[5]
            if D[k]==4:#gauche pondéré à 3
                preferee=preferee+3*[4]
    if orientation==7:
        for k in range (len(D)):
            if D[k]==6: #Devant pondéré à 10/20
                preferee=preferee+10*[6]
            if D[k]==4:#Droite pondéré à 7
                preferee=preferee+7*[4]
            if D[k]==5:#gauche pondéré à 3
                preferee=preferee+3*[5]
    return preferee
    

## Algorithme
P=[depart]
while t<tmax and [x,y]!=sortie: 
    direction = cases_intuitives(M,x,y,orientation)
    x,y,orientation=parcourt(x,y,direction)
    t+=2  
    P.append([x,y])
if t>=tmax:
    print ("Game over")
else :
    print ("Sortie atteinte !")



"""possibilité de complication de l'algo 

ligne 67


Construire le ruban sous forme de liste pondérée :
items = [‘server1′] * 10 + [‘server2′] * 45 + [‘server3′] * 34
2) Ne pas mélanger
3) Choisir un nombre x au hasard entre 0 et 88, et retourner items[x]"""