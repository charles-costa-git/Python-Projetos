# Simples, Composto, Encadeado

n1 = n2 = media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado: Aprovado!\nParabéns!')
elif (media >= 5):
    print('Aluno de recuperação!')
else:
    print('Aluno reprovado...')

print(f'Sua média é {media}')
