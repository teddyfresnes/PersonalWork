import random
import os
import math
print("""Une guerre atomique mondiale faisait rage. Quand arrivèrent les E-bombs, le nombre
de morts augmenta drastiquement et la destruction du monde tel que nous le connaissions
s'aggrava. Avec la radioactivité et les ondes sur la Terre, la flore commença à
décroître. Ainsi, de grands déserts se formèrent et la flore ayant résisté à une
telle catastrophe se transforma petit à petit. Les hommes, eux, se cachèrent dans
leurs abris anti-atomique ou dans des zones loin des explosions. C'est dans la colline
de Molineux-Les-Bains que fut découvert l'origine d'un fléau pis encore ! Il s'agissait
d'une personne que beaucoup de gens appréciaient énormément pour sa gentillesse et sa
générosité que quelques citoyens de cette petite communauté, formée à la suite de ces
catastrophes, découvrirent dans son taudis complètement décomposée sur le sol. Quand
ces citoyens voulurent s'approcher de lui afin de le transporter et l'incinérer, le
putride se réveilla. Il s'agissait du premier zombie ! Cette personne à l'origine
humaine semblait touchée par une forme de rage provoquant la mort d'une grande partie
de son corps. Le cannibalisme impulsif faisant partie intégrante du zombie, il mange
toutes les personnes qu'il peut. Ceci provoqua une terrible épidémie qui débuta dans
le taudis de ce premier zombie puisque une morsure suffisait à contaminer une personne.
Ce terrible virus contamina les survivants de la guerre, laissant encore moins d'êres
humains sur Terre. Ils furent obligés de se regrouper en de petites communautés et de
piller les anciens vestiges de l'humanité pour survivre. Cependant la votre a été décimée
il y a quelques temps.

Vous êtes partie dans le désert en quête de ressources et avec espérance, de trouver
d'autres survivants.

    --------------------------------------------------------------------------------------------
            COMMENT JOUER?
    - Entrez le nombre des choix proposées par le jeu pour avancer.
    - Surveillez votre jauge de soif et faim, ou vous mourrez.
    - Le but du jeu étant de survivre un maximum, fermez le programme une fois la partie terminée.
    --------------------------------------------------------------------------------------------
""")
state = True
while state:
    print("Prêt(e) à mourir?...")
    print("[1] Oui")
    reponse1 = input("[2] Non\n")
    if reponse1 == "1":
        state = False
    elif reponse1 == "2":
        print("La mort n'est pas grave dans ce jeu...")
    else:
        print("Erreur de saisie")
SCORE = 0
heal = 10
hurt = False
hurting = "Non"
sicking = "Non"
sick = False
bag = {}
nbMaxItem = 20
zombie = 0
r = 0
r2 = 0
obj1 = {nom: 'Bandage rudimentaire', fn: )}
obj2 = {nom: '', fn: )}
obj3 = {nom: '', fn: )}
obj4 = {nom: '', fn: )}
obj5 = {nom: '', fn: )}
obj6 = {nom: '', fn: )}
obj7 = {nom: '', fn: )}
obj8 = {nom: '', fn: )}
obj9 = {nom: '', fn: )}
obj10 = {nom: '', fn: )}
obj11 = {nom: '', fn: )}
obj12 = {nom: '', fn: )}
obj13 = {nom: '', fn: )}
obj14 = {nom: '', fn: )}
obj15 = {nom: '', fn: )}
obj16 = {nom: '', fn: )}
obj17 = {nom: '', fn: )}
obj18 = {nom: '', fn: )}
obj = {nom: '', fn: )}
items = [obj1,"Betapropine 5mg périmée","Médicaments sans étiquette","Paracétoïde 7g","Twinoïde 500mg","Stéroïdes Anabolisants","Boule de pâte visqueuse","Substance épaisse","Lambeau de chair","Micropur effervescent","Teddy n'Ours","Paquet de cigarettes entamé","Dés","Jeu de cartes incomplet","Débris métalliques","Souche de bois pourrie","Petit manche vibrant","Paquet de cigarettes entamé","Piqure de calmant","LSD","Cyanure","Fiole de poison","Médicament sans étiquette","Tondeuse à gazon","Tronçonneuse","Canif dérisoire","Chaise Ektörp-Gluten","Clef à Molette","Couteau à dents","Couteau suisse","Cutter","Four cancérigène","Grand Bâton Sec","Grosse chaîne rouillée","Os humain fêlé","Ouvre-boîtes","Batteur électrique","Petit chaton furieux","Taser d'auto-défense","Torche","Vodka Marinostov","Bouteille d'eau","Cola sans bulles","Café froid","Hydratone","Bouteille de Sprite","Fanta sans gaz","Bierre Heineken","7up saveur mojito","RedBull","Ailerons de poulet entamés","Biscuit fades","Chamallows calcinés","Chewing-gums séchés","Jambon-beurre moisi","Légume suspect","Melon d'intestin","Napolitains moisis","Nouilles chinoises","Nouilles chinoises épicées","Os charnu","Paquet de chips molles","Petit-beurres rances","Pims périmés","Steak appétissant","Viande Humaine","Viande indéfinissable"]
etat = {'eau': 11, 'faim': 11}


