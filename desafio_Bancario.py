class Cliente:
  def __init__(self, nome, cpf):
    self.nome = nome
    self.cpf = cpf

class Conta:
  def __init__(self, cliente, saldo=0):
    self.cliente = cliente
    self.saldo = saldo
    
    def cadastrar_cliente(nome, cpf):
      return Cliente(nome, cpf)

def cadastrar_conta(cliente):
  return Conta(cliente)

def depositar(conta, valor):
  conta.saldo += valor
  return conta.saldo

def sacar(conta, valor):
  if conta.saldo < valor:
    return "Saldo insuficiente"
  else:
    conta.saldo -= valor
    return conta.saldo

def extrato(conta):
  return f"Cliente: {conta.cliente.nome}, Saldo: {conta.saldo}"

# Cadastrar cliente
cliente1 = cadastrar_cliente("João", "123456789")

# Cadastrar a conta do cliente
conta1 = cadastrar_conta(cliente1)

# Realizando operações
depositar(conta1, 1000)
print(extrato(conta1)) # Saída: "Cliente: João, Saldo: 1000"

sacar(conta1, 500)
print(extrato(conta1)) # Saída: "Cliente: João, Saldo: 500"