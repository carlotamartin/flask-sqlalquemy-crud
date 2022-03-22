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

#Crearemos esta ruta para cuando la aplicación añada un contacto
@contacts.route('/update')
def update_contact():
    return 'update a contact'

#Crearemos esta ruta para cuando la aplicación elimine un contacto
@contacts.route('/delete')
def delete_contact():
    return 'delete a contact'

@contacts.route('/abaut')
def abaut():
    return render_template('abaut.html')
