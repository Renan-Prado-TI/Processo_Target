def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

def testar_fibonacci():
    numeros_teste = [0, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89, 144, 7, 10, 20, 33]
    
    print("=== Teste da Sequencia de Fibonacci ===")
    for num in numeros_teste:
        if is_fibonacci(num):
            print(num, "PERTENCE a sequencia de Fibonacci!")
        else:
            print(num, "NAO pertence a sequencia de Fibonacci.")

if __name__ == "__main__":
    testar_fibonacci()