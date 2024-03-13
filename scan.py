import subprocess 
import argparse 
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
def execute_feroxbuster():



    
    print("execute_feroxbuster...")

# Gilvan
# Objetivo: enumera subdominio
def execute_subfinder(target):

    command = f'subfinder -d {target} '
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("Saída Subfinder:\n", stdout.decode())
    else:
        print("Erro Subfinder:\n", stderr.decode())

# Will
# Objetivo: 
def execute_nuclei():



    
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