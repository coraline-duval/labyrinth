import matplotlib.pyplot as plt
import numpy as np
import random as r

# 
## Constantes : 
# chemin = 0
# mur =1
# N,S,E,O=4,5,6,7

l = 30 #largeur = longeur
depart =[0,0] #case de départ
sortie =[l-1,l-1]

##Variables :  matrice M cube mur ; liste N de tt les sommets (tte les cases) ; liste U vide qui contiendra les sommets utilisés et liste vide F qui contidendra les frontières au Laby

U=[] #sert pour trouver les cases frontières qui ne sont pas ds le L--> pas dans U
F=[]

M=np.ones((l,l,2)) #ligne,colonnes, profondeur (0 correspond a est/droite et 1 à Sud)
 

## Fonctions intermédiaires

def recherche_sequentielle1 (U,x,y):
    for i in range (len(U)):
        if U[i]==[x,y]:
            return [x,y]
    return []

def declare_frontiere (x,y,F,U) : #ajoute à F les frontière pas dans le laby d'une case [x,y]
    if x+1<=l-1 and recherche_sequentielle1(U,x+1,y)!=[x+1,y] and recherche_sequentielle1(F,x+1,y)!=[x+1,y]:            #case à droite
        F.append([x+1,y])
    if x-1>=0 and recherche_sequentielle1(U,x-1,y)!=[x-1,y] and recherche_sequentielle1(F,x-1,y)!=[x-1,y]:            #case à gauche
        F.append([x-1,y])
    if y-1>=0 and recherche_sequentielle1(U,x,y-1)!=[x,y-1] and recherche_sequentielle1(F,x,y-1)!=[x,y-1]:            #case en dessous
        F.append([x,y-1])
    if y+1<=l-1 and recherche_sequentielle1(U,x,y+1)!=[x,y+1] and recherche_sequentielle1(F,x,y+1)!=[x,y+1]:          #case au dessus
        F.append([x,y+1])
    return F
    
def detruit_mur (x,y,M,U):
    # on détruit de manière aléaoire un mur voisin accolé du labyrinthe
    P=[] #liste des murs possible à détruire
    if recherche_sequentielle1(U,x+1,y)==[x+1,y]: #case en dessous de[x,y]
        P.append([x,y,1])

    if recherche_sequentielle1(U,x-1,y)==[x-1,y]:  #case au dessus
        P.append([x-1,y,1])
        
    if recherche_sequentielle1(U,x,y+1)==[x,y+1]:  #case a droite
        P.append([x,y,0])
        
    if recherche_sequentielle1(U,x,y-1)==[x,y-1]:  #case a gauche 
        P.append([x,y-1,0])
        
    if recherche_sequentielle1(U,x,y-1)!=[x,y-1] and recherche_sequentielle1(U,x,y+1)!=[x,y+1] and recherche_sequentielle1(U,x-1,y)!=[x-1,y] and recherche_sequentielle1(U,x+1,y)!=[x+1,y] :
        return None
        
    [a,b,c]=r.choice(P)
    M[a,b,c]=0
    return M

## algorithme :
 
[x,y]=depart

U.append([x,y])
F=declare_frontiere (x,y,F,U)
while F!=[]:
    [x,y]=r.choice(F) #on prend au hasard une des frontières pas dans le L (tte les frontières ont le meme "poid"/distance au L)
    F.remove ([x,y])
    F=declare_frontiere(x,y,F,U)
    M=detruit_mur(x,y,M,U)
    U.append([x,y])
    
## Dessin : liste pour tracer les bords (-entrée/sortie) puis fonction qui trace le reste du labyrinthe


def bords (l):
    borda=[0]*(l+1)               
    bordo=[]
    for i in range(l+1): #bord gauche
        bordo.append(i)
    
    bordo=bordo+[l]*(l) #bord du haut - 1ere case : entrée
    for i in range(1,l+1):   
        borda.append(i)
    
    borda=borda+[l]*(l+1)   #bord droit
    for i in range(l+1):   
        bordo.append(l-i)
    
    bordo=bordo+[0]*(l) #bord du bas - dernière case : sortie
    for i in range(l):   
        borda.append(l-i)
    return borda, bordo

def trace_labyrinthe(M):
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
    plt.show()




