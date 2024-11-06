#!/bin/bash

# listagem de um ou mais nfs montados
NFS_MOUNTS=(
  "/caminho/nfs3"
  "/caminho/nfs4"
  "/caminho/nfs5"
  "/caminho/nfs6"
  "/caminho/nfs7"
  "/caminho/nfs8"
  "/caminho/nfs9"
  "/caminho/nfs10"
  "/caminho/nfs11"
  "/caminho/nfs12"
  "/caminho/nfs13"
  "/caminho/nfs14"
  "/caminho/nfs15"
  "/caminho/nfs16"
  "/caminho/nfs17"
  "/caminho/nfs18"
  "/caminho/nfs19"
  "/caminho/nfs20"
  "/caminho/nfs21"
  "/caminho/nfs22"
  "/caminho/nfs23"
  "/caminho/nfs24"
  "/caminho/nfs25"
  "/caminho/nfs26"
  "/caminho/nfs27"
  "/caminho/nfs28"
  "/caminho/nfs29"
  "/caminho/nfs30"
  "/caminho/nfs31"
  "/caminho/nfs32"
  "/caminho/nfs33"
)

# diretporio onde os logs serao salvos
LOG_DIR="./nfs_logs"

# cria o diretorio se não existir
mkdir -p "$LOG_DIR"

#  for para listar a interna de cada mountpoint
for NFS_MOUNT in "${NFS_MOUNTS[@]}"; do
  # altera as barras do nome do ponto de montagem por underline para o nome do arquivo
  LOG_FILE="$LOG_DIR/$(echo "$NFS_MOUNT" | sed 's|/|_|g').log"

  if [ -d "$NFS_MOUNT" ]; then
    echo "Estrutura de diretórios para $NFS_MOUNT:" > "$LOG_FILE"
    echo "-----------------------------------------------" >> "$LOG_FILE"

    # executa o tree para listar a estrutura e imprime a saída para o log
    tree "$NFS_MOUNT" >> "$LOG_FILE"

    echo "Log de $NFS_MOUNT registrado em $LOG_FILE."
  else
    echo "Mountpoint $NFS_MOUNT não existe ou não está acessível." > "$LOG_FILE"
    echo "Log de $NFS_MOUNT gravado em $LOG_FILE com erro de acesso."
  fi
done
