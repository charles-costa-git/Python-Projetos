print(f'\n*** CADASTRO DE PESSOAS ***\n')
n = True
cadastrados = list()
pessoa = list()
while n == True:
    reg_nome = str(input('Digite o nome da pessoa: '))
    pessoa.append(reg_nome)
    reg_idade = int(input(f'Digite a idade do(a) {reg_nome}: '))
    pessoa.append(reg_idade)
    cadastrados.append(pessoa[:])
    validacao = str(input('\nDeseja cadastrar outra pessoa? [S/N]: ')).upper()
    print('\n')
    pessoa.clear()
    if validacao != 'S':
        break
print(f'*' * 37)
print(f'*** LISTA DE PESSOAS CADASTRADAS ***')
print(f'*' * 37)
for i in range(0, len(cadastrados)):
    if cadastrados[i][1] == 1:
        print(f'{cadastrados[i][0]:12} com {cadastrados[i][1]:3} ano  de idade')
    else:
        print(f'{cadastrados[i][0]:12} com {cadastrados[i][1]:3} anos de idade')
print(f'*' * 37)
print('\n')
