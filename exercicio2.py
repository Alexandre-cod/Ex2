#este documento foi reservado para os comits das funções que o Academia sugeria para a resolução do codigo.

#cria baralho
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

#extrai naipes
def extrai_naipe(carta):
    if carta[1] == '0':
        naipe = carta[2]
    
    if carta[1] != '0':
        naipe = carta[1]
    
    return (naipe)
    
    
  #extrai o valor
def extrai_valor(carta):
    if carta[1] == '0':
        valor = '10'

    else:
        valor = carta[0]

    return valor
    
    
#lista de movimentos possiveis
def lista_movimentos_possiveis(lista,i):
    lista_result = []
    if i > 0:
        if (extrai_naipe(lista[i]) == extrai_naipe(lista[i-1])) or extrai_valor(lista[i]) == extrai_valor(lista[i-1]):
            lista_result.append(1)


    if i>2:
        if (extrai_naipe(lista[i]) == extrai_naipe(lista[i-3])) or extrai_valor(lista[i]) == extrai_valor(lista[i-3]):
            lista_result.append(3)


    return lista_result


#empilha as cartas
def empilha(lista,ori,des):
    valor = lista[ori]
    lista.remove(valor)
    lista[des] = valor
    return lista

#checa se possui movimentos possiveis
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

