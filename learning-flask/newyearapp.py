from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)


# aplicação para mostrar na tela se é ano novo ou não
# Main program
@app.route('/')
def index():
    now = datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template('index.html', new_year=new_year)
