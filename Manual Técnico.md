# Principal

El código proporcionado es una aplicación de editor de texto desarrollada con la biblioteca `tkinter` en Python. Esta aplicación permite a los usuarios abrir, editar y guardar archivos de texto. Además, tiene funcionalidades adicionales para realizar un análisis léxico y sintáctico de un lenguaje de programación específico y generar informes sobre los resultados del análisis.

## Estructura general

El código se organiza en una clase principal llamada `TextEditorApp`, que representa la aplicación del editor de texto. Aquí están las partes clave de la aplicación:

1. **Interfaz de usuario**:
   - La aplicación utiliza `tkinter` para crear la interfaz gráfica.
   - La ventana principal muestra un área de edición de texto, una barra de números de línea a la izquierda y una consola de salida en la parte inferior.

2. **Funcionalidades de archivo**:
   - Los usuarios pueden abrir archivos existentes, editar el contenido y guardar los cambios en un nuevo archivo.
   - El menú de archivo (`Archivo`) incluye opciones para abrir y guardar archivos.

3. **Funcionalidad de análisis**:
   - La aplicación tiene un botón "Analizar" en la barra de menús que realiza un análisis léxico y sintáctico del código ingresado en el área de edición de texto.
   - El análisis léxico se realiza mediante la función `instruccion` de un módulo llamado `analizador_lexico`.
   - El análisis sintáctico se realiza mediante la función `instrucciones_sintactico` de un módulo llamado `analizador_sintactico`.
   - Los resultados del análisis se muestran en la consola de salida, y se generan informes y archivos HTML con los resultados.

4. **Generación de informes**:
   - La aplicación puede generar dos tipos de informes: un informe de tokens y un informe de errores.
   - Estos informes se crean en formato HTML y se guardan como archivos separados.
   - Los informes contienen información sobre los lexemas encontrados en el código y cualquier error de sintaxis identificado.

## analizador_lexico

- `open_file()`: Abre un cuadro de diálogo para seleccionar un archivo y carga su contenido en el área de edición de texto.

- `save_file()`: Abre un cuadro de diálogo para seleccionar la ubicación y el nombre de un archivo y guarda el contenido del área de edición de texto en ese archivo.

- `update_line_numbers()`: Actualiza la barra de números de línea según el número de líneas en el área de edición de texto.

- `analyze_code()`: Realiza el análisis léxico y sintáctico del código en el área de edición de texto, muestra los resultados en la consola de salida y genera un informe HTML si es necesario.

- `reporte_lex()`: Genera un informe de tokens en formato HTML y lo guarda como un archivo separado.

- `report_errors()`: Genera un informe de errores en formato HTML y lo guarda como un archivo separado.

## Ejecución

El script principal crea una instancia de la clase `TextEditorApp` y muestra la aplicación del editor de texto en una ventana de `tkinter`.

En resumen, esta aplicación de editor de texto proporciona una forma conveniente de editar código y realizar un análisis léxico y sintáctico en un lenguaje de programación específico, generando informes útiles para los desarrolladores.

## Explicación Técnica del Código

El código proporcionado es un programa en Python que realiza el análisis léxico de una cadena de entrada. Aquí se detalla su estructura y funcionamiento:

### Estructura del Programa

1. **Importaciones**: El código importa módulos desde archivos externos que contienen definiciones de clases y funciones necesarias para su funcionamiento.

2. **Variables Globales**: Se definen variables globales para hacer un seguimiento de la posición en la cadena, listas de lexemas y errores, y otras variables relacionadas con el procesamiento.

3. **Función `instruccion`**: Esta función es el núcleo del programa y realiza el análisis léxico. Procesa la cadena de entrada, identifica lexemas y registra errores léxicos.

4. **Bucle Principal**: El programa utiliza un bucle `while` para recorrer la cadena de entrada caracter por caracter y aplicar reglas de análisis.

5. **Identificación de Lexemas**: Se identifican palabras clave como "Claves," "Registros," "imprimir," etc., clasificándolas en tipos específicos, como 'CLAVES', 'REGISTROS', 'IMPRIMIR', etc. Los números se clasifican como 'NUMERO'.

6. **Manejo de Símbolos**: Otros símbolos, como comillas, corchetes, llaves, paréntesis, punto y coma, igual, coma, se identifican y clasifican en tipos como 'COMILLA', 'CORCHETE', 'LLAVE', 'PARIZQ', 'PARDER', 'PUNTOYCOMA', 'IGUAL', 'COMA'.

7. **Manejo de Comentarios**: Se manejan comentarios de una sola línea (precedidos por '#') y comentarios multilínea (encerrados entre tres comillas simples '''...''').

8. **Manejo de Errores**: Si se encuentra un carácter no clasificable, se registra como un error léxico en `lista_errores`.

9. **Salida de Resultados**: Al final del bucle, el programa imprime los lexemas identificados con sus tipos.

### Funciones de Soporte

- `armar_lexema`, `armar_instrucciones`, `comentario_Mlinea`: Estas funciones se utilizan para construir lexemas a partir de la cadena de entrada en diferentes contextos, como texto encerrado entre comillas, instrucciones o comentarios multilínea.

- `armar_numero`: Esta función construye números a partir de la cadena de entrada, considerando si son enteros o decimales.

### Resultados

El programa genera dos listas: `lista_lexemas` con lexemas y tipos identificados, y `lista_errores` con errores léxicos encontrados.

