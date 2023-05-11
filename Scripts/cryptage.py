cryptnumber = 1
def cryptage(y=""):
    return chr(ord(y)+1*cryptnumber)
def crypt(x):
    global cryptnumber
    nombre = len(x)
    result = ""
    for i in x:
        caractere = i
        caractere = str(caractere)
        result = result + cryptage(caractere)
        print(caractere)
        cryptnumber += 1
    print(result)
    return result
def prog():
    sentence = str(input("\nEntrez la phrase à chiffrer :\n"))
    crypt(sentence)
a = True
while a:
    prog()
        

    
