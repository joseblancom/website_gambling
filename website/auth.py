from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html', boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('El correo ingresado es muy corto', category='error')
        elif len(firstName) < 2:
            flash('El nombre ingresado es muy corto', category='error')
        elif password1 != password2:
            flash('Las claves ingresadas con coinciden', category='error')
        elif len(password1) < 7:
            flash('La clave es muy corta', category='error')
        else:
            flash('Usuario creado con exito', category='success')

    return render_template('sign_up.html')