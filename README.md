# monitoramento-de-rede
Um script que testa conexão de IPs e salva resultados.
# monitor.py

import os
import csv
from datetime import datetime
import platform

# --- LISTA DE ENDEREÇOS PARA MONITORAR ---
# Adicione ou remova os IPs e sites que deseja verificar.
enderecos_para_verificar = [
    '8.8.8.8',        # DNS do Google
    '1.1.1.1',        # DNS da Cloudflare
    '192.168.0.1',    # Gateway/Roteador local (exemplo)
    'google.com',
    'github.com',
    'um-site-que-nao-existe.com' # Exemplo de host inativo
]

# Nome do arquivo de saída
nome_arquivo_csv = 'resultado.csv'

def verificar_host(host):
    """
    Verifica a conectividade de um host usando o comando ping.
    Retorna True se estiver online, False caso contrário.
    """
    print(f"Verificando {host}...")
    
    # Parâmetro do ping varia com o sistema operacional
    parametro = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    
    # Executa o comando ping e suprime a saída
    comando = f"ping {parametro} {host}"
    resposta = os.system(comando + " > /dev/null 2>&1" if platform.system().lower() != "windows" else comando + " > NUL")

    # Verifica o código de saída (0 significa sucesso)
    return resposta == 0

# --- INÍCIO DO SCRIPT ---

# Pega a data e hora atuais para o registro
timestamp_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Prepara os dados para salvar
resultados = []
for host in enderecos_para_verificar:
    status = 'Online' if verificar_host(host) else 'Offline'
    resultados.append([host, status, timestamp_atual])
    print(f"-> Status: {status}")

# Salva os resultados no arquivo .csv
try:
    with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        
        # Escreve o cabeçalho
        writer.writerow(['Host', 'Status', 'Verificado em'])
        
        # Escreve os dados
        writer.writerows(resultados)
        
    print(f"\nResultados salvos com sucesso em '{nome_arquivo_csv}'")

except IOError:
    print(f"Erro: Não foi possível escrever no arquivo '{nome_arquivo_csv}'")
