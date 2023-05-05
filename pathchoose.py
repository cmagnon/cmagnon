import random
import time

print("Olá, aventureiro! Tudo bem? sou o ROBO FC47")
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
print("Pensando....")
time.sleep(2)
print("Vou repetir!")
time.sleep(2)
print("O seu nome é ", nome, ". E você tem ", idade, "anos!")
print(nome, "Você está em uma floresta. Para a direita, voce ve um caminho que leva a uma casa. Para a esquerda você ve um caminho que leva para a praia. Para cima, vc pode entrar em um foguuete. Para onde vc vai?")
caminho = ''
while caminho !='1' and caminho !='2' and caminho !='3':
    caminho=input("para onde voce quer ir? ([1] direita, [2] esquerda? ou [3] foguete)")
if caminho == '1':
    print("Voce entrou na casa e dormiu!!")
if caminho == '2':
    print("Voce chegou na praia, achou um barquinho. Entrou nele e dormiu!")
if caminho == '3':
    print("Você entrou no foguete. O foguete decolou. Foi pra Lua e chegando lá você não resistiu e dormiu!!")
    
