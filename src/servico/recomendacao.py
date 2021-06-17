import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json

def recomendacaoDemo(localidades, generos, tipo_eventos):
    localidade = localidades
    genero = generos
    tipo_evento = tipo_eventos
    ListaArtistas = []

    data = {
        'País': ['Bélgica', 'Índia', 'Brasil'],
        'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília'],
        'População': [123465, 456789, 987654]
    }

    df = pd.DataFrame(data, columns=['País','Capital','População'])

    return "retornaLista(linhas)"
    


