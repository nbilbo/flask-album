# Flask Album

Webisite para gerenciar galerias de imagens.

## Instalação

1. clone o repositorio `git clone https://github.com/nbilbo/flask-album.git`

2. mova-se para o diretorio `cd flask-album`

3. instale as dependencias `python3 -m pip install -r requirements.txt`

## Arquivo de configuração

Esse projeto utiliza variaveis de ambiente para configurar informações sensiveis; crie um arquivo `.env` no diretorio raiz do projeto e edite.

```.env
# application name.
APP_NAME='Nbilbo'

# youtube url.
YOUTUBE_URL='https://www.youtube.com/@noceunaotempao'

# github url.
GITHUB_URL='https://github.com/nbilbo'

# copyright url.
COPYRIGHT_URL='https://github.com/nbilbo'

# copyright message.
COPYRIGHT_MESSAGE='© 2024-2025 https://github.com/nbilbo'

# is used by Flask and extensions to keep data safe.
SECRET_KEY='sua-super-chave-secreta'

# database url.
SQLALCHEMY_DATABASE_URI='sqlite:///database.db'

# number of album images per page.
IMAGES_PER_PAGE_COUNT=9

# default admin name.
ADMIN_NAME='nbilbo'

# default admin username.
ADMIN_USERNAME='admin'

# default admin password.
ADMIN_PASSWORD='admin'

# cloudinary cloud name.
CLOUDINARY_NAME='your-cloudinary-cloud-name'

# cloudinary api key.
CLOUDINARY_KEY='your-cloudinary-api-key'

# cloudinary api secret.
CLOUDINARY_SECRET='your-cloudinary-secret-key'

# cloudinary folder.
CLOUDINARY_FOLDER='dev-flask-album'
```

## Execução
`export FLASK_APP=app.__init__:create_app && flask run --debug`

## Rotas
- Rota inicial http://127.0.0.1:5000

- Rota de autenticação http://127.0.0.1:5000/auth/login

- Rota de administração http://127.0.0.1:5000/admin

- Rota de api http://127.0.0.1:5000/api

## Tecnologias utilizadas
- [python](https://www.python.org/)

- [flask](https://flask.palletsprojects.com/en/stable/)

- [cloudinary](https://cloudinary.com/)

