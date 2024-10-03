'''
Q1
'''
# nome = input("digite seu name: ")
# print(f'bem vindo ao sistema, {nome}')

'''
Q2
'''
# nome = input("digite seu name: ")
# idade = input("qual é sua idade: ")
# print(f'{nome}, você tem {idade} anos')

'''
Q3
'''
# china = float(input('digite a população da china: '))
# brasil = float(input('digite a população do brasil: '))
# if brasil > china:
#     diferenca = brasil - china
#     print(f'Brasil tem uma população maior que a da China, com uma diferença de {diferenca} pessoas.')
# elif brasil < china:
#     diferenca = china - brasil
#     print(f'China tem uma população maior que a do Brasil, com uma diferença de {diferenca} pessoas.')
# else:
#     print(f'Os dois países possuem a mesma quantidade de pessoas, sendo de aprox. {brasil} pessoas.')

'''
Q4
'''
# numero1 = int(input("Digite um número qualquer (inteiro e positivo): "))
# calc = numero1%2
# if calc == 0:
#     print(f'{numero1} é par.')
# else:
#     print(f'{numero1} é impar.')

'''
Q5
'''
# salario = float(input("Digite um salário: "))
# desconto = float(input("Digite um desconte que será aplicado sobre o salário: "))
# calculo = salario - ((salario / 100)* desconto)

# print(f'o salário descontado é de R${calculo}')

'''
Q6
'''
# celsios = float(input(f'Digite um temperatura em grau celsios: '))
# calc = (celsios * 1.8) + 32
# print(f'{celsios}ºC equivale à {calc}ºF')

'''
Q7
'''
# num1 = float(input('Número 01: '))
# num2 = float(input('Número 02: '))
# num3 = float(input('Número 03: '))

# if num1 > num2 and num1 > num3:
#     print(f'O maior número é: {num1}')
# elif num2 > num1 and num2 > num3:
#     print(f'O maior número é: {num2}')
# else:
#     print(f'O maior número é: {num3}')

'''
Q8
'''
# idade = int(input('Quantos anos você tem? '))
# ano = int(input('Em que ano estamos? '))
# aniver = int(input('Já fez aniversário esse ano? (sim = 0, não = 1) '))
# if aniver == 0:
#     calc = ano - idade
#     print(f'Você nasceu em: {calc}')
# else:
#     calc = (ano - idade) + 1
#     print(f'Você nasceu em: {calc}')

'''
Q9
'''
# altura = float(input('informe sua altura (em metros): '))
# peso = float(input('informe o seu peso (em kilos): '))
# calc = peso /(altura**2)

# if calc <= 16.9:
#     print(f'Muito abaixo do peso, seu IMC é de {calc:.2f}')
# elif calc >= 17 and calc <= 18.9:
#     print(f'Abaixo do peso, seu IMC é de {calc:.2f}')
# elif calc >= 19 and calc <= 26.9:
#     print(f'Normal, seu IMC é de {calc:.2f}')
# elif calc >= 27 and calc <= 31.9:
#     print(f'Acima do peso, seu IMC é de {calc:.2f}')
# else:
#     print(f'Muito acima do peso, seu IMC é de {calc:.2f}')

'''
Q10
'''
# nota1 = float(input('nota 1: '))
# nota2 = float(input('nota 2: '))
# nota3 = float(input('nota 3: '))
# nota4 = float(input('nota 4: '))
# calc = (nota1 + nota2 + nota3 + nota4)/4

# if calc >= 7 and calc <= 10:
#     print(f'Aprovado, sua média foi de: {calc}')
# elif calc >= 5 and calc <= 6.9:
#     print(f'Em recuperação, sua média foi de: {calc}')
# else:
#     print(f'Reprovado, sua média foi de: {calc}')
