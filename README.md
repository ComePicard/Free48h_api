# Free 48h API

## Guide du développeur :

### Initialisation :

Cloner le projet :
```bash
git clone <url_du_repo>
cd free48h-api
```

Créer un fichier `.env` à la racine du projet contenant les variables de connexion à la BDD:
`BDD_HOST`, `BDD_PORT`, `BDD_NAME`, `BDD_USER`, `BDD_PASS`.

Installer Docker en suivant ce [lien](https://www.docker.com/products/docker-desktop/).

Lors de l'installation, vérifiez de bien installer DockerCLI et Docker compose.

Lancer le conteneur docker de la BDD :
```
docker-compose up -d
```
Vérifier l'état de la BDD:
```
docker-compose ps
```

Installer Python 3.10 en suivant ce [lien](https://www.python.org/downloads/).

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