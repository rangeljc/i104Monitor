#script para fazer analise do monitoramento de pacotes do protocolo de automação i104
# -*- coding: utf-8 -*-

#abrir arquivos em python
arquivo = open(r'i104_modelo.txt')
i = 1
for linha in arquivo.readlines():
    print(linha)
    if i == 10:
        break
    else:
        i=i+1
arquivo.close()