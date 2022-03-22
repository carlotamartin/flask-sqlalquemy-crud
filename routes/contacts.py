#En este archivo, vamos a tener todas las rutas de una forma organizada
#Blueprint -> son los módulos con los que se construye la aplicación, su objetivo es la organización del códio
#render_template -> es un módulo que sirva para distribuit un archivo html al navegador
from flask import Blueprint, render_template

contacts = Blueprint ('contacts', __name__)

#En las rutas, se pueden devolver tanto un string como un html
@contacts.route('/')
def home():
    return render_template('index.html')


@contacts.route('/new')
def add_contact():
    return 'saving a contact'

@contacts.route('/abaut')
def abaut():
    return render_template('abaut.html')
