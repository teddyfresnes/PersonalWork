def algoluhn(lenombrequoi): # Version rapide
    numberscounter = 1
    sommedesnombres = 0
    listedenombres = []
    lenombrequoireversed = int(str(lenombrequoi)[::-1]) # Inversion de la chaine
    for i in str(lenombrequoireversed):
        if numberscounter % 2 == 0:
            i = int(i) * 2
            if i > 9:
                i = sum(map(int,str(i))) # Calcul de la somme des 2 chiffres de i
        listedenombres.append(i)
        numberscounter += 1
    listedenombres.reverse()
    for i in listedenombres:
        sommedesnombres += int(i)
    if sommedesnombres % 10 == 0:
        print("Cette série de nombre est validé par la formule de Luhn.")
    else:
        print("Cette série de nombre n'est pas validé par la formule de Luhn.")

def algoluhnprint(lenombrequoi): # Version détaillé avec print
    numberscounter = 1
    sommedesnombres = 0
    listedenombres = []
    lenombrequoireversed = int(str(lenombrequoi)[::-1])
    print("Vous avez rentré le nombre :",lenombrequoi,"\nInversion des nombres :",lenombrequoireversed,"\nDétails :\n---------------------")
    for i in str(lenombrequoireversed):
        if numberscounter % 2 == 0:
            print("Nombre (",numberscounter,")",i," ->   ",int(i),"*",2,"=",int(i)*2)
            i = int(i) * 2
            if i > 9:
                print("Nombre(",numberscounter,")",i,"->    supérieur à 9 donc somme des 2 chiffres égale à",sum(map(int,str(i))))
                i = sum(map(int,str(i)))
        print("Nombre(",numberscounter,")",i)
        listedenombres.append(i)
        numberscounter += 1
    print("Nombres obtenus :",listedenombres)
    listedenombres.reverse()
    print("Nombres dans l'ordre :",listedenombres)
    for i in listedenombres:
        sommedesnombres += int(i)
    print("Somme égale à :",sommedesnombres,"\n---------------------")
    if sommedesnombres % 10 == 0:
        print("Cette série de nombre est validé par la formule de Luhn.")
    else:
        print("Cette série de nombre n'est pas validé par la formule de Luhn.")
