# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 01:26:09 2021

@author: Teddy
"""

import random

print("Pour jouer et tester votre chance, choisir un mode :")

choice = int(input("[1] Ticket à gratter\n[2] Billet de loto\n"))

number = int(input("Nombre de ticket à jouer :\n"))

argentperdu = 0
argentgagner = 0
ticketgagnant = 0
ticketperdant = 0
essais = 0

if choice == 1:
    
    for i in range(0,number):
        
        ticket = random.randint(0,100)
        
        if ticket < 19:
            
            ticketgagnant += 1
            argentgagner += 13 - 3
        
        elif ticket >= 19:
            
            ticketperdant += 1
            argentperdu += 3
            
        essais += 1
        
        
elif choice == 2:
    
    winner = random.randint(000000,999999)
    
    for i in range(0,number):
        
        ticket = random.randint(000000,999999)
        
        if ticket == winner:
            
            ticketgagnant += 1
            argentgagner += 150000 - 3
        
        else:
            
            ticketperdant += 1
            argentperdu += 3
            
        essais += 1
        
        
print("\n\nNombre Essais :",essais,"\nTicket perdant :",ticketperdant,"(",argentperdu,"€ perdu)"+"\nTicket gagnant :",ticketgagnant,"(",argentgagner,"€ gagner)")