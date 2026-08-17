#Sequencia de primos
import math
n= int(input())
if n < 2:
    raise ValueError("Intervalo inválido")

primos= []

#Gerar todos os numero do intervalo até n
for num in range(2,n+1):
    eh_primo= True #controle de decisão se é primo ou não

    if num > 2:
        raiz = int(math.sqrt(num)) #verifica divisores até a raiz quadrada de num
        for i in range(2, raiz+1):
            if num % i == 0:
                eh_primo= False
    
    if eh_primo== True:
        primos.append(num)
        
print(*primos)
