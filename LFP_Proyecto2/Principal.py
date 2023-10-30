import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import filedialog, messagebox
import subprocess
from analizador_lexico import *
from analizador_sintactico import *
from tabulate import *

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto 2 - LFP")

        # Barra de números de línea
        self.line_number_bar = tk.Text(root, width=4, padx=4, takefocus=0, border=0, background='lightgrey', state='disabled')
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        # Área de texto principal
        self.text_widget = tkst.ScrolledText(self.root, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill='both')

        self.text_widget.bind('<Key>', self.update_line_numbers)
        self.text_widget.bind('<MouseWheel>', self.update_line_numbers)

        # Consola de salida
        self.output_console = tkst.ScrolledText(self.root, wrap=tk.WORD)
        self.output_console.pack(expand=True, fill='both')
        self.output_console.config(state='disabled')

        self.current_line = 1

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)

        # Botón para analizar
        self.menu_bar.add_command(label="Analizar", command=self.analyze_code)

        # Botón para Reportes
        self.file_menu1 = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Reportes", menu=self.file_menu1)
        self.file_menu1.add_command(label="Reporte de Tokens", command=self.reporte_lex)
        self.file_menu1.add_command(label="Reporte de Errores", command=self.report_errors)

    def open_file(self):
        file_path = filedialog.askopenfilename(title='Seleccióne el "DOCUMENTO"')
        if file_path:
            with open(file_path, 'r', encoding = "UTF-8") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
            self.update_line_numbers()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(title='Nombre de el "DOCUMENTO"')
        if file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w', encoding = "UTF-8") as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")

    def update_line_numbers(self, event=None):
        line_count = self.text_widget.get('1.0', tk.END).count('\n')
        if line_count != self.current_line:
            self.line_number_bar.config(state=tk.NORMAL)
            self.line_number_bar.delete(1.0, tk.END)
            for line in range(1, line_count + 1):
                self.line_number_bar.insert(tk.END, f"{line}\n")
            self.line_number_bar.config(state=tk.DISABLED)
            self.current_line = line_count

    def analyze_code(self):
        # Obtén el código del área de texto
        code = self.text_widget.get(1.0, tk.END)
        imprimir_consola = ''
        #try:
            # Ejecuta el análisis léxico
        instrucciones_lexico, _ = instruccion(code)
        lista_instrucciones = []
        while True:
            instrucciones_lenguaje = instrucciones_sintactico(instrucciones_lexico)
            if instrucciones_lenguaje:
                lista_instrucciones.append(instrucciones_lenguaje)
            else:
                break

        # Ejecutar instrucciones
        pos = 0
        lista_claves = []
        lista_registros_y_Claves = []
        for elemento in lista_instrucciones:
            if isinstance(elemento, DeclaracionClaves):
                for i in range(len(elemento.operar(None))):
                    pos = i
                lista_claves = elemento.operar(None)

            elif isinstance(elemento, DeclaracionRegistros):
                if lista_claves:
                    for i in elemento.operar(None):
                        mi_diccionario = {}
                        for j in range(len(i)):
                            mi_diccionario[lista_claves[j]] = i[j]
                        lista_registros_y_Claves.append(mi_diccionario)
                else:
                    messagebox.showinfo("Claves", "No estan bien declaradas.")

            elif isinstance(elemento, Imprimir):
                imprimir_consola += elemento.operar(None) + ' ' 

            elif isinstance(elemento, Imprimirln):
                imprimir_consola += '\n' + elemento.operar(None)

            elif isinstance(elemento, Conteo):
                if lista_claves and lista_registros_y_Claves:
                    cantidad = len(lista_registros_y_Claves)
                    cantidad1 = len(lista_claves)
                    imprimir_consola += '\n' + str(cantidad*cantidad1)
                else:
                    messagebox.showinfo("Registros: Claves o Registros", "No estan bien declaradas.")

            elif isinstance(elemento, Promedio):
                if lista_claves and lista_registros_y_Claves:
                    sumatoria = 0
                    for i in lista_registros_y_Claves:
                        if type(i[elemento.operar(None)]) is int or type(i[elemento.operar(None)]) is float:
                            sumatoria += float(i[elemento.operar(None)])
                        else:
                            messagebox.showinfo("Promedio: String", "No se puede hacer promedio de Valores ALFANUMERICOS")
                            break
                    cantidad = len(lista_registros_y_Claves)
                    promedio = sumatoria/cantidad
                    imprimir_consola += '\n' + str(promedio)
                else:
                    messagebox.showinfo("Promedio: Claves o Registros", "No estan bien declaradas.")

            elif isinstance(elemento, ContarSi):
                if lista_claves and lista_registros_y_Claves:
                    elemen, val = elemento.operar(None)
                    if type(val) is int  or type(val) is float:
                        conta = 0
                        lista_concidencias = []
                        for i in lista_registros_y_Claves:
                            lista_concidencias.append(i[elemen])
                        for i in lista_concidencias:
                            if i == val:
                                conta += 1  
                        imprimir_consola += '\n' + str(conta)
                    else:
                        messagebox.showinfo("ContarSi: String", "No se puede hacer contarSi de Valores ALFANUMERICOS")
                else:
                    messagebox.showinfo("ContarSi: Claves o Registros", "No estan bien declaradas.")

            elif isinstance(elemento, Datos):
                if lista_claves and lista_registros_y_Claves:
                    table_format = tabulate(lista_registros_y_Claves, headers="keys", tablefmt="pretty")
                    # Imprime la tabla tabulada
                    imprimir_consola += '\n' + str(table_format)
                else:
                    messagebox.showinfo("Datos: Claves o Registros", "No estan bien declaradas.")

            elif isinstance(elemento, Sumar):
                if lista_claves and lista_registros_y_Claves:
                    suma = 0
                    for i in lista_registros_y_Claves:
                        if type(i[elemento.operar(None)]) is int or type(i[elemento.operar(None)]) is float:
                            suma += float(i[elemento.operar(None)])
                        else:
                            messagebox.showinfo("Sumar: String", "No se puede hacer la suma de Valores ALFANUMERICOS")
                            break
                    imprimir_consola += '\n' + str(suma)
                else:
                    messagebox.showinfo("Sumar: Claves o Registros", "No estan bien declaradas.")

            elif isinstance(elemento, Max):
                if lista_claves and lista_registros_y_Claves:
                    lista_maxima = []
                    for i in lista_registros_y_Claves:
                        if type(i[elemento.operar(None)]) is int or type(i[elemento.operar(None)]) is float:
                            lista_maxima.append(float(i[elemento.operar(None)]))
                        else:
                            messagebox.showinfo("Maximo: String", "No se puede hacer el maximo de Valores ALFANUMERICOS")
                            break
                    imprimir_consola += '\n' + str(max(lista_maxima))
                else:
                    messagebox.showinfo("Maximo: Claves o Registros", "No estan bien declaradas.")
            
            elif isinstance(elemento, Min):
                if lista_claves and lista_registros_y_Claves:
                    lista_minima = []
                    for i in lista_registros_y_Claves:
                        if type(i[elemento.operar(None)]) is int or type(i[elemento.operar(None)]) is float:
                            lista_minima.append(float(i[elemento.operar(None)]))
                        else:
                            messagebox.showinfo("Mínimo: String", "No se puede hacer el maximo de Valores ALFANUMERICOS")
                            break
                    imprimir_consola += '\n' + str(min(lista_minima))
                else:
                    messagebox.showinfo("Mínimo: Claves o Registros", "No estan bien declaradas.")

            elif isinstance(elemento, ExporReporte):
                if lista_claves and lista_registros_y_Claves:
                    titulo = elemento.operar(None)
                    table_format = tabulate(lista_registros_y_Claves, headers="keys", tablefmt="html")

                    # Crea el contenido HTML del informe
                    html_content = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>{titulo}</title>
                        <link rel="stylesheet" type="text/css" href="styles.css">
                    </head>
                    <body>
                        <h1>Informe de Datos</h1>
                        {table_format}
                    </body>
                    </html>
                    """

                    # Guarda el contenido HTML en un archivo
                    with open("informe.html", "w") as html_file:
                        html_file.write(html_content)
                    # Ruta al archivo HTML que deseas abrir
                else:
                    messagebox.showinfo("Claves o Registros", "No estan bien declaradas.")

        print(imprimir_consola)
        for error in lista_errores:
            print(error.operar(None))

                # Muestra el resultado en la consola de salida
        self.output_console.config(state='normal')
        self.output_console.delete(1.0, tk.END)
        self.output_console.insert(tk.END, imprimir_consola)
        self.output_console.config(state='disabled')
        messagebox.showinfo("Análisis exitoso", "El código se analizó exitosamente.")

        '''except Exception as e:
            messagebox.showerror(f"Ocurrió un error al analizar el código: {str(e)}")
            print("Ocurrió un error al analizar el código: ", e)'''


    def reporte_lex(self):
        # Obtén el código del área de texto
        code = self.text_widget.get(1.0, tk.END)
        # Ejecuta el análisis léxico
        instrucciones_lexico, _ = instruccion(code)
        tabla_html = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {
                font-family: Arial, sans-serif;
            }

            table {
                border-collapse: collapse;
                width: 100%;
                margin: 20px;
                border: 1px solid #ddd;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            th, td {
                padding: 10px;
                text-align: left;
            }

            th {
                background-color: #333;
                color: #fff;
            }

            tr:nth-child(even) {
                background-color: #f2f2f2;
            }

            tr:hover {
                background-color: #ddd;
            }

            .titulo {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }
        </style>
        </head>
        <body>
            <div class="titulo">Reporte de Lexemas</div>
            <table>
                <tr>
                    <th>Lexema</th>
                    <th>Tipo</th>
                    <th>Fila</th>
                    <th>Columna</th>
                </tr>
        """

        for lexema in instrucciones_lexico:
            tabla_html += f"        <tr>\n            <td>{lexema.lexema}</td>\n            <td>{lexema.tipo}</td>\n        <td>{lexema.fila}</td>\n            <td>{lexema.columna}</td>\n         </tr>\n"

        tabla_html += """
            </table>
        </body>
        </html>
        """

        # Guardar la tabla en un archivo HTML
        with open('reporte_lexemas.html', 'w') as file:
            file.write(tabla_html)
    
    def report_errors(self):
        code = self.text_widget.get(1.0, tk.END)
        imprimir_consola = ''

        instrucciones_lexico, _ = instruccion(code)
        lista_instrucciones = []
        while True:
            instrucciones_lenguaje = instrucciones_sintactico(instrucciones_lexico)
            if instrucciones_lenguaje:
                lista_instrucciones.append(instrucciones_lenguaje)
            else:
                break
        
        tabla_html = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {
                font-family: Arial, sans-serif;
            }

            table {
                border-collapse: collapse;
                width: 100%;
                margin: 20px;
                border: 1px solid #ddd;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            th, td {
                padding: 10px;
                text-align: left;
            }

            th {
                background-color: #333;
                color: #fff;
            }

            tr:nth-child(even) {
                background-color: #f2f2f2;
            }

            tr:hover {
                background-color: #ddd;
            }

            .titulo {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }
        </style>
        </head>
        <body>
            <div class="titulo">Reporte de Lexemas</div>
            <table>
                <tr>
                    <th>Lexema</th>
                    <th>Tipo</th>
                    <th>Fila</th>
                    <th>Columna</th>
                </tr>
        """

        for lexema in lista_errores:
            tabla_html += f"        <tr>\n            <td>{lexema.lexema}</td>\n            <td>{lexema.tipo}</td>\n        <td>{lexema.fila}</td>\n            <td>{lexema.columna}</td>\n         </tr>\n"

        tabla_html += """
            </table>
        </body>
        </html>
        """

        # Guardar la tabla en un archivo HTML
        with open('reporte_errores.html', 'w') as file:
            file.write(tabla_html)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()