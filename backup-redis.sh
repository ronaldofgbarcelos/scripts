#!/bin/bash

#######################################
# Script de Backup - Redis
# Por Ronaldo Barcelos
#######################################
ME=$(hostname)
REDIS_DIR=/var/lib/redis
BACKUP_DIR=/path/onde-sera-armazenado/backup-redis
LOG_FILE=/var/log/redis_backup.log
REDIS_CLI=/usr/bin/redis-cli
REDIS_HOST="localhost ou remoto"
REDIS_PORT=6379
REDIS_AUTH="chave-de-autenticacao-redis"

function log_message() {
    local MESSAGE=$1
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $MESSAGE" | tee -a $LOG_FILE
}

function backup_files() {
    log_message "Iniciando backup dos arquivos do Redis no host $ME..."

    if rsync -avh --delete $REDIS_DIR/ $BACKUP_DIR/$ME/db/ >> $LOG_FILE 2>&1; then
        log_message "Backup dos arquivos do Redis concluído com sucesso."
    else
        local ERROR_MSG=$(tail -n 10 $LOG_FILE)
        log_message "Erro durante o backup dos arquivos do Redis: $ERROR_MSG"
    fi
}

function dump_db() {
    log_message "Iniciando exportação do dump do Redis para texto..."

    mkdir -p $BACKUP_DIR/$ME/text

    if $REDIS_CLI -h $REDIS_HOST -p $REDIS_PORT -a $REDIS_AUTH keys '*' > $BACKUP_DIR/$ME/text/keys.txt; then
        log_message "Lista de chaves exportada com sucesso."

        while read -r key; do
            echo "Key: $key" >> $BACKUP_DIR/$ME/text/dump.txt
            $REDIS_CLI -h $REDIS_HOST -p $REDIS_PORT -a $REDIS_AUTH dump "$key" >> $BACKUP_DIR/$ME/text/dump.txt 2>> $LOG_FILE
            echo "" >> $BACKUP_DIR/$ME/text/dump.txt
        done < $BACKUP_DIR/$ME/text/keys.txt

        log_message "Dump do Redis exportado para texto com sucesso."
    else
        local ERROR_MSG=$(tail -n 10 $LOG_FILE)
        log_message "Erro durante a exportação do dump do Redis: $ERROR_MSG"
    fi
}

log_message "=== Iniciando processo de backup do Redis ==="
backup_files
dump_db
log_message "=== Backup do Redis concluído ==="
