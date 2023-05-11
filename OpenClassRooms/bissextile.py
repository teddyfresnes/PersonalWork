# -*-coding:utf-8 -*
import os
annee = input("Saisissez une année : ")
annee = int(annee)
bissextile = False 
if annee % 400 == 0:
    bissextile = True
elif annee % 100 and annee % 400 != 0:
    bissextile = True
if bissextile == True:
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
os.system("pause")
