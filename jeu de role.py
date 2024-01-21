from random import randint

#ici, on viens nomer nos variables de départ
pv_joueur=50
pv_enemi=50
nb_potions=3
choix_de_coup=""
attaque_joueur=""
attaque_enemi=""
choix_possible=[1,2]
regen=""


print("vous tombez sur un monstre mechant!")

while True:
    #on laisse le joueur faire son action
    choix_de_coup=int(input("choissez '1' pour attaqué et '2' pour prendre une potion de régénration "))
    while choix_de_coup not in choix_possible:
        choix_de_coup=int(input("vous avez du vous tromper, veuillez réssayé "))
    if choix_de_coup==1:
        attaque_joueur=randint(5,10)
        pv_enemi-=attaque_joueur
        print("votre attaque a fait",attaque_joueur,"degats! il reste",pv_enemi,"points de vie au monstre")
    elif choix_de_coup==2 and nb_potions>0:
        regen=randint(15,50)
        pv_joueur+=regen
        nb_potions-=1
        print("la potion vous a donner",regen,"points de vie! il vous reste",nb_potions,"vous avez maintenant",pv_joueur,"points de vie")
    elif nb_potions==0:
        print("vous n'avez plus de potions! vous avez perdu un tour")
    
    #au tour de l'advairsaire
    attaque_enemi=randint(5,15)
    pv_joueur-=attaque_enemi
    print("le monstre vous a fait",attaque_enemi,"degats! il vous reste",pv_joueur,"points de vie")
    
    #on viens ici, crée un moyen de sortir de la boucle
    if pv_enemi<=0 or pv_joueur<=0:
        break

if pv_joueur>pv_enemi:
    print("bravo, vous avez gagner, il vous restait",pv_joueur,"points de vie")
else:
    print("dommage,vous avez perdu, il restait",pv_enemi,"points de vie au monstre")

print("jeu terminer")