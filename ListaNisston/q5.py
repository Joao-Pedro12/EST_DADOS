# Função que calcula a média dos números pares em uma lista
def calcular_media_pares(lista):
    # Inicializa as variáveis para o cálculo da média
    soma = 0
    contador = 0

    # Percorre os números da lista
    for numero in lista:
        # Verifica se o número é par
        if numero % 2 == 0:
            # Soma o número à variável 'soma'
            soma += numero
            # Incrementa o contador
            contador += 1

    # Verifica se existem números pares na lista
    if contador != 0:
        # Calcula a média dos números pares
        media = soma / contador
        return media
    else:
        return None

# Lê os números da lista
numeros = input("Digite uma lista de números separados por espaço: ").split()

# Converte os números para inteiros
numeros = [int(numero) for numero in numeros]

# Chama a função para calcular a média dos números pares
media_pares = calcular_media_pares(numeros)

# Verifica se a média calculada é válida
if media_pares is not None:
    print(f"A média dos números pares é: {media_pares}")
else:
    print("Não há números pares na lista.")
