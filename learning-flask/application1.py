from flask import Flask, render_template
app = Flask(__name__)


# applicação para
    # - mostrar loopings no html
    # - redirecionando para funcoes com rotas no python e href no html
    # - template de herença através do jinja2

# Main Program
@app.route('/')
def index():
    names = ['Alice', 'Bob', 'Charlie', 'David']
    return render_template('index2.html', names=names)


@app.route('/more')
def more():
    return render_template('more.html')
