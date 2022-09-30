#script para fazer analise do monitoramento de pacotes do protocolo de automação i104
# -*- coding: utf-8 -*-
import pandas as pd
import re

def ManipulaLinha(linha):
    i=-1
    if linha.find('<-')!=-1:
        i = linha.find('<-')
    elif linha.find('->')!=-1:
        i = linha.find('->')
    if i==-1:
        horario = linha[:8]
        msg = re.sub(r"^\s+|\s+$", "", linha[8:])
        linha = [horario, msg] 
    elif i!=-1:
        horario = linha[:8]
        origem = re.sub(r"\s+", "", linha[8:i-10])
        tamanho = re.sub(r"^\s+|\s+$", "", linha[i-10:i])
        direcao = re.sub(r"\s+", "", linha[i:i+2])
        cabecalho = re.sub(r"^\s+|\s+$", "", linha[i+2:i+15])
        utr = re.sub(r"^\s+|\s+$", "", linha[i+15:i+20])
        informacao = re.sub(r"^\s+|\s+$", "", linha[i+20:])
        
        if re.sub(r"^\s+|\s+$", "", cabecalho[:3])=='30':
            tpFrame = 'Comando de SetPoint'
            if re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='06':
                causa = 'ATIVAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='07':
                causa = 'CONFIRMAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='0a':
                causa = 'TÉRMINO'
            else:
                causa = ''
        elif re.sub(r"^\s+|\s+$", "", cabecalho[:3])=='6b':
            tpFrame = 'Comando de Teste'
            if re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='06':
                causa = 'ATIVAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='07':
                causa = 'CONFIRMAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='0a':
                causa = 'TÉRMINO'
            else:
                causa = ''
        elif re.sub(r"^\s+|\s+$", "", cabecalho[:3])=='64':
            tpFrame = 'Comando de Interrogação'
            if re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='06':
                causa = 'ATIVAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='07':
                causa = 'CONFIRMAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", cabecalho[5:8])=='0a':
                causa = 'TÉRMINO'
            else:
                causa = ''
        else:
            tpFrame = ''
            causa = ''
        linha = [horario, origem, tamanho, direcao, cabecalho, utr, tpFrame, causa]
    return linha

arquivo = open(r'i104_modelo.txt')

lista = []
lista2 = []

for l in arquivo.readlines():
    line = ManipulaLinha(l)
    if len(line)>2:
        lista.append(line)
    else:
        lista2.append(line)

arquivo.close()

dtMon = pd.DataFrame(lista, columns=['Horário', 'Origem', 'Tamanho', 'Dir.',
                                     'Cabeçalho', 'UTR', 'Tipo do Frame',
                                     'Causa da Transmissão'])

dtMsg = pd.DataFrame(lista2, columns=['Horário', 'Mensagem'])
dtMsg = dtMsg.drop(dtMsg.index[[0]])#Apaga a primeira linha do arquivo


dtMon.to_excel(r'C:\Empresa\dev\i104Analysis\mon_104.xlsx',
               sheet_name='Monitoramento', index=False)
dtMsg.to_excel(r'C:\Empresa\dev\i104Analysis\msgs_104.xlsx',
               sheet_name='Mensagens', index=False)