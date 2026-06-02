from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Pedro Henrique</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; color: #333; line-height: 1.6; padding: 20px; }
        .container { max-width: 800px; margin: auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        h2 { color: #2980b9; margin-top: 25px; font-size: 1.4em; }
        .contact-info { font-style: italic; color: #7f8c8d; margin-bottom: 20px; }
        .badge { background: #3498db; color: white; padding: 4px 10px; border-radius: 15px; font-size: 0.85em; display: inline-block; margin: 3px; }
        .item { margin-bottom: 15px; }
        .item strong { color: #444; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Pedro Henrique Braga Izac</h1>
        <div class="contact-info">
            Belo Horizonte/MG | (31) 9 8451-7632 | pedrohbizac@gmail.com
        </div>

        <h2>Objetivo Profissional</h2>
        <p>Estudante de Informática (COTEMIG) focado em aplicar conhecimentos técnicos e comerciais em oportunidades formais de trabalho.</p>

        <h2>Experiência</h2>
        <div class="item">
            <strong>Estagiário Comercial - Meu Bolinho</strong> (12/2025 – 03/2026)<br>
            Atuação como SDR, qualificação de leads e fechamento de contratos.
        </div>
        <div class="item">
            <strong>Estagiário - Atlas Consultoria Digital</strong> (09/2023 – 11/2025)<br>
            Apoio a rotinas de e-commerce, sistemas ERP (Tiny) e marketplaces.
        </div>

        <h2>Habilidades e Tecnologias</h2>
        <div>
            {% for skill in skills %}
                <span class="badge">{{ skill }}</span>
            {% endfor %}
        </div>

        <h2>Formação</h2>
        <p>Técnico em Informática + Ensino Médio - COTEMIG (Previsão: 2026)</p>
    </div>
</body>
</html>
"""

@app.route('/curriculo')
def home():
    habilidades = [
        "HTML/CSS", "PHP", "Python", "SQL", "C#", 
        "ERP Tiny", "Marketplaces", "Inglês Avançado", 
        "SDR & Vendas", "Pacote Office"
    ]
    return render_template_string(HTML_TEMPLATE, skills=habilidades)

if __name__ == '__main__':
    app.run(debug=True)