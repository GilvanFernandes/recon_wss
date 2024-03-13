import subprocess 
import argparse 


# Kevin
# Objetivo: varredura nas portas, varredura nas portas abertas 
def execute_namp():

# Martines
# Objetivo: varredura de diretorios, 
def execute_feroxbuster():

# Gilvan
# Objetivo: enumera subdominio
def execute_subfinder():

# Will
# Objetivo: 
def execute_nuclei():



def main():
    parser = argparse.ArgumentParser(description='Script para executar recon um alvo especificado.')
    parser.add_argument('target', type=str, help='WSS Recon (exemplo: https://sap.com)')
    
    args = parser.parse_args()

    execute_nmap(args.target)
    execute_feroxbuster(args.target)

if __name__ == "__main__":
    main()

python3 scan.py https://sap.com