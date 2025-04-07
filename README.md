# Projet Microservices avec Docker

Ce projet illustre une architecture microservices utilisant Docker Compose, comprenant :
- Une application web Flask
- Une base de données PostgreSQL
- Un service de traitement de données Python

## Structure du Projet
microservices-project/
├── docker-compose.yml # Configuration Docker
├── .env # Variables d'environnement
├── web/ # Application Flask
│ ├── app.py # Code principal
│ ├── requirements.txt # Dépendances Python
│ └── templates/ # Templates HTML
├── data-processor/ # Service de traitement
│ ├── processor.py # Script d'analyse
│ └── requirements.txt # Dépendances Python
└── db/ # Base de données
└── init.sql # Initialisation de la DB

Accès aux Services

    Application web : http://localhost:5000

    Base de données : postgres://admin:secret@localhost:5432/analyticsdb

Configuration

Modifiez le fichier .env pour changer :

    Identifiants de la base de données

    Nom de la base
