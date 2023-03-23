# Free 48h API

## Guide du développeur :

### Initialisation :

Cloner le projet :
```bash
git clone <url_du_repo>
cd free48h-api
```

Installer Docker en suivant ce (lien)[https://www.docker.com/products/docker-desktop/].

Lors de l'installation, vérifiez de bien installer DockerCLI et Docker compose.

Lancer le conteneur docker de la BDD :
```
docker-compose up -d
```
Vérifier l'état de la BDD:
```
docker-compose ps
```

Installer les dépendances Python:
```bash
python -m pip install --upgrade pip
pip install pipenv
pipenv install --dev
```

Lancer le projet :
```bash
pipenv run python run-dev.py
```