def converte(numeroEmRomano):
    # Tabela de conversão de números romanos
    tabela = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Verificar se o número romano é válido
    if not numeroEmRomano or any(c not in tabela for c in numeroEmRomano):
        raise ValueError(f"Entrada inválida: {numeroEmRomano}")

    acumulador = 0
    ultimovizinhodireita = 0
    repeticao = 1
    for i in reversed(range(len(numeroEmRomano))):
        atual = tabela[numeroEmRomano[i]]

        # Verificar repetições consecutivas
        if i > 0 and numeroEmRomano[i] == numeroEmRomano[i - 1]:
            repeticao += 1
            if repeticao > 3:
                raise ValueError(f"Entrada inválida: {numeroEmRomano}")
        else:
            repeticao = 1

        # Adicionar ou subtrair conforme a posição
        if atual < ultimovizinhodireita:
            acumulador -= atual
        else:
            acumulador += atual

        ultimovizinhodireita = atual

    return acumulador
