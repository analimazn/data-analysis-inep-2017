''' @author: Ana Cristina Lima (analimazn@gmail.com)

    Análise de dados sobre a quantidade de alunos:
        - Ingressos
        - Matriculados
        - Concluintes
    De acordo com a região para o ano de 2017.

    Dados disponibilizados pelo Inep nos seguintes links:
    http://inep.gov.br/inep-data
    https://inepdata.inep.gov.br/analytics/saw.dll?Dashboard
'''

#Bibliotecas utilizadas
import pandas as pd
import numpy as np
import seaborn as sns

#Variáveis utilizadas para preencher o dataframe
path = 'data/'
firstName = 'dado_de_'
files = {'ingressos', 'matriculas', 'concluintes'}
lastName = '_2017'
extension = '.csv'

#Função para preencher o dataframe com os dados presentes em .csv
def populateDataFrame(path, firstName, files, lastName, extension):
    dfList = list()

    for file in files:
        pd.set_option('max_colwidth', 8)
        df = pd.DataFrame(pd.read_csv(path+firstName+file+lastName+extension))
        dfList.append(df)

    df = pd.concat(dfList, sort=True)
    return df

# Dataframe gerado dos dados utilizados
df = populateDataFrame(path, firstName, files, lastName, extension)

''' Quantidade de alunos ingressos, matriculados e concluintes 
    de instituições públicas e privadas de acordo com a REGIÃO 
'''
df.groupby(['REGIÃO', 'CATEGORIA ADMINISTRATIVA', 'DADO'])['QUANTIDADE'].sum()

''' Quantidade de alunos ingressos, matriculados e concluintes 
    de instituições públicas e privadas de acordo com a UF 
'''
df.groupby(['UF', 'CATEGORIA ADMINISTRATIVA', 'DADO'])['QUANTIDADE'].sum()

''' Quantidade de alunos ingressos, matriculados e concluintes 
    de instituições públicas e privadas de acordo com a SUB CATEGORIA ADMINISTRATIVA 
'''
df.groupby(['SUB CATEGORIA ADMINISTRATIVA', 'CATEGORIA ADMINISTRATIVA', 'DADO'])['QUANTIDADE'].sum()

''' Quantidade de alunos ingressos, matriculados e concluintes 
    de instituições públicas e privadas de acordo com a SUB CATEGORIA ADMINISTRATIVA e REGIÃO
'''
df.groupby(['REGIÃO', 'SUB CATEGORIA ADMINISTRATIVA', 'CATEGORIA ADMINISTRATIVA', 'DADO'])['QUANTIDADE'].sum()

''' Quantidade de alunos ingressos, matriculados e concluintes 
    de instituições públicas e privadas de acordo com a SUB CATEGORIA ADMINISTRATIVA e UF
'''
df.groupby(['UF', 'SUB CATEGORIA ADMINISTRATIVA', 'CATEGORIA ADMINISTRATIVA', 'DADO'])['QUANTIDADE'].sum()

''' Média de alunos ingressos, matriculados e concluintes 
    de instituições públicas e privadas de acordo com a UF 
'''
df.groupby(['UF', 'CATEGORIA ADMINISTRATIVA', 'DADO'])['QUANTIDADE'].median()

''' Média de alunos ingressos, matriculados e concluintes 
    de instituições públicas e privadas de acordo com a REGIÃO 
'''
df.groupby(['REGIÃO', 'CATEGORIA ADMINISTRATIVA', 'DADO'])['QUANTIDADE'].median()


