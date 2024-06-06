from flask import Flask, render_template, make_response, request

app = Flask(__name__)

application = app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/url')
def url():
    return render_template('url.html', title="URL", )


@app.route('/headers')
def headers():
    return render_template('headers.html', title="Headers")


@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html', title="Cookies"))
    if 'user' in request.cookies:
        resp.delete_cookie('user')
    else:
        resp.set_cookie('user', 'admin')
    return resp


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    return render_template('forms.html', title="Form parametrs")


@app.route("/phoneNumber", methods=["POST", "GET"])
def phoneNumber():
    if request.method == 'POST':
        phone = request.form["phone"]

        phone_num = [digit for digit in phone if digit.isdigit()]
        if not phone_num:
            phone_num.append("")

        error = ""
        if not all([symbol in [" ", "(", ")", "-", ".", "+", *list(map(str, list(range(10))))] for symbol in phone]):
            error = "Недопустимый ввод. В номере телефона встречаются недопустимые символы"
        elif ((phone_num[0] in ["7", "8"] and len(phone_num) != 11) or
              phone_num[0] not in ["7", "8"] and len(phone_num) != 10):
            error = "Недопустимый ввод. Неверное количество цифр"

        if error != "":
            return render_template("phoneNumber.html", title="Phone Number", phone=error)

        if len(phone_num) == 10:
            phone_num.insert(0, "8")

        return render_template("phoneNumber.html", title="Phone Number",
                               phone="8-{1}{2}{3}-{4}{5}{6}-{7}{8}-{9}{10}".format(*phone_num))
    else:
        return render_template("phoneNumber.html", title="Phone Number")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5100)