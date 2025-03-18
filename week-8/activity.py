def numCalcula(num):
    num = str(num)

    tamanho = len(num)

    return tamanho


numero = eval(input("Entre um número: "))

print("Quantidade de dígitos do numero é: ", numCalcula(numero))
print(tamanho) # Not declared globally
