from numeroromano import converte

def main():
    # Lista de exemplos para conversão
    numeros_romanos = ["I", "V", "II", "XXII", "IX", "XXIV", "MCMXCIV", "MMXXIV"]

    print("Conversão de números romanos para inteiros:")
    for numero in numeros_romanos:
        try:
            resultado = converte(numero)
            print(f"{numero} -> {resultado}")
        except ValueError as e:
            print(f"{numero} -> Erro: {e}")

if __name__ == "__main__":
    main()
