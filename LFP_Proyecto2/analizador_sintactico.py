from Abstract.errores import *
from Instrucciones.claves import *
from Instrucciones.imprimir import *
from Instrucciones.imprimirln import *
from Instrucciones.registros import *
from Instrucciones.conteo import *
from Instrucciones.promedio import *
from Instrucciones.contarsi import *
from Instrucciones.datos import *
from Instrucciones.sumar import *
from Instrucciones.max import *
from Instrucciones.min import *
from Instrucciones.exporReporte import *
from analizador_lexico import lista_errores


def instrucciones_sintactico(lista_lexemas):
    comitas = '\''*3
    print(comitas)
    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'Claves':
            lista_elementos = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == '"':
                            continue
                        elif lex.operar(None) == ',':
                            continue
                        elif lex.operar(None) == ']':
                            return DeclaracionClaves(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
                        else:
                            lista_elementos.append(lex.lexema)
                else:
                    lista_errores.append(Errores(corchete_izq.lexema,"Sintáctico", corchete_izq.getFila(), corchete_izq.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ']':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        break
        
        elif lexema.operar(None) == 'imprimir':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Imprimir(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: #! para detectar errores sintácticos
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                break
                        else: #! para detectar errores sintácticos
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        elif lexema.operar(None) == 'imprimirln':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Imprimirln(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: #! para detectar errores sintácticos
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                break
                        else: #! para detectar errores sintácticos
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
        
        elif lexema.operar(None) == 'Registros':
            lista_elementos = []
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    lista_resgistros = []
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == '"':
                            continue
                        elif lex.operar(None) == ',':
                            continue
                        elif lex.operar(None) == '{':
                            continue
                        elif lex.operar(None) == '}':
                            lista_elementos.append(lista_resgistros)
                            lista_resgistros = []
                        elif lex.operar(None) == ']':
                            return DeclaracionRegistros(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
                        else:
                            lista_resgistros.append(lex.lexema)
                else:
                    lista_errores.append(Errores(corchete_izq.lexema,"Sintáctico", corchete_izq.getFila(), corchete_izq.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ']':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        break

        elif lexema.operar(None) == 'conteo':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == ';':
                        return Conteo(lexema, lexema.getFila(), lexema.getColumna())
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                        break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                    
        elif lexema.operar(None) == 'promedio':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Promedio(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: #! para detectar errores sintácticos
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                break
                        else: #! para detectar errores sintácticos
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
                            
        elif lexema.operar(None) == 'contarsi':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        coma = lista_lexemas.pop(0)
                        if coma.operar(None) == ',':
                            valor = lista_lexemas.pop(0)
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.operar(None) == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.operar(None) == ';':
                                    return ContarSi(texto.lexema, valor.operar(None), lexema.getFila(), lexema.getColumna())
                                else: #! para detectar errores sintácticos
                                    lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                    break
                            else: #! para detectar errores sintácticos
                                lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                                while lista_lexemas:
                                    lex = lista_lexemas.pop(0)
                                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                    if lex.operar(None) == ';':
                                        break
                        else: #! para detectar errores sintácticos
                            lista_errores.append(Errores(coma.lexema,"Sintáctico", coma.getFila(), coma.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
        
        elif lexema.operar(None) == 'datos':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                parentesis = lista_lexemas.pop(0)
                if parentesis.operar(None) == ')':
                    punto_coma = lista_lexemas.pop(0)
                    if punto_coma.operar(None) == ';':
                        return Datos(lexema, lexema.getFila(), lexema.getColumna())
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                        break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
        
        elif lexema.operar(None) == 'sumar':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Sumar(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: #! para detectar errores sintácticos
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                break
                        else: #! para detectar errores sintácticos
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
        
        elif lexema.operar(None) == 'max':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Max(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: #! para detectar errores sintácticos
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                break
                        else: #! para detectar errores sintácticos
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
        
        elif lexema.operar(None) == 'min':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Min(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: #! para detectar errores sintácticos
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                break
                        else: #! para detectar errores sintácticos
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break
        
        elif lexema.operar(None) == 'exportarReporte':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return ExporReporte(texto.lexema, lexema.getFila(), lexema.getColumna())
                            else: #! para detectar errores sintácticos
                                lista_errores.append(Errores(punto_coma.lexema,"Sintáctico", punto_coma.getFila(), punto_coma.getColumna()))
                                break
                        else: #! para detectar errores sintácticos
                            lista_errores.append(Errores(parentesis.lexema,"Sintáctico", parentesis.getFila(), parentesis.getColumna()))
                            while lista_lexemas:
                                lex = lista_lexemas.pop(0)
                                lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                                if lex.operar(None) == ';':
                                    break
                    else: #! para detectar errores sintácticos
                        lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                            if lex.operar(None) == ';':
                                break
                else: #! para detectar errores sintácticos
                    lista_errores.append(Errores(comillas.lexema,"Sintáctico", comillas.getFila(), comillas.getColumna()))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                        if lex.operar(None) == ';':
                            break
            else: #! para detectar errores sintácticos
                lista_errores.append(Errores(lexema.lexema,"Sintáctico", lexema.getFila(), lexema.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ';':
                        break