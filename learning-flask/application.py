from flask import Flask, render_template, request, session
from flask_session import Session
app = Flask(__name__)
notes = list()


# Aplicação para receber um formulário e adicionar a uma lista de notas,
# que será exibida na tela
# Main Program
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('notes') is None:
        session['notes'] = list()
    if request.method == 'POST':
        note = request.form.get('note')
        session['notes'].append(note)
    return render_template('index4.html', notes=session['notes'])
