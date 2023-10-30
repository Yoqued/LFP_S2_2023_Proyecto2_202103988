from Abstract.lexema import *
from Abstract.numero import *
from Abstract.errores import *

lista_lexemas = []
lista_errores = []
n_linea = 1
n_columna = 1

def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    global lista_errores

    lexema = ''
    puntero = 0
    n_linea = 1
    n_columna = 1
    lista_lexemas.clear()
    lista_errores.clear()
    clase_comentario = 0
    conteo_comilla_simple = 0
    comilla_comentario = ''

    while cadena:
        char = cadena[puntero]
        puntero =+ 1

        if char == '"':   
                #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token
            l = Lexema('"', n_linea, n_columna, 'COMILLA')
            lista_lexemas.append(l)

            lexema, cadena = armar_lexema(cadena[puntero:])
            
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna, 'TEXTO')
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('"', n_linea, n_columna, 'COMILLA')
            lista_lexemas.append(l)

            n_columna += 1
            puntero = 0

        elif cadena.startswith("Claves"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'CLAVES')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

        elif cadena.startswith("Registros "):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1
                
                l = Lexema(lexema, n_linea, n_columna, 'REGISTROS')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

        elif cadena.startswith("imprimir"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1
                
                l = Lexema(lexema, n_linea, n_columna, 'IMPRIMIR')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("imprimirln"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'IMPRIMIRLN')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("conteo"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'CONTEO')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("promedio"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'PROMEDIO')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("contarsi"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'CONTARSI')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("datos"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'DATOS')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("sumar"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'SUMAR')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("max"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'MAX')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("min"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'MIN')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif cadena.startswith("exportarReporte"):

            lexema, cadena = armar_instrucciones(cadena)

            if lexema and cadena:
                n_columna += 1

                l = Lexema(lexema, n_linea, n_columna, 'EXPORTARREPORTE')
                lista_lexemas.append(l)

                n_columna += len(lexema) + 1
                puntero = 0

            l = Lexema('(', n_linea, n_columna, 'PARIZQ')

            lista_lexemas.append(l)
            n_columna += 1
            puntero = 0

        elif char.isdigit():

            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                #! Armamos lexema como clase
                n = Numero(token, n_linea, n_columna, 'NUMERO')
                lista_lexemas.append(n)

                n_columna += len(str(token)) + 1
                puntero = 0

        elif char == '[' or char == ']':
            # ! Armamos lexema como clase
            c = Lexema(char, n_linea, n_columna, 'CORCHETE')
            lista_lexemas.append(c)

            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == '{' or char == '}':
            # ! Armamos lexema como clase
            c = Lexema(char, n_linea, n_columna, 'LLAVE')
            lista_lexemas.append(c)

            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ';':

            c = Lexema(char, n_linea, n_columna, 'PUNTOYCOMA')
            lista_lexemas.append(c)

            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == '=':

            c = Lexema(char, n_linea, n_columna, 'IGUAL')
            lista_lexemas.append(c)

            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ',':

            c = Lexema(char, n_linea, n_columna, 'COMA')
            lista_lexemas.append(c)

            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == ')':

            c = Lexema(char, n_linea, n_columna, 'PARDER')
            lista_lexemas.append(c)

            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char == "\t":

            n_columna += 4
            cadena = cadena[4:]
            puntero = 0

        elif char == "\n":

            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1

        elif char == ' ' or char == '\r' or char == '.' or char == ':':

            n_columna += 1
            cadena = cadena[1:]
            puntero = 0

        elif char == '#':

            l = Lexema(char, n_linea, n_columna, 'COMENTARIO_UNA_LINEA')
            lista_lexemas.append(l)

            lexema, cadena = armar_lexema(cadena[puntero:])

            if lexema and cadena:

                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema.strip(), n_linea, n_columna, 'TEXTO')
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema

                n_columna += len(lexema) + 1
                puntero = 0

        elif char == '\'':
            conteo_comilla_simple += 1
            comilla_comentario += str(char)

            if conteo_comilla_simple == 3 and clase_comentario == 0:

                l = Lexema(comilla_comentario, n_linea, n_columna, 'COMENTARIO_MULTILINEA_ABRE')
                lista_lexemas.append(l)

                lexema, cadena = comentario_Mlinea(cadena[puntero+1:])
                conteo_comilla_simple = 0
                clase_comentario = 1
                comilla_comentario = ''

                if lexema and cadena:
                    n_columna += 1
                #   Armar lexema como clase
                    l = Lexema(lexema.strip('\n'), n_linea, n_columna, 'TEXTO')
                    lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema

                    n_columna += len(lexema) + 1
                    puntero = 0
            elif conteo_comilla_simple == 3 and clase_comentario == 1:

                l = Lexema(comilla_comentario, n_linea, n_columna, 'COMENTARIO_MULTILINEA_CIERRA')
                lista_lexemas.append(l)

                conteo_comilla_simple = 0
                clase_comentario = 0
                comilla_comentario = ''
                cadena = cadena[1:]
                puntero = 0
                n_columna += 1

            else:

                cadena = cadena[1:]
                puntero = 0
                n_columna += 1

        else:

            lista_errores.append(Errores(char, "Léxico",n_linea, n_columna))

            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

    for i in lista_lexemas:
        print(i.lexema, i.tipo)
    return lista_lexemas, lista_errores

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas

    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char

        if char == '"' or char == '\n' or char == '\t' or char == '(' or char == ')':

            return lexema, cadena[len(puntero):]
        
        else:

            lexema += char

    return None, None

def armar_instrucciones(cadena):
    global n_linea
    global n_columna
    global lista_lexemas

    lexema = ''
    puntero = ''

    for char in cadena:

        puntero += char

        if char == '"' or char == '\n' or char == '\t' or char == '(' or char == ')' or char == ' ' or char == '=':

            return lexema, cadena[len(puntero):]
        
        else:

            lexema += char

    return None, None

def comentario_Mlinea(cadena):
    global n_linea
    global n_columna
    global lista_lexemas

    lexema = ''
    puntero = ''

    for char in cadena:

        puntero += char
        if char == '\'':

            return lexema, cadena[len(puntero)-1:]
        
        else:

            lexema += char

    return None, None

def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False

    for char in cadena:
        puntero += char

        if char == '.':
            
            is_decimal = True

        if char == '\"' or char == ' ' or char == '\n' or char == '\t' or char == ',' or char == '}' or char == ')' or char == ']':

            if is_decimal:

                return float(numero), cadena[len(puntero)-1:]
            
            else:

                return int(numero), cadena[len(puntero)-1:]
            
        else:

            numero += char
            
    return None, None

'''cadena = Claves = ["codigo", "producto", "precio_compra",
    "precio_venta", "stock"]
    imprimir("Reporte de");
    imprimir("Abarrotería");
    imprimirln("Reporte de");
    imprimirln("Abarrotería");
    # hOoLA
instruccion(cadena)'''