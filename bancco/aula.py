def cria_conta(agencia, numero, titular, saldo, limite, senha):
    conta = {
        "agencia": agencia,
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite,
        "senha": senha,
    }
    return conta 

conta2 = cria_conta(123, "2000-2", "Ciclano", 200.0, 500.0, 1234)
print(f"Agência: {conta2 ['agencia']}, Conta: {conta2['numero']}, - SALDO: {conta2['saldo']}")

def extrato(conta):
    return conta['saldo']

def sacar(conta, valor):
    if conta['saldo'] > valor:
        conta ['saldo'] -