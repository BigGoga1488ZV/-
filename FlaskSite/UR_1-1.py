from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask (__name__)
app.config['SECRET_KEY'] = 'goidaZV1488VZslavaukraine'


menu = [{"name": "Привет", "url": "/Q"},
        {"name": "Пока", "url": "/login"},
        {"name": "Порно", "url": "/1488"}]
fot = ["Фотки"]

@app.route('/')
def main():
    print(url_for('main'))
    return render_template('base.html', menu=menu)

# @app.route('/Привет')
# def first():
#     print(url_for('first'))
#     return render_template('main.html', title = "Ответвление 1", fot=fot)

@app.route("/Q", methods=['GET', 'POST'])
def Q():
    show_video = False
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', 'success')
            show_video = True
        else:
            flash('Ошибка отправки', 'error')
    return render_template('ForQ.html', title="Привет", title_align="left", menu=menu, show_video=show_video)

@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return render_template('Prof.html', title="Профиль", username=username, menu=menu)

@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "Ж" and request.form['psw'] == "123123123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('LOG.html', title="Авторизация", menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('PG404.html', title='Долбаёб?', menu=menu), 404

@app.route('/lol')
def main404():
    print(url_for('main404'))
    return render_template('base1.html', menu=menu)


#with app.test_request_context():
    print(url_for('main'))
    print(url_for('first'))
    print(url_for('Q'))

if __name__ == "__main__":
    app.run(debug=True)