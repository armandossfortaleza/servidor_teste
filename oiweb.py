from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Oi www!"

@app.route("/bemvindo")
def bem_vindo():
    return render_template('bem_vindo.html')

@app.route("/felinos")
def meus_felinos():
    return render_template('felinos.html')