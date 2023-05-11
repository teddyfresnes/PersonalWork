import random
listeUn = ["Sa","Do","Vol","Exc","Rel","Aze","Por","Thone","Whi","Wi","Sco","Just_","IAm_","Fake","Break","Just"]
listeDeux = ["red","blue","blood","green","give","ter","tor","lax","is","are","ways"]
listeTrois = ["x","n","m"]
a = True
print("-----------------------------\nProgramme pour générer des pseudos\n-----------------------------\n")
def numberRandom():
    input("\nEntrez une touche pour continuer\n")
    number = random.randint(1911,2005)
    numberDeux = random.randint(10,99)
    number = str(number)
    numberDeux = str(numberDeux)
    a = random.randint(1,4)
    if a == 1:
        print( listeUn[random.randint(0,15)] + listeDeux[random.randint(0,10)] )
    if a == 2:
        print(listeUn[random.randint(0,15)] + listeDeux[random.randint(0,10)] + number)
    if a == 3:
        print(listeUn[random.randint(0,15)] + listeDeux[random.randint(0,10)] + numberDeux)
    if a == 4:
        print(listeUn[random.randint(0,15)] + listeDeux[random.randint(0,10)] + listeTrois[random.randint(0,2)]) 

i = True
while i:
    numberRandom()
