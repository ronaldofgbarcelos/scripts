#!/usr/bin/python
#coding: utf-8

# verifica versoes de pacotes no venv
# Por Ronaldo Barcelos
# python 2.7 - 2017-05-23


import urllib

#coleta na server01 
f = urllib.urlopen("http://server01.com/verify_pip_packages/pip_packages_version.txt")
delivery1 = f.read()
f.close()

#coleta na server02
f = urllib.urlopen("http://server02.com/verify_pip_packages/pip_packages_version.txt")
delivery2 = f.read()
f.close()

#coleta na server03
f = urllib.urlopen("http://server03.com/verify_pip_packages/pip_packages_version.txt")
delivery3 = f.read()
f.close()

#coleta na server04
f = urllib.urlopen("http://server04.com/verify_pip_packages/pip_packages_version.txt")
delivery4 = f.read()
f.close()

#coleta na mauqina06
f = urllib.urlopen("http://server05.com/verify_pip_packages/pip_packages_version.txt")
delivery5 = f.read()
f.close()

#coleta na server06
f = urllib.urlopen("http://server06.com/verify_pip_packages/pip_packages_version.txt")
delivery6 = f.read()
f.close()

if delivery1 == delivery2 and delivery1 == delivery3 and delivery1 == delivery4 and delivery1 == delivery5 and delivery1 == delivery6:
   print ("Version OK")

elif delivery1 != delivery2:
   print ("server02-mia NOK")

elif delivery1 != delivery3:
   print ("server03-mia NOK")

elif delivery1 != delivery4:
   print ("server04-mia NOK")

elif delivery1 != delivery5:
   print ("server05-mia NOK")

elif delivery1 != delivery6:
   print ("server06-mia NOK")
