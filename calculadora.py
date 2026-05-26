import math
from flask import render_template, request

def calcular():
    try:
        num1 = float(request.form["num1"])
    except (ValueError, KeyError):
        return render_template("calculadora.html", etapas="Erro: Primeiro número inválido.", resultados="")
        
    operacao = request.form["operacao"]

    # Operações que usam apenas o primeiro número
    if operacao == "sqrt":
        if num1 < 0:
            return render_template("calculadora.html", etapas=f"Não existe raiz real de {num1}.", resultados="Erro: número negativo")
        resultado = math.sqrt(num1)
        return render_template("calculadora.html", etapas=f"√{num1} = {resultado}", resultados=resultado)

    # Operações que exigem ou aceitam o segundo número
    num2_valor = request.form.get("num2", "").strip()
    
    # Se for logaritmo e o num2 estiver vazio, assume base natural (e)
    if operacao == "log" and not num2_valor:
        if num1 <= 0:
            return render_template("calculadora.html", etapas=f"O logaritmo exige número maior que zero. Recebido: {num1}", resultados="Erro: valor inválido")
        resultado = math.log(num1)
        return render_template("calculadora.html", etapas=f"ln({num1}) = {resultado}", resultados=resultado)
        
    # Para as demais operações, num2 é obrigatório
    if not num2_valor:
        return render_template("calculadora.html", etapas="Informe o segundo número para esta operação.", resultados="")
        
    try:
        num2 = float(num2_valor)
    except ValueError:
        return render_template("calculadora.html", etapas="Erro: Segundo número inválido.", resultados="")

    # Execução das operações de dois números
    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2} = {resultado}"
    elif operacao == "/":
        if num2 == 0:
            return render_template("calculadora.html", etapas="Divisão por zero não é permitida.", resultados="Erro: divisão por zero")
        resultado = num1 / num2
        etapas = f"{num1} ÷ {num2} = {resultado}"
    elif operacao == "**":
        resultado = math.pow(num1, num2)
        etapas = f"{num1} ^ {num2} = {resultado}"
    elif operacao == "log":
        if num1 <= 0 or num2 <= 0 or num2 == 1:
            return render_template("calculadora.html", etapas="O número e a base devem ser maiores que zero. A base não pode ser 1.", resultados="Erro: base/argumento inválido")
        resultado = math.log(num1, num2)
        etapas = f"log na base {num2} de ({num1}) = {resultado}"
    else:
        return render_template("calculadora.html", etapas="Operação inválida.", resultados="")

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)
