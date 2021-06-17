separador = 100 * "*"
print(separador)
print("Escolha sua Bebida")
print("1-Coca-Cola 5,00\t2-Pepsi 4,50\n3-Guarana 4,00\t4-Fanta Laranja 3,50"
    "\n5-Fanta Guarana 3,50\t6-Sukita 4,00\n7-Agua Cristal 2,00\t8-Limonada 5,00")
escolha = int(input("Qual será sua bebida ?"))
while(escolha < 1 or escolha > 8):
    escolha = int(input("Por favor informe dentro da opções\nQual será sua bebida ?"))
print(separador)
preco = 0.0
troco = 0.0
nome = ""
if(escolha == 1):
    preco = float(5.00)
    nome = "Coca Cola"
elif(escolha == 2):
    preco = float(4.50)
    nome = "Pepsi"
elif(escolha == 3):
    preco = float(4.00)
    nome = "Guarana"
elif(escolha == 4):
    preco = float(3.50)
    nome = "Fanta Laranja"
elif(escolha == 5):
    preco = float(3.50)
    nome = "Fanta Guarana"
elif(escolha == 6):
    preco = float(4.00)
    nome = "Sukita"
elif(escolha == 7):
    preco = float(2.00)
    nome = "Agua Cristal"
else:
    preco = float(5.00)
    nome = "Limonada"

pagamento = float(input("Você escolheu {}, {} reais\nInsira o dinheiro".format(nome, preco)))
while(pagamento < preco):
    restante = float(input("Você inseriou {} reais valor insuficiente.\nPor favor insira o restante do valor\n"
                                "Caso você não tenha o restante do valor digite 0 para cancelar a operação e devolver o valor inserido".format(pagamento)))
    if(restante == 0):
       troco = pagamento
       print("Receba {} reais da maquina".format(troco))
       break
    pagamento = pagamento + restante

if(pagamento > preco):
    troco = pagamento - preco
    print("Seu troco foi {:.2F}\nRetire sua bebida.\nObrigado".format(troco))
else:
    print("\nObrigado")
