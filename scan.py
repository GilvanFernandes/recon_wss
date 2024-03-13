import subprocess 
import argparse 
from datetime import datetime
import time
import os
import pandas as pd
import nmap

# Kevin
# Objetivo: varredura nas portas, varredura nas portas abertas 
def execute_namp(target):

    scanner = nmap.PortScanner()

    scanner.scan(target)

    # Print the scan results
    for host in scanner.all_hosts():
        print("Host: ", host)
        print("State: ", scanner[host].state())
        for proto in scanner[host].all_protocols():
            print("Protocol: ", proto)
            ports = scanner[host][proto].keys()
            for port in ports:
                print("Port: ", port, "State: ", scanner[host][proto][port]['state'])


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





    
    print("execute_feroxbuster...")



# # Will
# # Objetivo: 
# def execute_nuclei():


def execute_subfinder(target):

    command = f'subfinder -d {target} '
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("Saída Subfinder:\n", stdout.decode())
    else:
        print("Erro Subfinder:\n", stderr.decode())


def check_feroxbuster_installed():
    try:
        subprocess.run(["which", "feroxbuster"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False



    
    print("execute_nuclei...")


def main():
    parser = argparse.ArgumentParser(description='Script para executar recon um alvo especificado.')
    parser.add_argument('target', type=str, help='WSS Recon (exemplo: https://sap.com)')
    
    args = parser.parse_args()


    execute_namp(args.target)
    execute_feroxbuster(args.target)
    execute_subfinder(args.target)
    execute_nuclei(args.target)

if __name__ == "__main__":
    main()


# Para executar o script no terminal: python3 scan.py https://sap.com

