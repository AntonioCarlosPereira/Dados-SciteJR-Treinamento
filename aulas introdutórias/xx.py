
#5-------------------------------------------

try:
    # Solicita um número inteiro ao usuário
    numero = input("Digite um número inteiro: ")
    
    # Converte a entrada para um inteiro
    numero_inteiro = int(numero)
    
    # Calcula o antecessor e o sucessor
    numero_antecessor = numero_inteiro - 1
    numero_posterior = numero_inteiro + 1
    
    # Exibe o resultado de forma clara
    print(f"O antecessor de {numero_inteiro} é {numero_antecessor}.")
    print(f"O sucessor de {numero_inteiro} é {numero_posterior}.")
    
except ValueError:
    # Captura o erro caso a entrada não seja um número inteiro
    print("Entrada inválida. Por favor, digite apenas um número inteiro.")



#6------------------------------------------------

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
# Importa a biblioteca 'math' para poder usar a função de raiz quadrada
import math

# Pede ao usuário para digitar um número
numero = input("Digite um número: ")

try:
    # Converte a entrada do usuário para um número (float, para aceitar decimais)
    numero_flutuante = float(numero)

    # Calcula o dobro, triplo e a raiz quadrada
    dobro = numero_flutuante * 2
    triplo = numero_flutuante * 3
    raiz_quadrada = math.sqrt(numero_flutuante)

    # Exibe os resultados
    print(f"O dobro de {numero_flutuante} é: {dobro}")
    print(f"O triplo de {numero_flutuante} é: {triplo}")
    print(f"A raiz quadrada de {numero_flutuante} é: {raiz_quadrada:.2f}") # O .2f formata o resultado com 2 casas decimais

except ValueError:
    # Mensagem de erro caso a entrada não seja um número
    print("Entrada inválida. Por favor, digite um número válido.")

#7------------------------------------------------

try:
    # Lê a primeira nota do aluno
    nota1 = float(input("Digite a primeira nota: "))

    # Lê a segunda nota do aluno
    nota2 = float(input("Digite a segunda nota: "))

    # Calcula a média das notas
    media = (nota1 + nota2) / 2

    # Exibe a média com uma formatação de 2 casas decimais
    print(f"A média do aluno é: {media:.2f}")

except ValueError:
    # Mensagem de erro caso a entrada não seja um número
    print("Entrada inválida. Por favor, digite apenas valores numéricos para as notas.")

#9------------------------------------------------

try:
    # Solicita um número inteiro ao usuário
    numero = int(input("Digite um número inteiro para ver a sua tabuada: "))
    
    # Imprime um cabeçalho para a tabuada
    print("-" * 15)  # Imprime uma linha de hífens para separar
    print(f"Tabuada de {numero}:")
    print("-" * 15)
    
    # Usa um loop 'for' para calcular e imprimir a tabuada de 1 a 10
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado:3}")# :2 e :3 formatam a saída para alinhar os números
    
    print("-" * 15)
    
except ValueError:
    # Exibe uma mensagem de erro se a entrada não for um número inteiro
    print("Entrada inválida. Por favor, digite um número inteiro.")

#13------------------------------------------------

try:
    # Solicita o salário atual do funcionário
    salario_atual = float(input("Digite o salário atual do funcionário: R$ "))

    # Define a porcentagem de aumento
    aumento = 15

    # Calcula o valor do aumento
    valor_do_aumento = salario_atual * (aumento / 100)

    # Calcula o novo salário
    novo_salario = salario_atual + valor_do_aumento

    # Exibe os resultados formatados com 2 casas decimais
    print("-" * 30)
    print(f"Salário anterior: R$ {salario_atual:.2f}")
    print(f"Valor do aumento ({aumento}%): R$ {valor_do_aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")
    print("-" * 30)

except ValueError:
    # Mensagem de erro caso a entrada não seja um número
    print("Entrada inválida. Por favor, digite um valor numérico para o salário.")

#14------------------------------------------------

try:
    # Solicita a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte Celsius para Fahrenheit usando a fórmula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32

    # Exibe o resultado com uma formatação de duas casas decimais
    print(f"A temperatura de {celsius:.1f}°C corresponde a {fahrenheit:.1f}°F.")

except ValueError:
    # Mensagem de erro caso a entrada não seja um número
    print("Entrada inválida. Por favor, digite um valor numérico para a temperatura.")

#19------------------------------------------------

import random

# Pede para o usuário digitar o nome dos quatro alunos
aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

# Cria uma lista com os nomes dos alunos
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteia um nome da lista
aluno_sorteado = random.choice(lista_alunos)

# Exibe o nome do aluno sorteado
print(f"O aluno sorteado para apagar o quadro foi: {aluno_sorteado}")


#20------------------------------------------------

import random

# Pede para o usuário digitar o nome dos quatro alunos
aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

# Cria uma lista com os nomes dos alunos
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralha a ordem da lista
random.shuffle(lista_alunos)

# Exibe a ordem sorteada
print("A ordem de apresentação dos trabalhos será:")
for posicao, aluno in enumerate(lista_alunos, 1):
    print(f"{posicao}º - {aluno}")

#21------------------------------------------------

#Instalação: Primeiro, você precisa instalar a biblioteca. Abra o terminal ou prompt de comando e digite:
#pip install playsound

from playsound import playsound
import time

# Caminho para o seu arquivo MP3.
# Exemplo: 'musica.mp3' se estiver na mesma pasta.
# Exemplo: 'C:/Users/SeuUsuario/Musicas/musica.mp3' se for o caminho completo.
caminho_do_audio = 'musica.mp3'

print("Reproduzindo o áudio...")
playsound(caminho_do_audio)

# Nota: O programa só continuará após o áudio terminar de tocar, a menos que você
# use o parâmetro 'False' na função.
# Exemplo: playsound(caminho_do_audio, False)

print("Áudio finalizado.")

