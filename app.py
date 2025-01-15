from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.config["GITHUB_CLIENT_ID"] = "Ov23liR1KvxdssUzEEDu"
app.config["GITHUB_CLIENT_SECRET"] = "ba705e0f5b59f196e6de9bad2698cea5f841209f"

oauth = OAuth(app)
github = oauth.register(
    name='github',
    client_id=app.config['GITHUB_CLIENT_ID'],
    client_secret=app.config['GITHUB_CLIENT_SECRET'],
    authorize_url='https://github.com/login/oauth/authorize',
    access_token_url='https://github.com/login/oauth/access_token',
    client_kwargs={'scope': 'user:email'},
)

authorized_users = ['masaz31']

@app.route('/')
def home():
    if 'user_info' in session:
        user_info = session['user_info']
        if user_info["login"] in authorized_users:
            return f'''Hola, {user_info["login"]}! <br>
                       <img src="{user_info['avatar_url']}" alt="Avatar" width="50"><br>
                       <a href="/logout">Cerrar sesión</a>'''
        else:
            return redirect('/access-denied')  
    return 'No estás autenticado. <a href="/login">Iniciar sesión con GitHub</a>'  

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    token = github.authorize_access_token()
    
    user_info = github.get('https://api.github.com/user', token=token).json()
    
    session['user_info'] = user_info

    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_info', None)
    return redirect('/')

@app.route('/access-denied')
def access_denied():
    return "Acceso denegado. No tienes permisos para acceder a esta aplicación."

if __name__ == '__main__':
    app.run(debug=True)
