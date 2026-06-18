def soma(a, b):
    return a + b


def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 -> Somar dois números")
        print("2 -> Calcular a média de uma lista de valores")
        print("3 -> Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = soma(num1, num2)
                print(f"Resultado da soma: {resultado}")
            except ValueError:
                print("Erro: Por favor, digite apenas números válidos.")

        elif opcao == "2":
            try:
                valores = input(
                    "Digite os números separados por espaço (ex: 10 20 30): "
                )
                # Converte a string digitada em uma lista de números float
                lista_numeros = [float(x) for x in valores.split()]

                if not lista_numeros:
                    print("Erro: Nenhum número foi digitado.")
                    continue

                resultado = media(lista_numeros)
                print(f"Média dos valores: {resultado:.2f}")
            except ValueError:
                print("Erro: Certifique-se de digitar apenas números válidos.")

        elif opcao == "3":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    menu()