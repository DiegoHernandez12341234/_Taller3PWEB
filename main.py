from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
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
