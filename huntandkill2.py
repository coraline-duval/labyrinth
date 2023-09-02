import matplotlib.pyplot as plt
import numpy as np
import random as r

## Constantes : 
# chemin = 0
# mur =1
# N,S,E,O=4,5,6,7

l = 50 #largeur = longeur
depart =[0,0] #case de départ
sortie =[l-1,l-1]


##Variables : matrice M cube mur,liste U vide qui contiendra les cases utilisés
U=[]
M=np.ones((l,l,2)) #ligne,colonnes, profondeur (0 correspond a est/droite et 1 à Sud)

## Fonctions intermédiaires : hunt , kill (1 case à la fois ou non)

def recherche_sequentielle1 (U,x,y): 
    for i in range (len(U)):
        if U[i]==[x,y]: 
            return [x,y]
    return []

def direction_possible (U,x,y):
    '''evalue quelles sont les cases voisines qui ne sont ni hors des frontières du labyrinthe ni deja dans le labyrinthe pour garder celle qui peuvent être ajouté au L '''
    D=[4,5,6,7] # N,S,E,O
    if x==0 or recherche_sequentielle1(U,x-1,y)==[x-1,y]:
        D.remove(4)
    if x==l-1 or recherche_sequentielle1(U,x+1,y)==[x+1,y]:
        D.remove(5)
    if y==l-1 or recherche_sequentielle1(U,x,y+1)==[x,y+1]:
        D.remove(6)
    if y==0 or recherche_sequentielle1(U,x,y-1)==[x,y-1]:
        D.remove(7)
    return D
    
def tue (M,U,x,y):
    """a partir de la case précédente x,y il regarde quelle case est possible (cf fonction précéndente), en pioche une au hasard puis l'ajoute au L """
    D=direction_possible (U,x,y)
    if D==[]:
        return M,U,-1,-1 #quand il n'y a plus de direction libre, coordonées pour lancer le mode chasse
    else : 
        sens=r.choice(D)
        if sens==4:
            M[x-1,y,1]=0
            U.append([x-1,y])
            return M,U,x-1,y
        if sens==5:
            M[x,y,1]=0
            U.append([x+1,y])
            return M,U,x+1,y
        if sens==6:
            M[x,y,0]=0
            U.append([x,y+1])
            return M,U,x,y+1
        if sens==7:
            M[x,y-1,0]=0
            U.append([x,y-1])
            return M,U,x,y-1
    

def cases_non_visitees (U,i): 
    '''cases de la ligne i qui ne sont pas dans le labyrinthe'''
    cnv=[]
    for k in range(l):
        if recherche_sequentielle1(U,i,k)!=[i,k]:
            cnv.append([i,k])
    return cnv
    
    
def cases_adjacentes(U,i): 
    '''cases de la ligne i qui ne sont pas dans le labyrinthe et qui sont à côté d'une case du labyrinthe.'''
    ca=[]
    cnv=cases_non_visitees(U,i)
    for j in range (len(cnv)):
        [i,k]=cnv[j]
        if recherche_sequentielle1(U,i-1,k)==[i-1,k]:
            ca.append([i,k,i-1,k,1]) #pour savoir quel mur enlever
        if recherche_sequentielle1(U,i+1,k)==[i+1,k]:
            ca.append([i,k,i,k,1])
        if recherche_sequentielle1(U,i,k-1)==[i,k-1]:
            ca.append([i,k,i,k-1,0])
        if recherche_sequentielle1(U,i,k+1)==[i,k+1]:
            ca.append([i,k,i,k,0])
    return ca
        
def chasse (U):
    """parcours ligne par ligne de haut en bas le labyrinthe à la recherche d'une case vide accolé au labyrithe, si il en trouve une, il l'ajoute au labyrinthe."""    
    i=0
    while i<l:
        ca=cases_adjacentes(U,i)
        if ca!=[]:
            [x,y,a,b,c]=r.choice(ca)
            M[a,b,c]=0
            U.append([x,y])   #on eneleve le mur entre le labyrithe et la case choisie pour redemarrer chasse
            return [x,y]            
        else :
            i+=1
    return [-2,-2] #valeur qui veut dire liste vide
        
    
## algorithme : parcours (tue) le L jusqu'a ne peut plus, puis chasse pr une case vide jusqu'a ce qu'il n'y ait plus de case vide--> L fini

[x,y]=depart
U.append([x,y])
while chasse(U) !=[-2,-2]:
    while [x,y]!=[-1,-1]:
        M,U,x,y=tue(M,U,x,y)
    [x,y]=chasse(U)


## Dessin : liste pour tracer les bords puis fonction qui trace le reste du labyrinthe


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

        