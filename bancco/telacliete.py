import getpass
import csv
from conta import Conta

with open('contas.csv', newline='', encoding='utf-8', errors='ignore') as lerContas:
    leitor = csv.reader(lerContas, delimiter =",")
    for linha in leitor:
        conta = Conta (linha[0],linha[1],linha[2],linha[3],linha[4])
        conta.append(conta)


    agencia = int(input("Digite a agência: "))
    numero_conta = int(input("Digite sua conta corrente: "))
    senha = getpass.getpass("Digite a senha: ")
    
    