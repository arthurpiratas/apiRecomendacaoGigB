import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


def listaEventosArtistas(id_Artista):

    ID_artista = id_Artista
    ListaEventos = []  

    df1=pd.read_csv('src\servico\Base_Eventos.csv')
    EventosAtivos = df1.copy().loc[df1['status'] != 'cancelado']
    EventosAtivos = EventosAtivos.copy().loc[EventosAtivos['status'] != 'concluido']
    EventosMusico = EventosAtivos.copy().loc[EventosAtivos['ID_Artista'] == ID_artista]
    linhas = EventosMusico['ID_Evento'].shape
    EventosMusico.reset_index(inplace=True, drop=False)

    def retornaLista(linhas):
        for (i,linhas) in EventosMusico.head(10 if linhas[0] >= 10 else linhas[0]).iterrows():
            objetoID = {'ID_Evento' :  str(EventosMusico.at[i,'ID_Evento']), 'Nome_Organizador' : str(EventosMusico.at[i,'Nome_Organizador']), 'nota_avaliacao_organizador' : str(EventosMusico.at[i,'nota_avaliacao_organizador']), 'Local_Evento' : str(EventosMusico.at[i,'Local_Evento']), 'nomeEvento' : str(EventosMusico.at[i,'nomeEvento']), 'Descrição_Evento' : str(EventosMusico.at[i,'Descrição_Evento']), 'data' : str(EventosMusico.at[i,'data']), 'horario' : str(EventosMusico.at[i,'horario']), 'status' : str(EventosMusico.at[i,'status']), 'tipoEvento' : str(EventosMusico.at[i,'tipoEvento']), 'duracaoEvento' : str(EventosMusico.at[i,'duracaoEvento']), 'localidade' : EventosMusico.at[i,'localidade'], 'observacoes' : str(EventosMusico.at[i,'observacoes']), 'Valor_total_evento' : str(EventosMusico.at[i,'Valor total evento']), 'latitude' :EventosMusico.at[i,'latitude'], 'longitude' :EventosMusico.at[i,'longitude']}
            ListaEventos.append(objetoID)
        eventos = {"Eventos" : ListaEventos}
        return eventos
    
    return retornaLista(linhas)


