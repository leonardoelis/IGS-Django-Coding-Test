# IGS Django Coding Test

<p>Repositório com o desafio de Django e Python da IGS. Abaixo encontram-se as instruções para rodar o projeto.</p>

### Como rodar o projeto? (Windows)
<ul>
    <li>Clone o repositório</li>
    <li>Crie um virtualenv</li>
    <li>Ative o virtualenv</li>
</ul>

```
git clone https://github.com/leonardoelis/IGS-Django-Coding-Test.git
python -m venv venv
cd venv/Scripts
activate
```
Dentro da pasta IGS-Django-Coding-Test:
<ul>
    <li>Instale as dependências</li>
    <li>Rode as migrações</li>
    <li>Crie um superusuário</li>
    <li>Rode o projeto</li>
</ul>

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```