#!/usr/bin/python
#coding: utf-8

# Por Ronaldo Barcelos
# 14-06-2019

import requests
import json
import wget
import os
import logging

#salva arquivo de saida monit-openid - OK ou NOK
def salvaResultado (result):
    f = open('/tmp/openid-status', 'w')
    s = str(result)
    f.write(s) 

#config de logging
logging.basicConfig(filename='openid.log',format='%(asctime)s %(message)s',level=logging.INFO)

#verifica se a pagina esta ok - http code 200
logging.info('-----------------------------------------------------')
logging.info('-                                                   -')
logging.info('-          INITIATING MONITORING SCRIPT             -')
logging.info('-                                                   -')
logging.info('-----------------------------------------------------')
logging.info('starting with http code validation - expected code 200')
req = requests.get('https://sitesitesite.com.br/oauth/.well-known/openid-configuration')
logging.info('validating existence of the openid-configuration file')
if req.status_code == 200:
    filedir = os.listdir()
    file1 = "openid-configuration"
    file2 = "openid-configuration.old"
    # verifica se o arquivo openid-configuration existe
    if os.path.isfile('openid-configuration'):
            # renomeia o arquivo antigo para pegar o json mais atualizado na sequencia
            os.rename(file1,file2)
            #faz o wget do arquivo com json mais atualizado
            url = 'https://sitesitesite.com.br/oauth/.well-known/openid-configuration'
            json_saved = wget.download(url)
            logging.info('monit OK')
            salvaResultado('OK')

    else: 
            #efetua download do arquivo caso nao exista
            logging.info('openid-configuration file was not found and will be made a wget in the url')
            logging.info ('downloading')
            url = 'https://sitesitesite.com.br/oauth/.well-known/openid-configuration'
            json_saved = wget.download(url)
            logging.info('monit NOK')
            salvaResultado('NOK')

else:
    print('ERROR ON RETURN OF URL')
    logging.info('http code was not 200')
