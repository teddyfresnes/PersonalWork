# -*- coding: utf-8 -*-
from skpy import Skype
import time, os
findthetwo = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre] # function to get all ":"
def connexion_sk():
    global userinfo, skp, conf, mail_sk, password_sk, staylogged_sk
    staylogged_sk = False
    print("Welcome in the Skly script : tools for skype\nFirst you need to connect to your Skype account")
    conf = True
    try:
        with open("skly save.txt", "r") as identifiantsR_sk:
            for i in range(1):
                passm = identifiantsR_sk.readline() # take first line of file
            separatornum = findthetwo(passm,':') # list of all ":" locations numbers
            separatornum = separatornum[len(separatornum)-1] # take the last number
            print("Skly detected a saved account in your repertory, connexion...")
            mail_sk = passm[:(separatornum)]
            password_sk = passm[(separatornum+1):]
            try:
                skp = Skype(mail_sk,password_sk)
                userinfo = str(skp.user)
                staylogged_sk = True
                print("Logged...")
            except:
                print("Connexion failed, please connect on your Skype account again...")
    except:
        while conf:
            try:
                mail_sk = input("Enter your skype mail/username :\n")
                conf = False
            except:        
                print("Error 1, please retry")
            if not conf:
                try:
                    password_sk = input("Enter your skype password :\n")
                except:
                    print("Error 2, please retry")
                    conf = True
                if not conf:
                    try:
                        skp = Skype(mail_sk,password_sk)
                        userinfo = str(skp.user)
                        print("Logged...")
                        conf = True
                        while conf:
                            try:
                                choice = input("Do you want to stay logged for your next openning?\n[1] Yes\n[2] No\n")
                                if choice == "1":
                                    print("Saving your account in a text file... Don't delete it.")
                                    identifiantsW_sk = open("skly save.txt", "w")
                                    identifiantsW_text = mail_sk,":",password_sk
                                    identifiantsW_text = ''.join(identifiantsW_text)
                                    identifiantsW_sk.write(identifiantsW_text)
                                    identifiantsW_sk.close()
                                    staylogged_sk = True
                                    print("Account saved !")
                                    conf = False
                                elif choice == "2":
                                    conf = False
                                else:
                                    print("Please choose a number for your answer")
                            except:
                                print("Error 3, please retry")
                    except:
                        print("Connexion failed, the account doesn't work. Check your connection or contact the skly administrator")
                        conf = True
def skly():
    global userinfo
    connexion_sk()
    separatornum = findthetwo(userinfo,'\n')
    userinfo = [userinfo[(separatornum[0]+5):(separatornum[1])],userinfo[(separatornum[1]+7):(separatornum[2])],userinfo[(separatornum[2]+11):(separatornum[3])],userinfo[(separatornum[3]+11):(separatornum[4])],userinfo[(separatornum[4]+9):(separatornum[5])],userinfo[(separatornum[5]+7):(separatornum[6])],userinfo[(separatornum[6]+9):(separatornum[7])],userinfo[(separatornum[7]+11):(separatornum[8])],userinfo[(separatornum[8]+13):(separatornum[9])],userinfo[(separatornum[9]+10):(separatornum[10])],userinfo[(separatornum[10]+12):]]
    conf = True
    try:
        while conf:
            print("\nWelcome",userinfo[1],"into Skly, what do you want ? ;D\n[1] Show profile informations\n[2] Close Skly")
            if staylogged_sk:
                print("[3] Close Skly and disconnect")
            choice = input("")
            if choice == "1":
                print("Informations on you :\nUser id :",userinfo[0],"\nUsername :",userinfo[1],"\nLocation :",userinfo[2],"\nLanguage :",userinfo[3],"\nAvatar :",userinfo[4],"\nDescription/Mood :",userinfo[5],"\nPhone :",userinfo[6],"\nBirthday :",userinfo[7],"\nContacts :",userinfo[8],"\nBlocked users :",userinfo[9],"\nFavourites users :",userinfo[10])
                time.sleep(3)
            try:
                if choice == "2":
                    print("Closing...")
                    exit()
                    break
                elif staylogged_sk:
                    if choice == "3":
                        print("Closing")
                        os.remove('skly save.txt')
                        exit()
                        break
                else:
                    print("Please choose a number for your answer")
            except:
                print("Skly is closed !")
    except:
        print("Error 4, please retry")
skly()