import matplotlib.pyplot as plt
import numpy as np
import random as r
###CONSTANTES :

depart=[0,0]

tmax= 3600*8 #secondes en 1h*nmb heure --> temps max avant abandon
#matrice M qui a été exécuter par un autre programme
odepart=4 #orientation est l'orientation derriere nous (de la où on arrive)
 #l à definir pr les stats

###FONCTIONS

def recherche_sequentielle1 (U,x,y): 
    for i in range (len(U)):
        if U[i]==[x,y]: 
            return [x,y]
    return []

## Fonctions de hunt and kill 
def direction_possible (U,x,y,l):
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
    
def tue (M,U,x,y,l):
    """a partir de la case précédente x,y il regarde quelle case est possible (cf fonction précéndente), en pioche une au hasard puis l'ajoute au L """
    D=direction_possible (U,x,y,l)
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
        if sens==6: #Est
            M[x,y,0]=0
            U.append([x,y+1])
            return M,U,x,y+1
        if sens==7:
            M[x,y-1,0]=0
            U.append([x,y-1])
            return M,U,x,y-1
    

def cases_non_visitees (U,i,l): 
    '''cases de la ligne i qui ne sont pas dans le labyrinthe'''
    cnv=[]
    for k in range(l):
        if recherche_sequentielle1(U,i,k)!=[i,k]:
            cnv.append([i,k])
    return cnv
    
    
    
def cases_adjacentes(U,i,l): 
    '''cases de la ligne i qui ne sont pas dans le labyrinthe et qui sont à côté d'une case du labyrinthe.'''
    ca=[]
    cnv=cases_non_visitees(U,i,l)
    for j in range (len(cnv)):
        [i,k]=cnv[j]
        if recherche_sequentielle1(U,i-1,k)==[i-1,k]: #case au sud
            ca.append([i,k,i-1,k,1]) #pour savoir quel mur enlever
        if recherche_sequentielle1(U,i+1,k)==[i+1,k]:#Nord
            ca.append([i,k,i,k,1])
        if recherche_sequentielle1(U,i,k-1)==[i,k-1]:#Ouest
            ca.append([i,k,i,k-1,0])
        if recherche_sequentielle1(U,i,k+1)==[i,k+1]:#Est
            ca.append([i,k,i,k,0])
    return ca
        
def chasse (U,M,l):
    """parcours ligne par ligne de haut en bas le labyrinthe à la recherche d'une case vide accolé au labyrithe, si il en trouve une, il l'ajoute au labyrinthe."""    
    i=0
    while i<l:
        ca=cases_adjacentes(U,i,l)
        
        if ca!=[]:
            [x,y,a,b,c]=r.choice(ca)
            
            M[a,b,c]=0
            
            U.append([x,y])   #on eneleve le mur entre le labyrithe et la case choisie pour redemarrer chasse
            return [x,y]            
        else :
            i+=1
    return [-2,-2] #valeur qui veut dire liste vide
    
## Fonction de prim's

def declare_frontiere (x,y,F,U,l) : #ajoute à F les frontière pas dans le laby d'une case [x,y]
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
    
## Fonctions pour la résolution

def recherche_sequentielle2 (D,o):
    for i in range (len(D)):
        if D[i]==o:
            return o
    return None

def direction_possibles(M,x,y,l):
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


def cases_intuitives (M,x,y,orientation,l): 
    """ donne une direction via les cases que préfère l'H (pas revenir sur ses pas sauf impasse) dans les cases possibles"""
    D=direction_possibles(M,x,y,l)
    direction=0
    if D!=[orientation]: #si on n'est pas dans une impasse
        preferee=orientation_preferee(orientation,M,x,y) #il n'y a pas le choix de revenir sur ses pas (car pas ds une impasse) car le choix n'est pas dans preferee
        direction=r.choice(preferee)
    else : #on est alors dans une impasse, car la seule orientation possible est celle d'où l'on vient. 
        direction=D[0] #on revient en arrière et on aura 2 possibilités de direction, elle va donc enlever celle d'où on vient, ce qui permet de sortir de l'impasse 
    return direction
    
def orientation_preferee(orientation,M,x,y):
    '''enleve le choix de l'impasse et pondere le choix de direction : d'abord devant, puis a droite et enfin à gauche)'''
    D=direction_possibles(M,x,y,l)
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
    


## fonctions des algorithmes eux meme 

def hunt_and_kill(l):
    U=[]
    M=np.ones((l,l,2))
    [x,y]=depart
    U.append([x,y])
    while chasse(U,M,l) !=[-2,-2]:
        while [x,y]!=[-1,-1]:
            M,U,x,y=tue(M,U,x,y,l)
        [x,y]=chasse(U,M,l)
    return M
    
def prims(l):
    F=[]
    U=[]
    [x,y]=depart
    M=np.ones((l,l,2))
    U.append([x,y])
    F=declare_frontiere (x,y,F,U,l)
    while F!=[]:
        [x,y]=r.choice(F) #on prend au hasard une des frontières pas dans le L (tte les frontières ont le meme "poid"/distance au L)
        F.remove ([x,y])
        F=declare_frontiere(x,y,F,U,l)
        M=detruit_mur(x,y,M,U)
        U.append([x,y])
    return M
    

  
def resolution_humaine(M,l):
    t=0 
    
    [x,y]=depart 
    sortie =[l-1,l-1]
    orientation=odepart 
    while t<tmax and [x,y]!=sortie: 
        direction = cases_intuitives(M,x,y,orientation,l)
        x,y,orientation=parcourt(x,y,direction)
        t+=2  
        
    if t>=tmax:
        return "Game over"
    else :
        return "Sortie atteinte !"
        


### STATISTIQUES
#fait 100 essais de lab pour chaque algo, les resout et compte le nombre d'echec. Le faire pr des Laby entre l=4 à l=40 . Stocke dans une matrice de taille (41-4)x2 
nbrtirage =30
taille_voulue = 60
s1=0
s2=0
o=[]
S=np.zeros((56,2)) #ligne(taille du labyrinthe crée,colonnes (0:hunt&kill, 1:prims) affiche le pourcentage de game over
for l in range (5,61):
    s1=0
    s2=0
    o.append(l)
    for i in range (nbrtirage):
        M=hunt_and_kill(l)
        if resolution_humaine(M,l)=="Game over":
            s1+=1
        N=prims(l)
        if resolution_humaine(N,l)=="Game over":
            s2+=1
    s1=s1/nbrtirage
    s2=s2/nbrtirage
    S[l-10,0]=s1
    S[l-10,1]=s2
    print i
    
a1=[]
a2=[]

for k in range(66):
    a1.append(S[k,0])#h&k
    a2.append(S[k,1])
plt.plot(a1,o,color = "red")
plt.plot(a2,o,color = "black")
plt.show()
        
    
"""S=np.zeros((46,4))  
for l in range(4,50):
    t0= time.time()  
    M=hunt_and_kill(l)
    S[l-4,0]=(time.time() - t0)
    
        
    t1= time.time()  
    N=prims(l)
    S[l-4,1]=(time.time() - t1)"""