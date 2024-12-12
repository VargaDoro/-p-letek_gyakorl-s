'''2.feladat'''
import random

def dobasok():
    lista=[]
    for i in range(1,8):
        dobas:int=int(random.random()*2+1)
    print(dobas, end='-')

    if dobas==1:
        dobas="fej"
    else:
        dobas="írás"
    lista.append(dobas)

def fejek_szama(dobas):
    db:int=0
    while dobas==1:
        db+=1
    return db

