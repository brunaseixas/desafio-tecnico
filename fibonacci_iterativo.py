#Fibonacci iterativo
n = int(input())
if n < 0:
        raise ValueError("Numero fora do intervalo")
# Valores dos dois termos iniciais
p = 1
r = 1
# Valor do 1º  e 2º para impressão caso não entre no for
if n == 0:
    t= 0
else:
    t = 1
# Repete n-2 vezes pois calcula do 3º em diante
for _ in range(n-2):
    t = p + r
    # Prepara a próxima iteração
    p = r
    r = t
    
print(t)