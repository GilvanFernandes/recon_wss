import subprocess 
import argparse 
import subprocess
from datetime import datetime
import time
import os

# Kevin
# Objetivo: varredura nas portas, varredura nas portas abertas 
# def execute_namp():

# Martines
# Objetivo: varredura de diretorios, 
def execute_feroxbuster(target):
    
    print('[+] Executando feroxbuster...')
    start_time = time.time()  
    clean_target = target.replace('https://', '').replace('http://', '')
    date = time.strftime("%Y%m%d", time.localtime())
    output_file = f"scan_result/{clean_target}_feroxbuster_{date}.txt"
    
   
    assets_path = os.path.join(os.path.dirname(__file__), "assets")
    wordlist_path = os.path.join(assets_path, "wordlist.txt")
    
    if os.path.exists(wordlist_path):
        command = ["feroxbuster", "-u", target, "-w", wordlist_path, "-r"]
    else:
        command = ["feroxbuster", "-u", target, "-r"]
    
    with open(output_file, "w") as f:
        subprocess.run(command, stdout=f, stderr=subprocess.PIPE)

    end_time = time.time()  
    execution_time = end_time - start_time  
    print(f'[+] Feroxbuster finalizado! Tempo de execução: {execution_time:.2f} segundos')



# Gilvan
# Objetivo: enumera subdominio
# def execute_subfinder():

# # Will
# # Objetivo: 
# def execute_nuclei():



def check_feroxbuster_installed():
    try:
        subprocess.run(["which", "feroxbuster"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False



def main():
    parser = argparse.ArgumentParser(description='Script para executar recon um alvo especificado.')
    parser.add_argument('target', type=str, help='WSS Recon (exemplo: https://sap.com)')
    
    args = parser.parse_args()

    #execute_nmap(args.target)
    execute_feroxbuster(args.target)

if __name__ == "__main__":
    main()

##python3 scan.py https://sap.com