items[0][]

def verificateur(etat):
    if etat['eau'] > 10:
        etat['eau'] = 10
    if etat['faim'] > 10:
        etat['faim'] = 10
    return etat
#def compteur():
#    return eau == eau - 1 and faim == faim - 1 and SCORE == SCORE + 1
def objethasard():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    r2 = random.randint(0,65)
    print("Après de longues fouilles, vous arrivez à trouver",items[r2]," sur le sol de",lieux[r],"....")
    return r2
def statistiques():
    if hurt == 1:
        hurting = "Oui"
    else:
        hurting = "Non"
    if sick == 1:
        sicking = "Oui"
    else:
        sicking = "Non"
def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def actions():
    print("En parcourant le désert, vous découvrez parmis de nombreuses structures délabrées ; ", lieux[r])
    print(dess[r])
    sicavaousicavapa()
    if zombie == 0:
        zombie0()
    elif zombie >= 1:
        zombie1()
def sicavaousicavapa():
    print("""--------------------------------""")
    print("""  - Lieu ;""", lieux[r],"""\n  - Zombie(s) ;""", zombie,"""\n  - Santé ;""", heal,"""/ 10\n  - Faim ;""", etat['faim'],"""/ 10\n  - Soif ;""", etat['eau'],"""/ 10\n  - Bléssé(e) ;""", hurting,"""\n  - Malade ;""", sicking)
    print("""--------------------------------""")
def zombie0e():
    action = input("Actions disponibles :\n    [1] - Voir mon sac...\n    [2] - Voir mes stats...\n    [3] - Marcher dans le désert...\n")
    if action == "1":
        whatIsInMyBag()
        if len(bag.keys()) == 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Vous n'avez rien dans le sac!")
            lololol = 0
            lololol = input("   [1] Ok !\n")
            if lololol == "1":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                zombie0()
            else:
                print("Erreur de saisie.")
                WhatIsInMyBag()    
                zombie0()
        lololol = input("   [1] Ok !\n")
        if lololol == "1":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            zombie0()
    if action == "2":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        sicavaousicavapa()
        zombie0e()
    elif action == "3":
        5 # A TERMINER
    else:
        print("n")
        if action == "2":
            5
        elif action == "3":
            5
        else:
            print("Erreur de saisie.\n")
def zombie0():
    action = input("Actions disponibles :\n    [1] - Voir mon sac...\n    [2] - Fouiller les environs...\n    [3] - Voir mes stats...\n    [4] - Marcher dans le désert...\n")
    if action == "1":
        whatIsInMyBag()
        if len(bag.keys()) == 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Vous n'avez rien dans le sac!")
            lololol = 0
            lololol = input("   [1] Ok !\n")
            if lololol == "1":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                zombie0()
            else:
                print("Erreur de saisie.")
                WhatIsInMyBag()    
                zombie0()
        lololol = input("   [1] Ok !\n")
        if lololol == "1":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            zombie0()
    elif action == "2":
        r2 = objethasard()
        addToBag(items[r2])
        zombie0e()
    elif action == "3":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        sicavaousicavapa()
        zombie0()
    else:
        print("n")
        if action == "2":
            5
        elif action == "3":
            5
        else:
            print("Erreur de saisie.\n")
