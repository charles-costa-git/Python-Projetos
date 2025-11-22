n1 = n2 = z = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

z = n1 + n2

print(f'A soma dos dois valores é: {z}')

z = n1 == n2

print('São iguais?\n' , z, '\n')

z = n1 > n2

print(f'{n1} é maior que {n2}?\n', z)

idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.7)
print(resultado)
