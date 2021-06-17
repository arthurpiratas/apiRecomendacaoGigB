from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
#from pandas.io import api

from src.server.instance import server

app, api = server.app, server.api

from src.servico.recomendacao import recomendacaoDemo

@api.route('/recoDemo', methods=['GET', 'POST'])
class recoDemo(Resource):
    def get(self, ):
        # http://localhost:5000/recoDemo?localidade=Recife&genero=jaz&tipo_evento=Apresentação em Bar
        localidade = request.args.get('localidade', default = 'nulo',  type = str)
        genero = request.args.get('genero', default = 'nulo', type = str) 
        tipo_evento = request.args.get('tipo_evento' , default = 'nulo', type = str)
        #localidade = "Recife"
        #genero = "jaz"
        #tipo_evento = "Apresentação em Bar"
        if(localidade == 'nulo' or genero == 'nulo' or tipo_evento == 'nulo'):
            return 'bad request', 400

        #return geraResponse(200, "Sucesso","Bandas", recomendacaoDemo(localidade, genero, tipo_evento)) 
        return recomendacaoDemo(localidade, genero, tipo_evento), 200 
    
    def post(self, ):
        response = api.payload
        if("localidade" not in response or "genero" not in response or "tipo_evento" not in response):
            return geraResponse(400, "Erro! Sem Parâmetros necessários")
        
        localidade = response["localidade"]
        genero = response["genero"]
        tipo_evento = response["tipo_evento"]

        return geraResponse(200, "Sucesso", "Bandas", recomendacaoDemo(localidade, genero, tipo_evento)) 



def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["Status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response