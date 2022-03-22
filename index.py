#Este archivo se va a utilizar para que la aplicación empiece a funcionar
from app import app


if __name__ == '__main__':
    #debug=True se utiliza para que la consola no tengamos que reiniciar cada vez que cambiamos el código
    app.run(debug=True)