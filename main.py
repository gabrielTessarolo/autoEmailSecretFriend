import pyautogui as pag
import random

#names = ['Gabriel', 'Guilherme', 'Átila', 'Laura', 'Amanda']
#emails = ['tessarolohelmer@gmail.com', 'lanierguilherme@gmail.com', 'atilassooll@gmail.com', 'laura.oliveira.carvalho82@gmail.com', '06amandareis@gmail.com']

dic1 = {'tessarolohelmer@gmail.com': 'Gabriel',
        'lanierguilherme@gmail.com': 'Guilherme',
        'atilassooll@gmail.com': 'Atila',
        'laura.oliveira.carvalho82@gmail.com': 'Laura',
        '06amandareis@gmail.com': 'Amanda'}

pag.sleep(1)

pag.click(x=954, y=1060)

def sendEmail(email, name):
    pag.sleep(1)
    pag.hotkey('ctrl','t')
    pag.write('https://mail.google.com/mail/u/1/?ogbl#inbox')
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

#for c, i in enumerate(names,1):
for i in range(0,5):
    actualEmail = random.choice(emails)
    newList = [x for x in names if dic1[actualEmail] != x]
    actualName = random.choice(newList)

    sendEmail(actualEmail, actualName)

    emails.remove(actualEmail)
    names.remove(actualName)

    #sortear um email
    #criar uma lista com todos os nomes diferentes do email
    #sortear algo nessa lista
    #

pag.sleep(5)
pag.hotkey('alt','f4')




