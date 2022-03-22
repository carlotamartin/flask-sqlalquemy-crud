#Este archivo va a tener la configuración de la aplicación
#Flask es una librería de python que se utiliza apra crear aplicaciones web de una manera sencilla

from flask import Flask
from routes.contacts import contacts

app = Flask(__name__)


#Para poder utilizar los blueprints, hay que registrarlos -> register
app.register_blueprint(contacts)