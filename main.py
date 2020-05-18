from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")
    response = make_response(render_template("index.html"))

    if secret_number is None:
        secret_number = random.randint(0, 30)
        response.set_cookie("secret_number", str(secret_number))
    return response


@app.route("/result", methods=["POST"])
def result():
    num_user = int(request.form.get("num_user"))
    secret_number = int(request.cookies.get("secret_number"))

    if num_user == secret_number:
        mensaje = "Enhorabuena!! El numero correcto es: " + str(secret_number)
        response = make_response(render_template("result.html", mensaje=mensaje))
        response.set_cookie("secret_number", str(random.randint(0, 30)))
        return response

    elif num_user > secret_number:
        mensaje = "Tu numero no es correcto! Intentalo con uno mas pequeño!"
        return render_template("result.html", mensaje=mensaje)

    elif num_user < secret_number:
        mensaje = "Tu numero no es correcto! Intentalo con uno mas grande!"
        return render_template("result.html", mensaje=mensaje)


if __name__ == '__main__':
    app.run()