import os
from flask import Flask
from flask_restplus import Api

class Server(): 
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
            version='1.0',
            title='Api de recomendacao demografica',
            description='Recomendacao Demografica da aplicacao GigB', 
            doc='/docs')

    def run(self, ):
        Port = int(os.environ.get("PORT", 5000))
        self.app.run(
            debug=False, 
            host='0.0.0.0', 
            port=Port
            #cancelar o debug qnd tiver em produção
        )
server = Server()