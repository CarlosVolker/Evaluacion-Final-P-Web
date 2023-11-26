from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ""
    sin_descuento = ""
    descuento_precio = ""
    con_descuento = ""
    mostrar_resultado = False

    precio_tarro = 9000  # Precio por tarro de pintura

    if request.method == 'POST':
        nombre = request.form['txtNombre']
        edad = int(request.form['txtEdad'])
        cantidad_tarros = int(request.form['txtCantidad'])

        # Calcular total sin descuento
        sin_descuento = cantidad_tarros * precio_tarro

        # Aplicar descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        mostrar_resultado = True

        # Calcular total con descuento
        con_descuento = sin_descuento - (sin_descuento * descuento)
        descuento_precio = sin_descuento - con_descuento

    return render_template('ejercicio1.html',
                           nombre=nombre,
                           descuento_precio=descuento_precio,
                           con_descuento=con_descuento, sin_descuento=sin_descuento,
                           mostrar_resultado=mostrar_resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # Diccionario de usuarios
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }
    mensaje = ""
    mostrar_resultado = False

    if request.method == 'POST':
        usuario_ingresado = request.form.get('usuario')
        contrasena_ingresada = request.form.get('contrasena')
        # Verificar si el usuario y la contraseña coinciden usando el diccionario local
        if usuario_ingresado in usuarios and usuarios[usuario_ingresado] == contrasena_ingresada:
            session['usuario'] = usuario_ingresado
            mensaje = f"Bienvenido {'administrador' if usuario_ingresado == 'juan' else 'usuario'} {usuario_ingresado}"
        else:
            mensaje = "Credenciales incorrectas. Inténtalo de nuevo."

        mostrar_resultado = True

    return render_template('ejercicio2.html',
                           mensaje=mensaje,
                           mostrar_resultado=mostrar_resultado)


if __name__ == '__main__':
    app.run(debug=True)