def zombie1():
    print("Malheureusement vous êtes bloqué(e)s par",zombie,"zombie(s).")
    action = input("Actions disponibles :\n    [1] - Voir mon sac...\n    [2] - Fouiller les environs...\n    [3] - Voir mes états...    [4] - Tenter de fuir la zone...")
    if action == "1":
        whatIsInMyBag()
    elif action == "2":
        5
    elif action == "3":
        5
    else:
        print("Erreur de saisie.\n")
def zombiezone():
    zombie = random.randint(1,100)
    if 0 <= zombie <= 70:
        return zombie == 0
    elif 70 <= zombie <= 85:
        return zombie == 1
    elif 85 <= zombie <= 90:
        return zombie == 2
    elif 90 <= zombie <= 93:
        return zombie == 3
    elif 93 <= zombie <= 95:
        return zombie == 4
    elif 95 <= zombie < 99:
        return zombie == random.randint(5,8)
    elif 99 <= zombie <= 100:
        return zombie == random.randint(9,25)
def countBag():
    j = 0
    for i in bag.values():
        j = j + i
    if j >= nbMaxItem:
        print("Votre sac est plein, impossible de mettre un objet de plus!")
    return j
def whatIsInMyBag():
    j=1
    for k,v in bag.items():
        print("[",j,"]"," ",k," (",v,")")
        j = j + 1
def addToBag(item):
    if countBag() < nbMaxItem:
        nbItem = 1
        if item in bag.keys():
            nbItem = bag[item] + 1
        bag[item] = nbItem
def removeToBag(item):
    if item in bag.keys():
        if bag[item] == 1:
            del bag[item]
            print(item," à été supprimé du sac")
        else:
            bag[item] = bag[item] - 1
            print("1 ",item," à été supprimé du sac, il en reste", bag[item])            
    else:
        print(item," n'est pas présent dans le sac")
def liste(l):
    j = 1
    for i in l:
        print("[",j,"]"," ",i)
        j = j + 1
