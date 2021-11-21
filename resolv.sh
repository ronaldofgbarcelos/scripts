#!/bin/bash

# script para resolucao de ips oriundos do arquivo chamado hosts.txt
while read LINHA
do
	IP=$( echo "$LINHA" )
	HOST=$(host "$IP")
	echo "$LINHA" "$HOST"
done < hosts.txt
