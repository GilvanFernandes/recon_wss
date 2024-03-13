# Contribuindo com o Projeto
Este guia irá ajudá-lo a contribuir com o projeto fazendo um fork, realizando alterações localmente e enviando um pull request.

## Passo-a-Passo para Contribuir

### 1. Faça um Fork do Repositório
- Navegue até a página do repositório original no GitHub.
- Clique no botão **Fork** no canto superior direito.

### 2. Clone o Fork para a sua Máquina Local
- Abra o terminal.
- Clone o fork utilizando o comando abaixo:
```bash
https://github.com/GilvanFernandes/recon_wss
```

### 3. Configure um Remote Upstream
- Navegue para a pasta do repositório clonado.
- Adicione o repositório original como um remote chamado `upstream`:

```bash
cd caminho/recon_wss
git remote add upstream https://github.com/GilvanFernandes/recon_wss.git
```

### 4. Faça suas Alterações Locais
- Realize as alterações necessárias no código.
- Adicione e commit suas mudanças:

```bash
git add .
git commit -m "Descrição das alterações"
```

### 5. Envie as Alterações para o seu Fork no GitHub (Push)
- Envie suas alterações com o comando:

```bash
git push origin main
```

Substitua `main` pelo nome do branch, se necessário.

### 6. Crie um Pull Request

- No GitHub, vá para a página do seu fork.
- Clique em **Pull Request** > **New Pull Request**.
- Escolha o branch correto e revise suas alterações.
- Clique em **Create Pull Request**.

## Mantendo seu Fork Sincronizado
- Atualize seu fork com as alterações do repositório original:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

Siga estes passos para contribuir de forma eficaz e manter seu fork atualizado. Obrigado pela sua contribuição!




# Guia de Instalação e Uso do Pipenv

Pipenv é uma ferramenta que visa trazer o melhor de todos os mundos (pacotes, gerenciador de dependências, etc.) para o mundo Python. Ele automaticamente cria e gerencia um ambiente virtual para seus projetos, além de adicionar/remover pacotes do seu arquivo `Pipfile` conforme você instala/desinstala pacotes.

## Pré-Requisitos

- Python 3 instalado em sua máquina.
- `pip3` instalado em sua máquina.

## Passo a Passo

### 1. Instalação do Pipenv
Para instalar o Pipenv, utilize o seguinte comando no seu terminal:

```bash
pip3 install pipenv
```

### 2. Criando um Ambiente Virtual com Pipenv
Para criar um novo ambiente virtual e ativar esse ambiente, navegue até o diretório do seu projeto e execute:

```bash
pipenv shell
```
Se o diretório do seu projeto não contiver um ambiente virtual, o Pipenv irá criá-lo automaticamente.

### 3. Instalando Pacotes com Pipenv
Para instalar um novo pacote e adicioná-lo ao seu arquivo Pipfile, use o comando:

```bash
pipenv install <nome_do_pacote>
````

Substitua <nome_do_pacote> pelo nome do pacote que você deseja instalar.

### 4. Exportando as Dependências para um arquivo requirements.txt
Para exportar as dependências do seu projeto para um arquivo requirements.txt, use o seguinte comando:

```bash
pipenv lock -r > requirements.txt
````

### 5. Saindo do Ambiente Virtual
Para sair do ambiente virtual, basta executar o comando:

```bash
exit
```