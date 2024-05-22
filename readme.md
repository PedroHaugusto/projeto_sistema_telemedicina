# Projeto Sistema de Telemedicina

Projeto WEB desenvolvido em Python + Django, um sistema completo de TeleMedicina onde um médico pode se cadastrar e um futuro paciente pode encontrar esse médico e agendar consulta.


## Pré-requisitos

Certifique-se de ter o Python e Django instalados em sua máquina. Se necessário, você pode baixar o Python [aqui](https://www.python.org/downloads/), o Django [aqui](https://www.djangoproject.com/download/).

## Passo 1: Clone o Repositório

```bash
git clone https://github.com/PedroHaugusto/projeto_sistema_telemedicina.git
```

## Passo 2: Crie e Ative o Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate      # No Windows: venv\Scripts\activate
```

## Passo 3: Instale as Dependências

```bash
pip install -r requirements.txt
```

## Passo 4: Colete os arquivos estáticos

```bash
python manage.py collectstatic --noinput
```

## Passo 5: Execute o makemigrations

```bash
    python manage.py makemigrations     #Caso não funcione, rode especificando cada pasta dentro de apps. 
                                        
```

## Passo 6: Execute as Migrações

```bash
    python manage.py migrate
```

## Passo 7: Crie um login de acesso

```bash
    python manage.py createsuperuser
```

## Passo 8: Rode o projeto

```bash
    python manage.py runserver
```