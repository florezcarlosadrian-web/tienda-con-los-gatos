def mergesort(lista,clave="precio",acendente=True) -> list[dict]:
    if len(lista[:]) <= 1:
        return lista[:]
    mitad = len(lista) // 2
    izquierda = mergesort(lista[:mitad],clave,acendente)
    derecha = mergesort(lista[mitad:],clave,acendente)
    return combinar(izquierda,derecha,clave,acendente)

def combinar(izq,der,clave,acendente):
    resultado = []
    i = 0 
    j = 0
    valor_izq = izq[i][clave]
    valor_der = der[j][clave]
    while i < len(izq) and j < len(der):
        if acendente:
            if valor_izq <= valor_der:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
        else:
            if valor_izq >= valor_der:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def buscar(lista,clave="precio",orden=True) -> list[dict]:
    '''
    retorna una lista con dict convalor de la clave mas alto o mas bajo
    (si enpata la clave, debuelve los mas altos)
    '''
    lista_ordenada = mergesort(lista,clave,True)
    if orden:
        resultado = [i for i in lista_ordenada if i[clave] == lista_ordenada[0] [clave] ]
    else:
        resultado = [i for i in lista_ordenada if i[clave] == lista_ordenada[-1][clave] ]
    return resultado



def buscar2(lista,clave="precio",orden=True) -> list[dict]:
    '''
    retorna una lista con dict convalor de la clave mas alto o mas bajo
    (si enpatan la clave, debuelve los mas altos)
    '''
    lista_ordenada = mergesort(lista,clave,True)
    resultado = []
    p = 0
    u = -1
    while len(lista_ordenada):
        if orden:
            resultado.append(lista_ordenada[p])
            p += 1
            if lista_ordenada[p][clave] != lista_ordenada[0][clave]:
                break
        else:
            resultado.append(lista_ordenada[u])
            u -= 1
            if lista_ordenada[u][clave] != lista_ordenada[-1][clave]:
                break
    return resultado
