from flask import Flask, request, render_template

app = Flask(__name__)


# FUNCIONES DE UTILIDAD

# Función para limitar un número a cierto rango con mínimo y máximo.
def clamp(value, lower, upper):
    return max(lower, min(value, upper))
#

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = clamp(int(request.form['nota1']), 10, 70)
        nota2 = clamp(int(request.form['nota2']), 10, 70)
        nota3 = clamp(int(request.form['nota3']), 10, 70)
        asistencia = clamp(int(request.form['asistencia']), 0, 100)
        promedio = round((nota1 + nota2 + nota3)/3, 1)
        resultado = None
        if promedio >= 40 and asistencia >= 80:
            resultado = 'APROBADO'
        else:
            resultado = 'REPROBADO'
        return render_template('ejercicio1.html', promedio=promedio,
                               resultado=resultado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()
