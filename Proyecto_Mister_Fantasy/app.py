from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuración de la conexión a la base de datos
db_connection = pymysql.connect(host='bxlfjozyadylicrojiil-mysql.services.clever-cloud.com', user='uvbui3pydp3dtywa', password='RlFkyyTF3rhbD2AppQHU', database='bxlfjozyadylicrojiil')

# Ruta para el registro de usuarios
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        
        # Realizar la inserción en la base de datos
        with db_connection.cursor() as cursor:
            sql = "INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)"
            cursor.execute(sql, (correo, contraseña))
            db_connection.commit()
        
        # Redirigir al usuario a la página de inicio de sesión
        return redirect(url_for('login'))
    return render_template('registro.html')

# Ruta para el inicio de sesión de usuarios
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        
        # Verificar las credenciales en la base de datos
        with db_connection.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s"
            cursor.execute(sql, (correo, contraseña))
            usuario = cursor.fetchone()
        
        if usuario:
            # Iniciar sesión del usuario
            session['correo'] = correo
            return redirect(url_for('inicio'))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html')

# Ruta para la página de inicio después de iniciar sesión
@app.route('/inicio')
def inicio():
    if 'correo' in session:
        correo = session['correo']
        return render_template('index.html', correo=correo)
    else:
        return redirect(url_for('login'))

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('correo', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
