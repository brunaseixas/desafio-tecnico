#fibonacci recursivo
def fibonacci(n):
    #caso base
    if n== 0:
        return 0
    if  n== 1:
        return 1
    #recursao
        return fibonacci(n-1) + (n-2)
n= int(input())
print (fibonacci(n))