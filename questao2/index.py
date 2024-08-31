def contar_a(texto):
    return texto.lower().count('a')

texto = input("Digite um texto: ")
quantidade = contar_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes.")