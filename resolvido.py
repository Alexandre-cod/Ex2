def cria_baralho():
    lista = []
    espadas = '♠'
    i=2
    lista.append('A{}'.format(espadas))
    while i<=10:
        lista.append('{}''{}'.format(i,espadas))
        i+=1
    lista.append('J{}'.format(espadas))
    lista.append('Q{}'.format(espadas))
    lista.append('K{}'.format(espadas))
    copas = '♥'
    j=2
    lista.append('A{}'.format(copas))
    while j<=10:
        lista.append('{}''{}'.format(j,copas))
        j+=1
    lista.append('J{}'.format(copas))
    lista.append('Q{}'.format(copas))
    lista.append('K{}'.format(copas))
    ouros = '♦'
    k=2
    lista.append('A{}'.format(ouros))
    while k<=10:
        lista.append('{}''{}'.format(k,ouros))
        k+=1
    lista.append('J{}'.format(ouros))
    lista.append('Q{}'.format(ouros))
    lista.append('K{}'.format(ouros))
    paus = '♣'
    m=2
    lista.append('A{}'.format(paus))
    while m<=10:
        lista.append('{}''{}'.format(m,paus))
        m+=1
    lista.append('J{}'.format(paus))
    lista.append('Q{}'.format(paus))
    lista.append('K{}'.format(paus))
    return lista
#///////
def extrai_naipe(carta):
    if carta[1] == '0':
        naipe = carta[2]

    if carta[1] != '0':
        naipe = carta[1]

    return (naipe)
#///////
def extrai_valor(carta):
    if carta[1] == '0':
        valor = '10'
    else:
        valor = carta[0]
    return valor
#//////
def lista_movimentos_possiveis(lista,i):
    lista_result = []
    if i > 0:
        if (extrai_naipe(lista[i]) == extrai_naipe(lista[i-1])) or extrai_valor(lista[i]) == extrai_valor(lista[i-1]):
            lista_result.append(1)
    if i>2:
        if (extrai_naipe(lista[i]) == extrai_naipe(lista[i-3])) or extrai_valor(lista[i]) == extrai_valor(lista[i-3]):
            lista_result.append(3)
    return lista_result
#///////
def empilha(lista,ori,des):
    valor = lista[ori]
    lista.remove(valor)
    lista[des] = valor
    return lista
#//////
def possui_movimentos_possiveis(baralho):
    cartasmov = []
    j = 0
    while j<len(baralho):
        if (lista_movimentos_possiveis(baralho,j)) != []:
            cartasmov.append(baralho[j])
        j+=1
    if cartasmov == []:
        return False
    if cartasmov != []:
        return True
#//////
#//////
#//////
#//////
print ('Bem vindo(a) ao jogo Paciência Acordeão desenvolvido em Python pelo aluno Alexandre Goldfajn da sala 1A 2021.1')
input('Vamos jogar? (pressione enter)')
regras = input('Gostaria de ler as regras do jogo antes? Digite "sim". Caso contrário pressione "enter"')
if regras == 'sim':
    print ('O objetivo do jogo é colocar todas as cartas em uma mesma pilha.')
    print ('Existem apenas dois movimentos possíveis:')
    print ('          Empilhar uma carta sobre a carta imediatamente anterior.')
    print ('          Empilhar uma carta sobre a terceira carta anterior.')
    print ('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:')
    print ('          As duas cartas possuem o mesmo valor ou')
    print ('          As duas cartas possuem o mesmo naipe.')
    print ('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')
    input('Estamos prontos para começar! Digite Enter')

quer = 'sim'



while quer== 'sim':
    import random
    ordenadas = cria_baralho()
    random.shuffle(ordenadas)
    while possui_movimentos_possiveis(ordenadas):
        ponto = '.  '
        espaço = ' '
        k = 0
    #imprime o baralho
        print('O estado atual é:')
        while k<len(ordenadas):
            if k<9:
                string = '0'+str(k+1)+ponto +ordenadas[k] 
            else:
                string = str(k+1)+ponto +ordenadas[k]

            print(string)
            k+=1
        
        #pede pra escolher ate ser uma com movimentos
        escolha = int(input('Escolha uma carta (digite um numero entre 1 e {0})'.format(len(ordenadas))))
        
        indice = (escolha - 1)
        while escolha<=1 or escolha>len(ordenadas) or len(lista_movimentos_possiveis(ordenadas,indice)) == 0 or type(escolha)!=int:
            if escolha<=1 or escolha>len(ordenadas) :
                escolha = int(input('Posição inválida. Por favor digite um número entre 1 e {})'.format(len(ordenadas))))
            
            if type(escolha) !=int:
                escolha = int(input('Posição inválida. Por favor digite um número entre 1 e {})'.format(len(ordenadas))))



            elif len(lista_movimentos_possiveis(ordenadas,indice)) == 0:
                escolha = int(input('A carta {0} não pode ser movida. Por favor digite um numero entre 1 e {1})'.format((ordenadas[indice]),len(ordenadas))))
                indice = (escolha - 1)

        
        #se tiver uma opção para mover, vai automatico
        if len(lista_movimentos_possiveis(ordenadas,indice)) == 1:
            destino = indice - ((lista_movimentos_possiveis(ordenadas,indice))[0])
            ordenadas = empilha(ordenadas,indice,destino)

        # se tiver duas, pergunta e então  move se for possivel de mover
        elif len(lista_movimentos_possiveis(ordenadas,indice)) == 2:
            print ('Sobre qual carta gostaria de empilhar o {}'.format(ordenadas[indice]))
            print (('1. {}'.format(ordenadas[indice-1])))
            print (('2. {}'.format(ordenadas[indice-3])))
            resp = int(input('Escolha uma carta. digite um número entre 1 e {}'.format(len(ordenadas))))
            while resp != 1 and resp!= 2:
                resp = int(input('Escolha uma carta. digite um número entre 1 e {}'.format(len(ordenadas))))

            if resp == 1:
                destino = indice-1
                ordenadas = empilha(ordenadas,indice,destino)
            if resp ==2:
                destino = indice-3
                ordenadas = empilha(ordenadas,indice,destino)



    if len(ordenadas) == 1:
        print('Parabens, você venceu')
        quer = input('Gostaria de jogar novamente? Caso querira, digite "sim"')

    else:
        print('Não há mais movimentos possíveis, você perdeu.')
        quer = input('Gostaria de jogar novamente? Caso queira, digite "sim"')
