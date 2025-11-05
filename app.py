from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():

     return "Olá, Mundo !"

@app.get("/info") 

def info(): 

   modulo = "Flask" 

   aula = 1 

   return f"<h1>Módulo: {modulo} — Aula {aula}<h1>"

@app.get("/bemvindo/<usuario>") 

def bemvindo(usuario):
   return f"<h1>Bem-vindo, {usuario.capitalize()}!<h1>"