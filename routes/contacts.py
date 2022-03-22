#En este archivo, vamos a tener todas las rutas de una forma organizada
#Blueprint -> son los módulos con los que se construye la aplicación, su objetivo es la organización del códio
from flask import Blueprint

contacts = Blueprint ('contacts', __name__)

#En las rutas, se pueden devolver tanto un string como un html
@contacts.route('/')
def home():
    return '<h1>contacts list </h1>'


@contacts.route('/new')
def add_contact():
    return 'saving a contact'

