salario = float (input('Digite o salario'))
casaValor = float (input('Digite o valor da casa'))
anofin = float(input('Digite anos de financiamento'))
prestacao = casaValor/(anofin *  12)
print('--==--'*35)
print('prestacao será de R${}'.format(prestacao))
