def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa)/100
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa)/100
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    res = f'{moeda} {preço:>.2f}'.replace('.', ',')
    return res


def resumo(preço=0, aumen=10, dimin=5):
    print('\u2014' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('\u2014' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumen}% de aumento: \t{aumentar(preço, aumen, True)}')
    print(f'{dimin}% de redução: \t{diminuir(preço, dimin,True)}')
    print('\u2014' * 35)