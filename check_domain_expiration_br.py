#!/usr/bin/python
#coding: utf-8

# Retorna data de expiracao de dominio
# Por Ronaldo Barcelos
# python 2.7 - 2015-04-20

# usage
# python check_domain_expiration_br.py site.com.br valor_warning valor_critical

import datetime
import commands
import sys
import os

DOMAIN = sys.argv[1]
WARNING = sys.argv[2]
CRITICAL = sys.argv[3]
ANO1 = commands.getoutput("whois "+ DOMAIN + "  | grep expires: | cut -c14-17")
MES2 = commands.getoutput("whois "+ DOMAIN +  "| grep expires: | cut -c18-19")
DIA3 = commands.getoutput("whois "+ DOMAIN +  "| grep expires: | cut -c20-21")

ANO=int(ANO1)
MES=int(MES2)
DIA=int(DIA3)

DT_EXP=datetime.datetime( ANO, MES, DIA).date()
 
FUTURO=datetime.datetime( ANO, MES, DIA) - datetime.datetime.today()
VALOR=FUTURO.days

if  VALOR < int(CRITICAL):
        print 'CRITICAL - DOMINIO', DOMAIN, 'EXPIRA EM:' ,str(DT_EXP)
        sys.exit(2)
    
elif VALOR < int(WARNING):
        print 'WARNING - DOMINIO', DOMAIN, 'EXPIRA EM:' ,str(DT_EXP)
        sys.exit(1)
else:
        print 'OK - FALTAM', VALOR, 'DIAS PARA EXPIRAR O DOMINIO', DOMAIN
        sys.exit(0)
