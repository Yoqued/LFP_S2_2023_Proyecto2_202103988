# Supongamos que lista_lexemas es una lista de objetos que tienen un atributo lexema y un atributo tipo

# Datos de ejemplo
class Lexema:
    def __init__(self, lexema, tipo):
        self.lexema = lexema
        self.tipo = tipo

lista_lexemas = [Lexema("lexema1", "tipo1"), Lexema("lexema2", "tipo2")]

# Generar la tabla HTML con estilos personalizados
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
</style>
</head>
<body>
    <table>
        <tr>
            <th>Lexema</th>
            <th>Tipo</th>
        </tr>
"""

for lexema in lista_lexemas:
    tabla_html += f"        <tr>\n            <td>{lexema.lexema}</td>\n            <td>{lexema.tipo}</td>\n        </tr>\n"

tabla_html += """
    </table>
</body>
</html>
"""

# Guardar la tabla en un archivo HTML
with open('reporte_lexemas.html', 'w') as file:
    file.write(tabla_html)

print("Se ha generado el archivo 'reporte_lexemas.html'")