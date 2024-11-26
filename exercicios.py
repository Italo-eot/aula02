# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero_01 = int(input("Insira o primeiro número inteiro: "))
# numero_02 = int(input("Insira o segundo número inteiro: "))
# soma = numero_01 + numero_02
# print(f"A soma dos dois números é: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numero = int(input("Insira o primeiro número inteiro: "))
# resto = numero % 5
# print(f"O resto da divisão desse número por 5 é: {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero1 = int(input("Insira o primeiro número inteiro: "))
# numero2 = int(input("Insira o segundo número inteiro: "))
# multiplica = numero1 * numero2
# print(f"A multiplicação dos dois números é: {multiplica}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero1 = int(input("Insira o primeiro número inteiro: "))
# numero2 = int(input("Insira o segundo número inteiro: "))
# divide = numero1 // numero2
# print(f"A divisão dos dois números é: {divide}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero1 = int(input("Insira o primeiro número inteiro: "))
# potencia = numero1 ** 2
# print(f"O quadrado do número informado é: {potencia}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero_01 = float(input("Insira o primeiro número float: "))
# numero_02 = float(input("Insira o segundo número float: "))
# soma = numero_01 + numero_02
# print(f"A soma dos dois números é: {soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero_01 = float(input("Insira o primeiro número float: "))
# numero_02 = float(input("Insira o segundo número float: "))
# media = (numero_01 + numero_02) / 2
# print(f"A média dos dois números é: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# numero = float(input("Insira o primeiro número float: "))
# expoente = float(input("Insira o segundo número float: "))
# potencia = numero ** expoente
# print(f"A potência do número é: {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = float(input("Insira sua temperatura em Celsius: "))
# conversao = (celsius * 9/5) + 32
# print(f"{celsius}°C é igual a {conversao}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Insira o raio: "))
# area = 3.14159 * raio ** 2
# print(f"A área referente ao {raio} é {area}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = input("Insira aqui o seu texto: ")
# maiuscula = texto.upper()
# print(f"O texto convertido para upper é: {maiuscula}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome = input("Insira o seu nome completo: ")
# minuscula = nome.lower()
# print(f"O seu nome em lower é : {minuscula}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Insira sua frase aqui: ")
# sem_espaco = frase.strip()
# print(f"Sua frase sem espaços em branco é: {sem_espaco}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Insira sua data aqui. Com o formato de __/__/__ :")
# dia, mes, ano = data.split("/")
# print("Dia: ", dia)
# print("Mês: ", mes)
# print("Ano: ", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# texto_1 = input("Insira o primeiro texto: ")
# texto_2 = input("Insira o segundo texto: ")
# texto_concatenado = texto_1 + texto_2
# print(f"Texto concatenado: ", texto_concatenado)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# exp1 = True
# exp2 = False
# verifica = exp1 and exp2
# print("Resultado lógico AND: ", verifica)

# # 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# resultado_or = exp1 or exp2
# print("Resultado or é: ", resultado_or)

# # 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# resultado_invertido = not exp1
# print("Resultado NOT é: ", resultado_invertido)

# # 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# resultado_comparado = exp1 == exp2
# print("Resultado == é: ", resultado_comparado)

# # 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# resultado_diferentes = exp1 != exp2
# print("Resultado != é: ", resultado_diferentes)

# #### try-except e if

# 21: Conversor de Temperatura

# try:
#     celsius = float(input("Insira sua temperatura em Celsius: "))
#     conversao = (celsius * 9/5) + 32
#     print(f"{celsius}°C é igual a {conversao}°F")
# except ValueError as e:
#     print("O tipo de temperatura inserido não atende ao solicitado")
    

# 22: Verificador de Palíndromo

# palindromo = input("Insira aqui sua mensagem: ")

# if isinstance (palindromo, str):
#     formate = palindromo.replace(" ","").lower()
#     if formate == formate[::-1]:
#         print("É um palindromo")
#     else:
#         print("Não é um palindromo")
# else:
#     print("Entrada inválida. Por favor inserir novamente!")

# 23: Calculadora Simples

# try:

#     numero_1 = float(input("Insira o primeiro número: "))
#     numero_2 = float(input("Insira o segundo número: "))
#     operador = input("Digite o operador (+, -, *, /): ")

#     if operador == "-":
#         resultado = numero_1 - numero_2
#     elif operador == "+":
#         resultado = numero_1 + numero_2
#     elif operador == "*":
#         resultado = numero_1 * numero_2
#     elif operador == "/" and numero_2 != 0:
#         resultado = numero_1 / numero_2
#     else:
#         print("Operador inválido. Tente novamente.")

#     print(f"Resultado: {resultado}")

# except ValueError:
#     print("Erro: Entrada inválida. Certifique de inserir números.")

# 24: Classificador de Números

# try:

#     numero = int(input("Insira o número desejado: "))

#     if numero > 0:
#         print("Número positivo!")
#     elif numero < 0:
#         print("Número negativo!")
#     else:
#         print("Número Zero!")
#     if numero % 2 == 0:
#         print("Número par!")
#     else:
#         print("Número ímpar!")
# except ValueError:
#     print("Insira, por gentileza, um número inteiro.")

# 25: Conversão de Tipo com Validação

# digita = input("Digite uma lista de números separados por vírgula: ")
# separa = digita.split(",")
# lista = []

# try:
#     for num in separa:
#         lista.append(int(num.strip()))
#     print(f"Nossa lista de números é: {lista}")
# except ValueError:
#     print("Erro: Certifique-se de inserir números.")