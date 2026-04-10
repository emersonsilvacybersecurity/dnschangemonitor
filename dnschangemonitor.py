import socket
import os
import time

def check_dns_change(domain):
    log_file = f"dns_log_{domain}.txt"
    
    try:
        # Tenta obter o IP atual do domínio
        current_ip = socket.gethostbyname(domain)
    except socket.gaierror:
        print(f"[!] Erro: Não foi possível resolver o domínio {domain}")
        return

    # Se o arquivo de log não existe, cria com o IP atual
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write(current_ip)
        print(f"[*] Monitoramento iniciado para {domain}. IP atual: {current_ip}")
    else:
        # Lê o último IP registrado
        with open(log_file, "r") as f:
            last_ip = f.read().strip()

        # Compara
        if current_ip != last_ip:
            print(f"[🚨] ALERTA DE ALTERAÇÃO: {domain}")
            print(f"      IP Antigo: {last_ip}")
            print(f"      IP Novo:   {current_ip}")
            
            # Atualiza o arquivo com o novo IP
            with open(log_file, "w") as f:
                f.write(current_ip)
        else:
            print(f"[✓] {domain} continua no mesmo IP: {current_ip}")

# Configuração
alvo = "exemplo.com" # Coloque aqui o domínio que quer monitorar

check_dns_change(alvo)