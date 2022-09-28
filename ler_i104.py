#script para fazer analise do monitoramento de pacotes do protocolo de automação i104
# -*- coding: utf-8 -*-
import re
#abrir arquivos em python
arquivo = open(r'i104_modelo.txt')
i = 1
#for linha in arquivo.readlines():
#    print(linha)
#    if i == 10:
#        break
#    else:
#        i=i+1
#arquivo.close()
lista =[]
for linha in arquivo.readlines():
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
        if re.sub(r"^\s+|\s+$", "", linha[i+2:i+5])=='30':
            tpFrame = 'Comando de SetPoint'
            if re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='06':
                causa = 'ATIVAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='07':
                causa = 'CONFIRMAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='0a':
                causa = 'TÉRMINO'
            else:
                causa = ''
        elif re.sub(r"^\s+|\s+$", "", linha[i+2:i+5])=='6b':
            tpFrame = 'Comando de Teste'
            if re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='06':
                causa = 'ATIVAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='07':
                causa = 'CONFIRMAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='0a':
                causa = 'TÉRMINO'
            else:
                causa = ''
        elif re.sub(r"^\s+|\s+$", "", linha[i+2:i+5])=='64':
            tpFrame = 'Comando de Interrogação'
            if re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='06':
                causa = 'ATIVAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='07':
                causa = 'CONFIRMAÇÃO'
            elif re.sub(r"^\s+|\s+$", "", linha[i+8:i+11])=='0a':
                causa = 'TÉRMINO'
            else:
                causa = ''
        else:
            tpFrame = ''
            causa = ''
        lista.append([horario, origem, tamanho, direcao, cabecalho, utr, tpFrame, causa])
        
arquivo.close()
print(lista[:10])
