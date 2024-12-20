from libs.benchmark import Benchmark

@Benchmark("main")
def main():
    for num in range (1,101):

        string = ""

        # Si es divisible por 3, añade Fizz al string
        if num % 3 == 0:
            string += "Fizz"

        # Si es divisible por 5, añade Buzz al string
        if num % 5 == 0:
            string += "Buzz"

        # Si no es divisible por ninguno, añade el número
        if num % 3 != 0 and num % 5 != 0:
            string += str(num)

        # Imprimir resultados
        print(string)


if __name__ == "__main__":
    main()