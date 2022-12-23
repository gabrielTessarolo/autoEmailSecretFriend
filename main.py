import pyautogui as pag
import random

#This code is an auto-emailing for secret friend game. It works using the PyAutoGUI library, and the screen resolution is 1920*1080px.

dic1 = {}

numPlayers = int(input('\033[1;97mSECRET FRIEND | \033[1;31mHow many friends will play? '))

for i in range(0, numPlayers):
    dic1[input(f'\033[1;92mFriend {i+1} \033[mEmail: ')] = input(f'\033[1;92mFriend {i+1} \033[mName: ')
    print('\033[1;97m'+('-'*20));

mainEmail = input('\033[1;97mSECRET FRIEND | \033[1;31mWhat email will send the sorted names? ') #Here, paste the link of the main email's mail box.

pag.sleep(1)

pag.click(x=954, y=1060)

def sendEmail(email, name):
    pag.sleep(1)
    pag.hotkey('ctrl','t')
    pag.write(mainEmail)
    pag.press('enter')
    pag.sleep(3)
    pag.click(x=117, y=204)
    pag.sleep(2)
    pag.write(email, interval=0.1)
    pag.click(x=1130, y=501)
    pag.write('Secreto Amigo')
    pag.sleep(1)
    pag.click(x=1191, y=551)
    pag.write(f'Seu amigo secreto: {name}')
    pag.sleep(1)
    pag.click(x=1161, y=999)
    pag.sleep(2)

emails = [i for i in dic1.keys()]
names = [i for i in dic1.values()]

for i in range(0, len(emails)):
    actualEmail = random.choice(emails) #sort an email
    newList = [x for x in names if dic1[actualEmail] != x] #create a list with containing other people
    actualName = random.choice(newList) #sort a name in this list

    sendEmail(actualEmail, actualName) #send the email to the sorted person

    emails.remove(actualEmail) #remove the sorted email from the emails list
    names.remove(actualName) #remove the sorted name from the names list

    #this way, nobody is gonna draw itself, and two or more people won't draw the same person.

pag.sleep(5)
pag.hotkey('alt','f4') #close the email box, so you won't see what's have been sorted!




