nome_completo = input("Digite seu nome completo: ")

# 1. Nome com todas as letras maiúsculas e minúsculas
nome_maiusculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()

print(f"Seu nome em maiúsculas é: {nome_maiusculo}")
print(f"Seu nome em minúsculas é: {nome_minusculo}")

# 2. Quantas letras ao todo (sem considerar espaços)
nome_sem_espacos = nome_completo.replace(" ", "")
total_letras = len(nome_sem_espacos)
# Ou, de forma mais compacta:
# total_letras = len(nome_completo.replace(" ", ""))

print(f"Seu nome tem ao todo {total_letras} letras.")

# 3. Quantas letras tem o primeiro nome
primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)

print(f"Seu primeiro nome tem {letras_primeiro_nome} letras.")


#-------------------------------------------------

nome_completo = input("Digite seu nome completo: ")

# Divide o nome completo em uma lista de strings, usando os espaços como separadores
partes_do_nome = nome_completo.split()

# Pega o primeiro nome (índice 0 da lista)
primeiro_nome = partes_do_nome[0]

# Pega o último nome (último item da lista)
# O índice -1 sempre se refere ao último item de uma lista em Python
ultimo_nome = partes_do_nome[-1]

# Exibe os resultados
print(f"Muito prazer em te conhecer, {nome_completo}!")
print(f"Seu primeiro nome é: {primeiro_nome}")
print(f"Seu último nome é: {ultimo_nome}")

#28-----------------------------------------------------

import random

# O computador "pensa" em um número aleatório de 0 a 5
numero_secreto = random.randint(0, 5)

# Pede ao usuário para adivinhar o número
try:
    chute_do_usuario = int(input("Tente adivinhar o número que eu pensei, de 0 a 5: "))

    # Compara o chute do usuário com o número secreto
    if chute_do_usuario == numero_secreto:
        print(f"Parabéns! Você acertou! O número era {numero_secreto}.")
    else:
        print(f"Que pena! Você errou. O número que eu pensei era {numero_secreto}.")

except ValueError:
    print("Isso não é um número. Por favor, digite um número inteiro de 0 a 5.")

#29-----------------------------------------------------

try:
    # Lê a velocidade do carro em km/h
    velocidade = float(input("Digite a velocidade do carro em Km/h: "))
    
    # Define o limite de velocidade
    limite = 80
    
    # Verifica se a velocidade ultrapassa o limite
    if velocidade > limite:
        # Calcula o valor da multa
        km_acima_do_limite = velocidade - limite
        valor_multa = km_acima_do_limite * 7.00
        
        # Exibe a mensagem de multa e o valor
        print(f"ATENÇÃO! Você foi multado por exceder o limite de {limite}Km/h.")
        print(f"O valor da multa é de R${valor_multa:.2f}.")
    else:
        # Exibe uma mensagem de parabéns se a velocidade estiver dentro do limite
        print("Você está dentro do limite de velocidade. Dirija com segurança!")
        
except ValueError:
    # Mensagem de erro para entradas inválidas
    print("Entrada inválida. Por favor, digite um valor numérico para a velocidade.")

#32-----------------------------------------------------

import calendar

try:
    # Solicita o ano ao usuário
    ano = int(input("Digite um ano para saber se ele é bissexto: "))

    # Usa a função is_leap() do módulo calendar para verificar
    if calendar.isleap(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

#34-----------------------------------------------------

try:
    # Pergunta o salário do funcionário
    salario = float(input("Digite o salário do funcionário: R$ "))

    # Define o limite para os diferentes aumentos
    limite = 1250.00

    if salario > limite:
        # Aumento de 10% para salários superiores a R$ 1250,00
        aumento = salario * 0.10
        novo_salario = salario + aumento
        porcentagem = 10
    else:
        # Aumento de 15% para salários inferiores ou iguais a R$ 1250,00
        aumento = salario * 0.15
        novo_salario = salario + aumento
        porcentagem = 15

    # Exibe o resultado formatado
    print("-" * 30)
    print(f"Salário anterior: R$ {salario:.2f}")
    print(f"Aumento de {porcentagem}%: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")
    print("-" * 30)

except ValueError:
    # Mensagem de erro caso a entrada não seja um número
    print("Entrada inválida. Por favor, digite um valor numérico para o salário.")

#35-----------------------------------------------------

try:
    # Lê o comprimento das três retas
    r1 = float(input("Digite o comprimento da primeira reta: "))
    r2 = float(input("Digite o comprimento da segunda reta: "))
    r3 = float(input("Digite o comprimento da terceira reta: "))

    # Verifica a regra de existência de um triângulo
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print("As três retas PODEM formar um triângulo!")
    else:
        print("As três retas NÃO PODEM formar um triângulo.")

except ValueError:
    # Mensagem de erro para entradas inválidas
    print("Entrada inválida. Por favor, digite apenas valores numéricos.")

