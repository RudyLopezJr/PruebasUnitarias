#Suma de dos números
def sum(a, b):
    for n in (a, b):
        #en dado caso que no reciba un entero devuelve error
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a + b

#Función para obtener lista de números primos
def get_prime_numbers(max_number):
    numbers = [True, True] + [True] * (max_number-1)
    last_prime_number = 2
    i = last_prime_number
    
    while last_prime_number**2 <= max_number:
        i += last_prime_number
        while i <= max_number:
            numbers[i] = False
            i += last_prime_number
        j = last_prime_number + 1
        while j < max_number:
            if numbers[j]:
                last_prime_number = j
                break
            j += 1
        i = last_prime_number
    
    return [i + 2 for i, not_crossed in enumerate(numbers[2:]) if not_crossed]

#Buscamos si un número es primo
def is_prime(n):
    return n in get_prime_numbers(n)