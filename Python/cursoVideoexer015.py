diaria = float(input("Digite o numero de dias que o carro foi locado..."))
km = float(input("Digite a kilometragem..."))
calc = (diaria * 60) + (km * 0.15)
print("*********************************************************************")
print("O valor sera de R${}".format(calc))
print("*********************************************************************")