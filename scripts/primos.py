from libs.benchmark import Benchmark

def is_prime(n):

    # Para generalizar el codigo e invalidar 1 y 0, pero no es relevante
    #if n < 2:
    #    return False

    # Menores a 3, para verificar el 2
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    # Todos los numeros primos son de la forma 6k +/- 1
    i = 5
    while i * i <=n :
        # Todos los numeros divisibles por 6 no son primos
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@Benchmark("main")
def main():
    # El primer numero primo es 2
    for num in range (2,1001):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    main()










