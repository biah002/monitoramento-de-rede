import platform
import subprocess

def verificar_conectividade(host):
    """
    Verifica se um host (endereço IP ou domínio) está acessível.
    """
    # A flag "-n 1" é para Windows. A flag "-c 1" é para Linux/macOS.
    parametro_ping = ['-n', '1'] if platform.system().lower() == 'windows' else ['-c', '1']
    
    # Executa o comando e captura a saída.
    try:
        resultado = subprocess.run(
            ['ping'] + parametro_ping + [host],
            capture_output=True,
            text=True,
            check=True
        )
        print(f'O endereço {host} está ONLINE.')
        print(resultado.stdout) # Mostra a saída do ping
    except subprocess.CalledProcessError:
        print(f'O endereço {host} está OFFLINE.')
        print('Erro: Não foi possível alcançar o host.')

# Lista de endereços para verificar
enderecos_para_verificar = ['8.8.8.8', 'google.com', '192.168.1.1', 'site-falso.com']

# Loop para verificar cada endereço na lista
for endereco in enderecos_para_verificar:
    verificar_conectividade(endereco)