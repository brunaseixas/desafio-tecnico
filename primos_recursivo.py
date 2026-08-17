#recursiva num primo
import math
def eh_primo(num, divisor=2):
    if num < 2: #caso base q se for menor que 2 não é considerado primo
        return False
    if divisor > math.isqrt(num): #se passou da raiz quadrada sem achar divisor, é primo
        return True
    
    #se achou algum divisor não é primo
    if num % divisor == 0:
        return False
    
    #chamar recursivamente pro próximo divisor
    return eh_primo(num, divisor + 1)

def primos_ate(n, num=2):
    if num > n: #caso base: passou do limite, encerra a recursão
        return []
   
    if eh_primo(num):
        return [num] + primos_ate(n, num + 1)
    #se não é primo, continua
    return primos_ate(n, num + 1)


def p(n): #validaçao
    if n < 2:
        raise ValueError("intervalo inválido")
    return primos_ate(n)


n = int(input())
print(*p(n))