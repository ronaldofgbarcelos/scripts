#!/usr/bin/python
#coding: utf-8
# testa a disponibilidade do json base para o Dullahan
# Por Ronaldo Barcelos
# 28-05-2019

import requests
import json
import wget
import datetime
import sys
import os

req = requests.get('http://ci.domain.com/job/testes-portal-parceiros/lastCompletedBuild/artifact/jenkins/test-parceiros.json')
if req.status_code == 200:
       url = 'http://ci.domain.com/job/testes-portal-parceiros/lastCompletedBuild/artifact/jenkins/test-parceiros.json'
       json_saved = wget.download(url)
       arq = open ('test-parceiros.json','r')
       content = arq.read()
       print (' \n')
       print (content)
else:
       print('ERRO NO CI')