lieu1 = "Maison d'un citoyen"
lieu2 = "Ambulance"
lieu3 = "Petite maison"
lieu4 = "Camion en panne"
lieu5 = "Parking désafecté"
lieu6 = "Ecole maternelle brûlée"
lieu7 = "Kebab << Chez Coluche >>"
lieu8 = "Atomic' Café"
lieu9 = "Bar miteux"
lieu10 = "Fast-food"
lieu11 = "Tente d'un citoyen"
lieu12 = "Immeuble délabrée"
lieu13 = "Relais auto-routier"
lieu14 = "Mini-market"
lieu15 = "Bureau de poste"
lieu16 = "Ancien commisseriat"
lieu17 = "Ancien Velib"
lieu18 = "Camion \"Mairie-mobile\""
lieu19 = "Carcasses de voitures"
lieu20 = "Caverne"
lieu21 = "Entrepôt désafecté"
lieu22 = "Epicerie Fargo"
lieu23 = "Boutique meubles Ikea"
lieu24 = "Pharmacie détruite"
lieu25 = "Stand de fête foraine"
lieu26 = "Viel hôpital de campagne"
lieu27 = "Villa de duke"
lieu28 = "Villa délabrée"
lieu29 = "Route barrée"
lieu30 = "Laboratoire cosmétique"
des1 = """« Ici vivait un Citoyen qui avait décidé de s'installer hors de la ville, pensant survivre plus longtemps,\n loin des querelles et des trahisons. La moitié de son corps est toujours dans le salon. »"""
des2 = """« Une ambulance arrêtée au milieu de la route. Elle ne comporte plus de roue, ni de moteur…\n Aucune trace de lutte, ni d'accident. Pourtant vous ne trouvez aucun corps non plus… »"""
des3 = """« Une vieille bicoque laissée à l'abandon depuis des années. Presque entièrement ensevelie sous le sable. Parfois, vous pouvez entendre des grattements inquiétants venant de ce qui doit être la cave… »"""
des4 = """« Un camion de transport du groupe soviétique Transtwinä. La cabine du conducteur est totalement encastrée dans un arbre,\n mais les entailles profondes dans le siège et le sang qui tapisse toutes les parois laissent supposer que l'accident n'est pas la cause de la mort… »"""
des5 = """« Un parking souterrain presque entièrement enseveli. Idéal pour mourir dans le noir, sans que personne ne vous entende… »"""
des6 = """« Les dessins enfantins peints sur les parois calcinées contrastent effroyablement avec les restes vaguement humains dispersés çà et là.\n Par moment, on croirait même entendre des rires lugubres sous les décombres. »"""
des7 = """« Si vous avez un petit creux, ne vous arrêtez surtout pas ici !\n Ou c'est le cuistot lui même qui viendra vous dévorer, après vous avoir découpé à la scie circulaire. »"""
des8 = """« Le rendez-vous branché du désert : venez goûter notre Nuka-Cola, spécialité de la maison, aux vrais extraits d'hormones animales. »"""
des9 = """« Ca ne ressemble plus vraiment à un bar, mais la présence d'une enseigne à demi enfouie dans le sable et d'un comptoir ne laisse pas trop planer le doute.\n La plupart des bouteilles sont cassées, mais on doit pouvoir y trouver des choses utiles… »"""
des10 = """« Une odeur atroce de cadavre faisandé émane de ce bâtiment : les réserves de viande se sont transformées en répugnants monticules de moisissure blanche qui ont commencé à “s'écouler” par les portes… »"""
des11 = """« Une bonne planque, c'est certain. Le type qui a monté ce camp savait comment mettre ses fesses à l'abri des zombies :\n camouflage naturel, bonne visibilité alentour, plusieurs issues et même un trou pour se cacher sous terre au besoin. Le nom « Shenji » est brodé dans la toile de la tente. »"""
des12 = """« Un bel immeuble de bureau où il devait faire bon venir travailler au petit matin, entouré de ses collègues anonymes pour accomplir on ne sait\n trop quel but global et avec pour seule préoccupation : sa propre survie. Vous vous dites que les choses n'ont peut-être finalement pas tant changé que ça… »"""
des13 = """« A une certaine époque, c'était sûrement le coin le plus branché de toute l'autoroute A217, avec ses bières frelatées,\n son odeur d'urine et ses rats morts sur le comptoir. Personne avant vous ne semble s'y être arrêté depuis des lustres. »"""
des14 = """« Ce petit magasin proposait toutes sortes de produits de consommation courants : nourriture, boissons, produits d'entretien… Ouvert 24h/24 et 7j/7 si on en croit ce qui est imprimé sur la vitrine. Le trou béant dans la façade lui donne raison. »"""
des15 = """« Un bâtiment qui semble avoir résisté aux affres du temps, vestige d'un antique service postal. Peu de chances que vous y\n trouviez quoi que ce soit de grand intérêt, sauf si vous aimez la lecture… »"""
des16 = """« L'imposant bâtiment s'étend sur plusieurs centaines de mètres. Il est divisé en nombreuses salles mais beaucoup se sont\n effondrées il y a bien longtemps. Si on en croit les nombreux impacts de balles et les barricades improvisées, ce commissariat a été le théâtre d'affrontements particulièrement violents. »"""
des17 = """« Une ancienne gare à vélo jonchée de pièces de ferrailles, d'outils et de débris en tous genres. »"""
des18 = """« “ Vos démarches citoyennes juste en bas de chez vous ”. Pas de doute, les zombies ont complètement adhéré au concept si on\n croit les traces de griffe un peu partout à l'intérieur du camion et les restes humains soigneusement éparpillés dans les rayonnages. »"""
des19 = """« Un modèle plutôt commun de break familial encastré dans un modèle tout aussi commun de fourgonnette… Ce petit accident\n semble avoir provoqué un carambolage de grande envergure si on en juge par l'amas de carcasses calcinées tout autour. »"""
des20 = """« Une sorte de tumulus qui devait autrefois servir de sépulture ou d'abri… Allez-savoir. L'intérieur est plongé dans le noir\n le plus total, l'air y est glacial et une odeur insupportable de charogne en émane… »"""
des21 = """« L'entrepôt de stockage d'un ancien supermarché dont la porte a résisté aux tentatives de pillages. Il doit sûrement contenir diverses babioles intéressantes… »"""
des22 = """« Une enseigne de la chaîne de magasins Brian Fargo. On y trouve généralement tout ce qu'il faut pour nettoyer et entretenir\n sa maison. Les plus démunis y trouveront de quoi manger… »"""
des23 = """« La chaîne de magasins Ikea était autrefois spécialisée dans la fabrication et la vente de meubles bons marchés. On dit que\n la piètre qualité de leurs produits serait l'une des raisons qui a poussé le monde à sa perte… »"""
des24 = """« Une petite pharmacie de quartier… perdue au milieu du désert. Les odeurs innommables font penser à tout sauf à des médicaments. »"""
des25 = """« Un endroit comme celui-ci est une aubaine de nos jours… Nul doute que vous trouverez ici de quoi vous équiper\n décemment en jouets en plastique et autres gadgets utiles. »"""
des26 = """« Les restes qui jonchent les allées de cet hôpital improvisé devaient être des patients. Difficile de savoir combien ils avaient pu être à mourir ici,\n le soir de l'attaque… Peut-être qu'en comptant le nombre de bras et en divisant par deux ? »"""
des27 = """« La maison d'un certain « Duke » si on en croit la plaque d'entrée calcinée, ancien « Héros Pour Toujours » … Plus qu'une villa, l'endroit semble être une vaste forteresse aménagée. »"""
des28 = """« Quelqu'un a vécu ici, il y a très longtemps. Peut-être même que cette personne était entourée d'une famille qui l'aimait et qu'ils\n y ont coulé des jours heureux tous ensembles ? Aujourd'hui il n'en reste rien; un peu de poussière et la désolation la plus totale. Et parfois même un cadavre qui marche vers vous en grinçant des dents. »"""
des29 = """« Ce qui s'est déroulé ici est assez incompréhensible : un énorme rocher semble s'être écrasé en plein milieu d'une route, comme tombé de nulle part… »"""
des30 = """« Ce bâtiment lugubre a servi autrefois pour divers tests de produits sur des animaux. Ça sent le camphre, l'ether et la charogne. Et ce n'est que l'entrée… »"""
lieux = [lieu1, lieu2, lieu3, lieu4, lieu5, lieu6, lieu7, lieu8, lieu9, lieu10, lieu11, lieu12, lieu13, lieu14, lieu15, lieu16, lieu17, lieu18, lieu19, lieu20, lieu21, lieu22, lieu23, lieu24, lieu25, lieu26, lieu27, lieu28, lieu29, lieu30]
dess = [des1, des2, des3, des4, des5, des6, des7, des8, des9, des10, des11, des12, des13, des14, des15, des16, des17, des18, des19, des20, des21, des22, des23, des24, des25, des26, des27, des28, des29, des30]
def deflieu():
    r = random.randint(0,29)
    return r
jspquoimettreenfait = False
while jspquoimettreenfait == False:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("""En rodant dans le désert, vous découvrirez des bâtiments enterrés. Il s'agira de les explorer. Ces bâtiments regorgent\nd'objets spéciaux, d'objets rares et parfois dangereux. Peut-être vous sauveron-ils d'une mort certaine ?""")
    reponse9999 = input("    [1] J'ai compris\n")
    if reponse9999 == "1":
        jspquoimettreenfait = True
    else:
        print("Erreur de saisie")
day = True
while day:
    etat = verificateur(etat) # Verifie si la faim et la soif sont inferieur a 10
    r = deflieu() # Lieu
    zombiezone() # Dis si y a zombies ou pas
    statistiques() # Vérifie blessure et maladie
    clear() 
    actions() # Jeu
    
