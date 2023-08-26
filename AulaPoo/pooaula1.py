import time

def soma1(n):
    soma = 0
    n = 10
    for i in range(n + 1):
        soma = soma + i
    return(soma)
print(soma1(10))


def soma2(n):
    return (n*(n+1)) /2
print(soma2(10))

#CALCULANDO O TEMPO DE EXECUÇÃO
inicio=time.time()
resultado = soma1(100000)
termino = time.time()
resultado_time = termino - inicio
print(f'O resultado foi de..:{resultado}')
print(f'Tempo de início...:{inicio:.5f}segundos')
print(f'Tempo de termino...:{termino:.5f}segundos')
print(f'Tempo de execução...:{resultado_time:.10f}segundos')