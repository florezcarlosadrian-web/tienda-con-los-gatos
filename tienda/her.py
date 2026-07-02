def pedir_info_entero(texto):
    while True:
        try:
            cuanto_agregas = int(input(texto))
            if cuanto_agregas <= 0:
                print("solo numeros enteros")
                continue
            break
        except ValueError:
            print("solo numeros")
    return cuanto_agregas
    
def pedir_info_flotante(texto):
    while True:
        try:
            cuanto_agregas = float(input(texto))
            if cuanto_agregas <= 0:
                print("solo numeros enteros")
                continue
            break
        except ValueError:
            print("solo numeros")
            
    return cuanto_agregas





                