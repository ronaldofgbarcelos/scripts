#!/usr/bin/python
#coding: utf-8

# Por Ronaldo Barcelos
# 17-09-2020
# Python3.7

import urllib.request
import json
import requests
import logging

#salva arquivo de saida da monitoracao - OK ou NOK
def salvaResultado (result):
    f = open('/tmp/json-status.txt', 'w')
    s = str(result)
    f.write(s)

#config de logging
logging.basicConfig(filename='/var/log/monit-json.log',format='%(asctime)s %(message)s',level=logging.INFO)

#verifica se a pagina esta ok - http code 200
logging.info('-----------------------------------------------------')
logging.info('-                                                   -')
logging.info('-          INITIATING MONITORING SCRIPT             -')
logging.info('-                                                   -')
logging.info('-----------------------------------------------------')
logging.info('starting with http code validation - expected code 200')

#grava o dado a ser parseado na variavel good
good = 'SUCCESS'
url = "https://xxxxxxxxxxxxxx.com.br/api/support/monitoring/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
if requests.get(url).status_code == 200:
   try:
       logging.info ('http_code 200.....ok')
       #grava o json e faz o decode do mesmo
       url= urllib.request.urlopen('https://xxxxxxxxxxxxxxxxxxxxxxx.com.br/api/support/monitoring/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
       x= url.read()
       y = json.loads(x.decode('utf-8'))
       #apos conversao grava o conteudo na variavel conv apenas o resultado referente status
       conv = y['status']
       if conv == good:
               logging.info('monit OK')
               salvaResultado('Status OK')
               logging.info ('END OF MONITORING!!!')
       else:
               logging.info('monit NOK')
               salvaResultado('Status NOK')
               logging.info ('END OF MONITORING!!!')
               logging.info ('Check the documentation - http://github.com/xxxxxxxxxxxxxxxxxxxx')

   except Exception as e:
       print("Servidor indisponível. Erro:", e)
       logging.info ('END OF MONITORING!!!')
       logging.info ('Check the documentation - http://github.com/xxxxxxxxxxxxxxxxxxxxxxxxxxx')

else:
       print('ERROR ON RETURN OF URL')
       logging.info('http code was not 200')
       logging.info ('END OF MONITORING!!!')
       logging.info ('Check the documentation - http://github.com/xxxxxxxxxxxxxxxxxxxxxxxxx')
