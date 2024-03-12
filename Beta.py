print ('Seja bem vindo(a) a fase beta da cálculadora de materiais de piscina ')

CumprimentoEmmetros = int(input('Digite o cumprimento da sua piscina em METROS '))
larguraEmMetros = int(input('Agora digite a largura em METROS '))
ProfundidadeEmMetros = int(input('Agora digite a profundidade em METROS '))
volumeEmlitros = CumprimentoEmmetros * larguraEmMetros * ProfundidadeEmMetros#calcula tamanho da piscina em litros
print(f'sua piscina possui {volumeEmlitros} mil litros')


introdução = input('Selecione qual o tipo de material deseja calcular: cloro, barrilha ou sulfato de aluminio')


if introdução == 'cloro':
    ResultadoCloro = volumeEmlitros / 1.000 * 4 #cálculo para a quantidade de cloro em gramas
    print(f'Você precisa de {ResultadoCloro} gramas, em sua piscina'.format())
    ResultadoCloroArredondado = round(ResultadoCloro, 10)
    print(f'Sendo mais preciso, o resultado é : {ResultadoCloroArredondado}')
        
elif introdução == 'barrilha':
    Resultadobarrilha = volumeEmlitros / 1.000 * 16#cálculo para a quantidade de barrilha em gramas
    print(f'Você precisa de {Resultadobarrilha} gramas, em sua piscina'.format())
elif introdução == 'sulfato de aluminio':
    Resultadosulfato = volumeEmlitros / 1.000 * 40#cálculo para a qyuan
    print(f'Você precisa de {Resultadosulfato} gramas em sua piscina'.format())
else:
        print('Selecione uma opção válida ')

