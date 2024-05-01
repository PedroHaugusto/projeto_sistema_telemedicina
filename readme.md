# Projeto Sistema de Telemedicina


## Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. Se necessário, você pode baixá-lo [aqui](https://www.python.org/downloads/).


## Passo 1: Crie e Ative o Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate      # No Windows: venv\Scripts\activate
```

## Passo 2: Execute as Migrações

```bash
python manage.py migrate
```

## Passo 3: Execute o Projeto

```bash
python manage.py runserver
```

Agora, você pode acessar o projeto em http://localhost:8000/.
    