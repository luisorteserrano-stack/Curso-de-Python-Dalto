# Creando función que muestre la serie Fibonacci hasta un límite

def fibonacci_hasta(limite):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(limite):
        if b > limite: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a, b = b, a + b
        
resultado = fibonacci_hasta(20)
print(resultado)

# Creando función que muestre la serie Fibonacci usando lambda
primos_hasta__lambda = lambda numero: list(filter(lambda x: all(x % i != 0 for i in range(2, x)), range(3, numero + 1)))
# Fatarlía el número 2, que es el ñico número par primo
resultado_lambda = primos_hasta__lambda(15)
print(resultado_lambda)
