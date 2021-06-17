import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json

def recomendacaoDemo(localidades, generos, tipo_eventos):
    localidade = localidades
    genero = generos
    tipo_evento = tipo_eventos
    ListaArtistas = []

    url = 'https://raw.githubusercontent.com/arthurpiratas/apiRecomendacaoGigB/master/src/servico/Base-Artista-Gigb1.csv'

    df1=pd.read_csv(url, sep = ',', )

    mediaGeral = round(df1['notaMedia'].mean())
    baseAtivos = df1.copy().loc[df1['status'] == 'Ativo']
    BaseSemStrike = baseAtivos.copy().loc[baseAtivos['QtdDeStrike'] <= 1]
    BaseMediaGeral = BaseSemStrike.copy().loc[BaseSemStrike['notaMedia'] >= mediaGeral]
    BaseParticipacaoEventos = BaseMediaGeral.copy().loc[BaseMediaGeral['QtdDeEventosPresente'] >= 80]
    baseFinal = BaseParticipacaoEventos.copy().loc[(BaseParticipacaoEventos['notaMedia'] * BaseParticipacaoEventos['QtdDeVotos']) >= 300]

    def votosPonderado(x):
        media = x['notaMedia']
        qtdVotos = x['QtdDeVotos']
        return (media*qtdVotos)

    baseFinal['score'] = baseFinal.apply(votosPonderado, axis=1)
    baseFinal = baseFinal.copy().loc[baseFinal['generoMusical'].str.contains(genero) == True]
    baseFinal = baseFinal.copy().loc[baseFinal['endereco'].str.contains(localidade) == True]
    baseFinal = baseFinal.copy().loc[baseFinal['valorTipoEvento'].str.contains(tipo_evento) == True]

    baseFinal = baseFinal.sort_values('score', ascending=False).head(10)

    linhas = baseFinal[['ID']].shape
    baseFinal.head(linhas[0])

    def retornaLista(linhas):
        for (i,linhas) in baseFinal.head(10 if linhas[0] >= 10 else linhas[0]).iterrows():
            objetoID = {'ID' : + str(linhas['ID'])}
            ListaArtistas.append(objetoID)
        bandas = {"Bandas" : ListaArtistas}
        return bandas

    
    return retornaLista(linhas)
    


