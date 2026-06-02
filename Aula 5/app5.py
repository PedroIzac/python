from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario_escrito = request.form.get('usuario')
    senha_escrito = request.form.get('senha')
    lista_usuarios = {
       "Pedro" : "pedro123",
       "Dolga" : "cotemig2026",
       "Janaina" : "cotemig2026",
       "Antonio" : "cotemig2026"
    }


    while True:
        login_sucesso = False

        for usuario, senha in lista_usuarios.items():
            if usuario_escrito == usuario and senha_escrito == senha:
                login_sucesso = True
                break  

        if login_sucesso:
            return(f" Acesso permitido! Bem-vindo(a), {usuario_escrito}.")
        else:
            return(" Acesso negado! Usuário ou senha incorretos. Tente novamente.")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)