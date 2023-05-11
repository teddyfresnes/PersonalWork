example = "dzedz%53%40de"
def unescape(text):
    liste = []
    nohex = ""
    compteur = 0
    indextrouves = []
    for index, caractere in enumerate(text): 
        if caractere == "%":
            indextrouves.append(index)
    for i in text:
        if compteur <= 0:
            if text.find(i) in indextrouves:
                nohex += i
            else:
                liste.append(nohex)
                liste.append(text[i:i+3])
                compteur = 3
        compteur -= 1
    print(liste)
    print(nohex)
    print(compteur)
unescape(example)