En resumen, el código es un analizador léxico básico que procesa una cadena de entrada, dividiéndola en lexemas, identificando palabras clave, números y otros símbolos, y manejando comentarios y errores léxicos.

## Explicación Técnica del Código

El código proporcionado es un programa en Python que realiza el análisis léxico de una cadena de entrada. Aquí se detalla su estructura y funcionamiento:

### Estructura del Programa

1. **Importaciones**: El código importa módulos desde archivos externos que contienen definiciones de clases y funciones necesarias para su funcionamiento.

2. **Variables Globales**: Se definen variables globales para hacer un seguimiento de la posición en la cadena, listas de lexemas y errores, y otras variables relacionadas con el procesamiento.

3. **Función `instruccion`**: Esta función es el núcleo del programa y realiza el análisis léxico. Procesa la cadena de entrada, identifica lexemas y registra errores léxicos.

4. **Bucle Principal**: El programa utiliza un bucle `while` para recorrer la cadena de entrada caracter por caracter y aplicar reglas de análisis.

5. **Identificación de Lexemas**: Se identifican palabras clave como "Claves," "Registros," "imprimir," etc., clasificándolas en tipos específicos, como 'CLAVES', 'REGISTROS', 'IMPRIMIR', etc. Los números se clasifican como 'NUMERO'.

6. **Manejo de Símbolos**: Otros símbolos, como comillas, corchetes, llaves, paréntesis, punto y coma, igual, coma, se identifican y clasifican en tipos como 'COMILLA', 'CORCHETE', 'LLAVE', 'PARIZQ', 'PARDER', 'PUNTOYCOMA', 'IGUAL', 'COMA'.

7. **Manejo de Comentarios**: Se manejan comentarios de una sola línea (precedidos por '#') y comentarios multilínea (encerrados entre tres comillas simples '''...''').

8. **Manejo de Errores**: Si se encuentra un carácter no clasificable, se registra como un error léxico en `lista_errores`.

9. **Salida de Resultados**: Al final del bucle, el programa imprime los lexemas identificados con sus tipos.

### Funciones de Soporte

- `armar_lexema`, `armar_instrucciones`, `comentario_Mlinea`: Estas funciones se utilizan para construir lexemas a partir de la cadena de entrada en diferentes contextos, como texto encerrado entre comillas, instrucciones o comentarios multilínea.

- `armar_numero`: Esta función construye números a partir de la cadena de entrada, considerando si son enteros o decimales.

### Resultados

El programa genera dos listas: `lista_lexemas` con lexemas y tipos identificados, y `lista_errores` con errores léxicos encontrados.

En resumen, el código es un analizador léxico básico que procesa una cadena de entrada, dividiéndola en lexemas, identificando palabras clave, números y otros símbolos, y manejando comentarios y errores léxicos.

## Explicación Técnica del Código

Este código es una función de análisis sintáctico escrita en un lenguaje de programación que procesa una lista de lexemas (tokens) y realiza un análisis sintáctico para construir una estructura de datos que represente la sintaxis del código fuente. La función parece estar diseñada para analizar un lenguaje de programación específico que contiene declaraciones de claves, impresión, impresión con salto de línea y declaraciones de registros.

### Función `instrucciones_sintactico`

La función `instrucciones_sintactico` toma una lista de lexemas como entrada. Un lexema es una unidad de texto que representa un token en el código fuente, como palabras clave, operadores, números, cadenas, etc.

La función utiliza un bucle `while` para iterar a través de la lista de lexemas hasta que la lista esté vacía.

En cada iteración del bucle, se extrae el primer lexema de la lista con `lista_lexemas.pop(0)` y se almacena en la variable `lexema`.

La función verifica el tipo de lexema utilizando `lexema.operar(None)` para determinar si es una palabra clave, como "Claves," "imprimir," "imprimirln," "Registros," o "conteo."

Dependiendo del tipo de lexema, se realizan diferentes acciones:
- Para las declaraciones de "Claves," se verifica si la sintaxis es correcta y se construye una estructura `DeclaracionClaves` con la palabra reservada y una lista de elementos.
- Para las declaraciones de "Registros," se verifica si la sintaxis es correcta y se construye una estructura `DeclaracionRegistros` con la palabra reservada y una lista de elementos que representan los registros.
- Para las sentencias de "imprimir" e "imprimirln," se verifica si la sintaxis es correcta y se construye una estructura `Imprimir` o `Imprimirln` con el texto a imprimir.
- Para "conteo," se verifica si la sintaxis es correcta y se construye una estructura `Conteo`.

En caso de errores sintácticos, se agregan objetos `Errores` a una lista llamada `lista_errores` para registrar los detalles del error, como el tipo de error, la ubicación en el código fuente (línea y columna) y el lexema que causó el error.

El bucle continúa hasta que se haya analizado completamente la lista de lexemas.

La función devuelve la estructura de datos construida que representa la sintaxis del código fuente, ya sea una declaración de claves, una declaración de registros, una sentencia de impresión o una sentencia de conteo.

Es importante tener en cuenta que esta explicación se basa en la estructura general del código proporcionado y en suposiciones sobre el funcionamiento de las clases y métodos relacionados (como `DeclaracionClaves`, `DeclaracionRegistros`, `Imprimir`, `Imprimirln`, `Conteo`, `Errores`, y métodos como `operar`, que no se definen en el código proporcionado). Para comprender completamente cómo funciona este código, se necesitaría conocer la estructura y la semántica del lenguaje de programación específico que se está analizando.
