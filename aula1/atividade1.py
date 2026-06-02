from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def texto_explicativo():
    return '1. O que é um Decorator?Em Python, funções são objetos de "primeira classe", o que significa que podem ser passadas como argumentos para outras funções. Um decorator é simplesmente uma função que recebe outra função, adiciona alguma lógica extra a ela e a devolve pronta para o uso.No código, ele aparece com o símbolo @ (conhecido como "açúcar sintático"), posicionado logo acima da função que ele está "decorando".2. Para que ele serve?O objetivo principal é a reutilização de código e a separação de responsabilidades. Em vez de escrever a mesma lógica dentro de dez funções diferentes, você cria um decorator e o aplica onde for necessário.Aplicações comuns:Autenticação: Verificar se o usuário tem permissão antes de executar a função.Logs: Registrar no sistema cada vez que uma função é chamada.Cache: Guardar o resultado de uma função pesada para não precisar recalculá-la.3. O uso no Flask: @app.routeNo Flask, os decorators são a base para conectar as URLs do navegador ao código Python.Como o @app.route funciona por dentro:Quando você escreve @app.route("/contato"), você não está apenas "etiquetando" a função. Você está chamando um método do objeto app que:Pega a função que vem logo abaixo.Associa o endereço /contato a essa função dentro de um dicionário interno do Flask.Garante que, quando o servidor receber uma requisição para esse endereço, ele saiba exatamente qual função deve "disparar".' 

if __name__ == '__main__':
    app.run(debug=True)