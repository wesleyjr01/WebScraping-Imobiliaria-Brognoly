
def teste(nome, sobrenome):
    print(f"O nome é: {nome}")
    print(f"O sobrenome é: {sobrenome}")


teste(nome='Jamarry', sobrenome='Viado')

dict = {'nome': 'Evaldo', 'sobrenome': 'Wolkers'}
print(*dict)
teste(**dict)
