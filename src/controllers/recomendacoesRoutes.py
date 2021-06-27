from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
from flask_cors import CORS
#from pandas.io import api

from src.server.instance import server

app, api = server.app, server.api

CORS(app)

from src.servico.recomendacao import recomendacaoDemo
from src.servico.consultaEventosArtista import listaEventosArtistas

@api.route('/recoDemo', methods=['GET', 'POST'])
class recoDemo(Resource):
    def get(self, ):
        localidade = request.args.get('localidade', default = 'nulo',  type = str)
        genero = request.args.get('genero', default = 'nulo', type = str) 
        tipo_evento = request.args.get('tipo_evento' , default = 'nulo', type = str)
        if(localidade == 'nulo' or genero == 'nulo' or tipo_evento == 'nulo'):
            return 'bad request', 400

        return recomendacaoDemo(localidade, genero, tipo_evento), 200 
    
    def post(self, ):
        response = api.payload
        if("localidade" not in response or "genero" not in response or "tipo_evento" not in response):
            return geraResponse(400, "Erro! Sem Parâmetros necessários")
        
        localidade = response["localidade"]
        genero = response["genero"]
        tipo_evento = response["tipo_evento"]

        return geraResponse(200, "Sucesso", "Bandas", recomendacaoDemo(localidade, genero, tipo_evento)) 

@api.route('/ListaEventos', methods=['GET'])
class listarEventos(Resource):
    def get(self, ):
        id_artista = request.args.get('Id_artista', default = 'nulo',  type = int)
        if(id_artista == 'nulo'):
            return 'bad request', 400

        return listaEventosArtistas(id_artista), 200 
    
    



def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["Status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response