# función para ordenar
def quicksort_productos(lista,clave='precio', descendente=True) -> list[dict] :
    ''' los valores de los parametros seran mutables segun la decision de una en trada a futuro'''
    if len(lista) <= 1 :return lista
    pivote = lista[0]
    izquierda  = []
    derecha = []
    
    for x in lista[1:]:
      
      p = pivote[clave]
      valor = x[clave]
      
      if descendente:
          if valor >= p:
              izquierda.append(x)
          else:
              derecha.append(x)
      else:
          if valor <= p:
              izquierda.append(x)
          else:
              derecha.append(x)
    return quicksort_productos(izquierda,clave,descendente) + [pivote] + quicksort_productos(derecha,clave,descendente)

# función para buscar 
def buscar(lista,clave="precio",orden=True) -> list[dict]:
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