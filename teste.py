def notas(*num, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos
    
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    D = {}
    D['total'] = len(num)
    D['maior'] = max(num)
    D['menor'] = min(num)
    D['média'] = sum(num)/len(num)
    if sit:
        if D['média'] >= 7:
            D['situação'] = 'BOA'
        elif D['média'] >= 5:
            D['situação'] = 'RAZOÁVEL'
        else:
            D['situação'] = 'RUIM'
    return D

#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, 7, 10, 9.5, 8.3, 8.3, sit=True)
print(resp)